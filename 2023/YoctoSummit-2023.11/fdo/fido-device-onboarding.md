class: center, middle, intro

# **FIDO Device Onboarding**

# Late-binding Provisioning & Tales from the Trenches of Bleeding Edge Tech

### Yocto Summit 2023

## Tymoteusz Burak

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
src="/remark-templates/3mdeb-presentation-template/images/tymek_burak.png"
width="150px" style="marking-top:-50px"> ]

.center[Tymoteusz Burak] .center[_Junior Embedded Systems Developer_]
.right-column50[

- 6 months in 3mdeb
- Integration of functionalities and the creation of Operating Systems for
  embedded devices in Yocto
- Working on my Bachelor's Degree in Automation and Robotics ] .left-column50[
- <a href="mailto:tymoteusz.burak@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    tymoteusz.burak@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/tymoteusz-burak-a108252a0/">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/tymoteusz-burak-a108252a0
    </a>
  ]

---

# Who we are ?

.center[
.image-15[![](/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/lvfs.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)] ]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

- coreboot licensed service providers since 2016 and leadership participants
- UEFI Adopters since 2018
- Yocto Participants and Embedded Linux experts since 2019
- Official consultants for Linux Foundation fwupd/LVFS project since 2020
- IBM OpenPOWER Foundation members since 2020

---

# Agenda

- What is FDO?
- Existing implementations of FDO protocol
- Challenges faced in integrating the
  [fido-device-onboard-rs](https://github.com/fdo-rs/fido-device-onboard-rs)
  project in Yocto + Current Rust implementations inside of Yocto + Bitbake
  environment vs pkg-config
- Demo presentation
- Q&A

---

# What is FDO?

<br>
<br>

.center[

<img src="/img/fido-logo.jpeg" height="100px">

_An automatic onboarding protocol for IoT devices. Permits late binding of
device credentials, so that one manufactured device may onboard, without
modification, to many different IOT platforms_\*

]

.footnote[

\* quote from
[FIDO Device Onboard Specification 1.1](https://fidoalliance.org/specs/FDO/FIDO-Device-Onboard-RD-v1.1-20211214/FIDO-device-onboard-spec-v1.1-rd-20211214.pdf)

##### FIDO® is a trademark (registered in numerous countries) of FIDO Alliance, Inc

##### All trademarks used are properties of their respective owners

]

???

- Definition is a quote from Abstract of
  [FIDO Device Onboard Specification](https://fidoalliance.org/specs/FDO/FIDO-Device-Onboard-RD-v1.1-20211214/FIDO-device-onboard-spec-v1.1-rd-20211214.pdf)
- By allowing late binding of credentials, it provides flexibility and ease of
  deployment, as manufacturers can produce a single device that can be securely
  onboarded to different IoT platforms without needing any changes to the device
  itself. + IoT Platforms - systems or environments where IoT device operate and
  interact - For example smart home automation system.
- Originally created by Intel under the name SDO - Secure Device Onboard
  + Focused on providing zero-touch automation, scalability and enhanced
    security for device deployment.
  + Later open-sourced with the help of FIDO Alliance which created Fast
    Identity Online thus creating FDO - FIDO Device Onboarding
- Proposed Open IoT standard
  + Aims to set a new benchmark for secure and efficient onbarding for IoT
    devices
  + By being an open standard, it encourages industry-wide adoption and fosters
    innovation in IoT security

---

# What is FDO?

.left-column50[ <img src="/img/fdo_cert_chain.svg" height="460px"
style="margin-left:150px"> ]

.right-column50[ Example stakeholders:

- Distributors
- Retailers
- System Integrators
- Certification Agencies ]

???

- "We'll start simple and expand from there"
- This is the basic gist how an passwordless IoT device onboarding should look
  like with FDO
- Addresses supply chain security
  + The device has to "walk" the whole specified chain
  + If the trust is established -> provision
- Addresses password management for provisioning/onboarding
  + Devices use cryptographic keys
  + Process is automated to reduce the risk of human error

---

# What is FDO?

.left-column50[ <img src="/img/fdo_cert_chain_2.svg" height="460px"
style="margin-left:150px"> ]

.right-column50[ <img src="/img/fdo_cert_chain_2_legend.svg" height="120px"
style="margin-left:0px"> ]

???

- Visualization how the certificate travels independently
  + The created Ownership Voucher is tied to this specific device
  + Thus the device doesn't have to be powered on to sign the certificate
- Ownership Voucher holds information about every stakeholder
- Each extension of the voucher serves as a proof of legitimacy and trust for
  the next recipient in the supply chain. + If at any point in the supply chain
  the voucher is not properly extended, it breaks the chain of trust.

---

# What is FDO?

.center[ <img src="/img/fdo_protocols.svg" height="430px" width="900px"
style="margin-left:-75px"> ]

???

- Those are the protocols and entities that actually make up the FIDO Device
  Onboarding protocol
- If the chain of trust is broken the Rendezvous Server and ultimately the
  Onboarding Server will not accept the device as legitimate, leading to a
  failure in the provisioning and onboarding process.

---

# What is FDO?

.center[ <img src="/img/fdo_cert_chain_3.svg" height="460px"> ]

???

- This is how it looks in the end with all the protocols highlighted
- What mattered for us most was the late binding provisioning
- We needed to implement it inside of a Yocto project for a client
- FIDO Alliance only specified the theoretical background -> implementations
- All implementations have to implement those protocols in some way

---

# Existing implementations of FDO protocol

.center[

<br>

.right-column50[ <img src="/img/lfedge-horizontal-color.svg" height="40px"> ]

.left-column50[ <img src="/img/FIDODeviceOnboard_Logo_Color.svg" height="60px">
]

<br>
<br>
<br>

### FDO Project

]

- [client-sdk-fidoiot](https://github.com/fido-device-onboard/client-sdk-fidoiot)
- [pri-fidoiot](https://github.com/fido-device-onboard/pri-fidoiot)

???

- `client-sdk-fidoiot` is a direct descendant of
  [secure-device-onboard/client-sdk](https://github.com/secure-device-onboard/client-sdk)
  + Written in C
  + Currently supports only x86 Linux machines (Ubuntu, RHEL, Debian)
  + Is planned to support Yocto at some point
    - "The configurations mentioned in the document are not supported yet. This
      document will be updated in a future release when the source code
      implementation is updated to support the same."
    - This line is not present in the `client-sdk` repo
- The protocols can be implemented via the
  [pri-fidoiot](https://github.com/fido-device-onboard/pri-fidoiot)
- Looks promising
  + Has the potential to maybe suit the Yocto environment better
- Hard pass for now

---

# Existing implementations of FDO protocol

.center[ <img src="/img/rustacean.svg" height="130px">

### [fido-device-onboard-rs](https://github.com/fdo-rs/fido-device-onboard-rs)

]

.left-column50[

- `fdo-client-linuxapp`
- `fdo-rendezvous-server`
- `fdo-owner-onboarding-server`
- `fdo-serviceinfo-api-server` ]

.right-column50[

- `fdo-manufacturing-client`
- `fdo-manufacturing-server`
- `fdo-owner-tool` ]

???

- Developed by Fedora IoT as of recently, now the `fdo-rs` company
  + Reached out to them on matrix
  + The move to fdo-rs org was intended to represent that the FDO implementation
    is really a community effort that is distro-agnostic.
  + primary maintainers are Red Hatters working on Fedora IoT + RHEL for Edge
- Modular - functionalities in form of crates
- Looked most promising and faster to implement
  + "How hard can it be to port Rust crates to Yocto?"

---

.center[ <img src="/img/rustacean-flat-sad.svg" height="130px">

### "That should be easy right?"

]

???

- Turns out cross-compiling Rust is harder than it seemed at first

---

# State of Rust in Yocto

<br>
<br>

.left-column50[

### meta-rust

- Source-based, thus more customizable
- Allows for an offline build via `cargo-bitbake`
- Doesn't contain `cross` or `rustc-nightly` ]

.right-column50[

### meta-rust-bin

- Provides pre-built compiler and `cargo`
- Needs online build
- Allows for the use of `rustc-nightly` and `cross` ]

???

- **All was implemented for the `honister` branch**
- Both exist to satisfy different requirements
- `cargo-bitbake` generates .bb recipe from `Cargo.toml`
  + Yocto also has the `cargo-update-recipe-crates`
    - It allows for updating the cargo dependencies via bitbake -c update_crates
      recipe + Wasn't used by us as the project was done for the Honister
      version
- nightly builds of rustc contain some improvements to cross-compilation that
  will be upstreamed in the future + Besides some improvements to parallelism
  and multi-threading it adds `Cross` crate - Contenerized toolchain and
  linker - Theoretically should work - Abandoned this trope as it seemed less
  stable

---

# Bitbake environment vs pkg-config

<br>
<br>

### .center[pkg-config]

_"The `pkg-config` command usually doesn’t support cross-compilation, and this
crate prevents it from selecting incompatible versions of libraries. Setting
`PKG_CONFIG_ALLOW_CROSS=1` disables this protection, **which is likely to cause
linking errors**, unless `pkg-config` has been configured to use appropriate
sysroot and search paths for the target platform."_

[docs.rs/pkg_config](https://docs.rs/pkg-config/latest/pkg_config/)

???

- The Host dependencies were also built using the pkg-config and used aarch64
  flags
- The reverse happened for linker
  [meta-rust issue#431](https://github.com/meta-rust/meta-rust/issues/431)

---

# Bitbake environment vs pkg-config

<br>
<br>

.code-11px[

```bitbake
# By default pkg-config variables point to aarch64 libraries which are picked up
# during x86_64 builds, this causes aarch64 include directories and linker
# search paths to into x86_64 builds, causing problems.
#
# Host libraries already use absolute paths so set sysroot to /
export PKG_CONFIG_SYSROOT_DIR="/"
export PKG_CONFIG_PATH="${RECIPE_SYSROOT_NATIVE}/usr/lib/pkgconfig:${RECIPE_SYSROOT_NATIVE}/usr/share/pkgconfig"
export PKG_CONFIG_LIBDIR="${RECIPE_SYSROOT_NATIVE}/usr/lib/pkgconfig"
export PKG_CONFIG_DIR="${RECIPE_SYSROOT_NATIVE}/usr/lib/pkgconfig"

# Those variables are handled internally by pkg-config crate.
# All paths are relative to sysroot, so set PKG_CONFIG_SYSROOT_DIR
# The PKG_CONFIG_*_{TARGET} needs underscores in it's triple instead of hyphens

export PKG_CONFIG_TARGET_VAR = "${@d.getVar('TARGET_SYS').replace('-','_')}"

do_compile:prepend() {
    export PKG_CONFIG_SYSROOT_DIR_${PKG_CONFIG_TARGET_VAR}="${RECIPE_SYSROOT}"
    export PKG_CONFIG_PATH_${PKG_CONFIG_TARGET_VAR}="${RECIPE_SYSROOT}/usr/lib/pkgconfig:${RECIPE_SYSROOT}/usr/share/pkgconfig"
    export PKG_CONFIG_LIBDIR_${PKG_CONFIG_TARGET_VAR}="${RECIPE_SYSROOT}/usr/lib/pkgconfig"
    export PKG_CONFIG_DIR_${PKG_CONFIG_TARGET_VAR}="${RECIPE_SYSROOT}/usr/lib/pkgconfig"
}
```

]

---

# Bitbake environment vs pkg-config

### openssl-kdf

```rust
let kdf_h_cts = std::fs::read_to_string("/usr/include/openssl/kdf.h").unwrap();
```

???

- Cargo's are not standardized
  + In the above example the library paths are hard-coded
  + This doesn't work well with Yocto and Bitbake

---

# Bitbake environment vs pkg-config

```rust
fn read_header(lib: &pkg_config::Library, path_rel: &str) -> std::io::Result<String> {
    for dir in lib
        .include_paths
        .iter()
        .map(|p| p.as_path())
        .chain(std::iter::once(std::path::Path::new("/usr/include")))
    {
        match std::fs::read_to_string(dir.join(path_rel)) {
            Ok(r) => return Ok(r),
            Err(e) if e.kind() == std::io::ErrorKind::NotFound => continue,
            Err(e) => return Err(e),
        }
    }

    return Err(std::io::ErrorKind::NotFound.into());
}

```

```diff
-   let openssl_version = openssl.version;
+   let openssl_version = &openssl.version;
```

```diff
-   let kdf_h_cts = std::fs::read_to_string("/usr/include/openssl/kdf.h").unwrap();
+   let kdf_h_cts = read_header(&openssl, "openssl/kdf.h").unwrap();
```

???

- Function that uses pkg-config to dynamically find needed libraries
- `pkg-config` proved most useful despite previously getting in our way
  + `pkg-config` provides a unified interface for querying installed libraries
    for the presence of particular software packages, along with their version
    numbers and other information

---

# Bitbake environment vs pkg-config

### devicemapper-sys

```diff
+   let library = pkg_config::probe_library("devmapper").unwrap();
```

```diff
+   .clang_args(
+       library.include_paths
+           .iter()
+           .map(|path| format!("-I{}", path.to_string_lossy())),
+   )
```

???

- Similar story, missing clang arguments
- pkg-config can be very versatile with its use cases

---

<br>
<br>
<br>

## .center[Live Demo]

???

- systemctl restart fdo-client-linuxapp
- journalctl -u fdo-client-linuxapp

---

# meta-fdo

<br>
<br>
<br>
<br>

### [3mdeb/meta-fdo](https://github.com/3mdeb/meta-fdo)

### [Image used for demo](https://cloud.3mdeb.com/index.php/s/8ofCq3MNGzR7Z79)

---

# Resources

- https://fidoalliance.org/
- https://fido-device-onboard.github.io/docs-fidoiot/latest/
- https://www.lfedge.org/projects/fidodeviceonboard/
- https://docs.rs/pkg-config/latest/pkg_config/

<br>
<br>
<br>
<br>
<br>

### Contact

- <a href="mailto:leads@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    leads@3mdeb.com
  </a>
- <a href="mailto:tymoteusz.burak@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    tymoteusz.burak@3mdeb.com
  </a>

---

<br>
<br>
<br>

## .center[Q&A]
