class: center, middle, intro

# Dealing with UEFI Secure Boot support using Yocto Project

### Yocto Summit 2023

## Tomasz Żyjewski

<img
  src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# Agenda

* `whoami`
* Who we are?
* Recap from first part
  - booting secure embedded device
  - UEFI Secure Boot
  - meta-secure-core
  - running image with UEFI Secure Boot integrated
* Build improvements
* UEFI Secure Boot compliance
* Keys management
* CI/CD integration
* Demo

---

# `whoami`

.center[<img
  src="/remark-templates/3mdeb-presentation-template/images/tomasz_zyjewski.png"
  width="150px">]

.center[Tomasz Żyjewski]
.center[_Embedded Systems Team Leader_]
.right-column50[
- over 4 years in 3mdeb
- integration of update systems and OS creation for embedded devices
- system security
]
.left-column50[
- <a href="https://twitter.com/tomzy_0"><img
  src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
  width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @tomzy_0</a>
- <a href="mailto:tomasz.zyjewski@3mdeb.com"><img
  src="/remark-templates/3mdeb-presentation-template/images/email.png"
  width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  tomasz.zyjewski@3mdeb.com</a>
]

---

# Who we are ?

.center[.image-15[![](/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)].image-15[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)].image-15[![](/remark-templates/3mdeb-presentation-template/images/lvfs.png)].image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)]]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

- coreboot licensed service providers since 2016 and leadership participants
- UEFI Adopters since 2018
- Yocto Participants and Embedded Linux experts since 2019
- Official consultants for Linux Foundation fwupd/LVFS project since 2020
- IBM OpenPOWER Foundation members since 2020

---

# Recap from first part

.center[<img src="../../img/secure_boot.svg" width="720px">]

???

* Booting secure device
  - Root of Trust (RoT): source that can always be trusted within a
    cryptographic system
  - Chain of Trust (CoT): ensuring that each subsequent element launched on the
    device can be trusted, and thus verified by the previous element
* Ensure that every stage of booting is verified
* Let's focus on the process from powering up the platform to running the
  operating system
  - vary depending on the architecture we are dealing with
  - in cases with UEFI Secure Boot we can talk about multistages boot chain
    consist of BIOS, Bootloader, Kernel, OS

---

# Recap from first part

* Explained in chapter 32 of UEFI Specification
  - information from there should always take precedence over other documents
* Key goal
  - provide infrastructure for UEFI Image load time authentication
  - UEFI Secure Boot authenticates OS Loaders and UEFI drivers
  - Platform Owner manage platfrom's security policy and can check integrity and
    security of a given UEFI Image
* The subject of UEFI Secure Boot is very complex and multi-level
  - we will cover about 1%
  - want to focus on integrating that within Yocto Project
* Worth to check available training courses
  - https://p.ost2.fyi/

???

* Explained in chapter 32 of UEFI Specification
  - information from there should always take precedence over other documents
* Key goal
  - provide infrastructure for UEFI Image load time authentication
  - UEFI Secure Boot authenticates OS Loaders and UEFI drivers
  - Platform Owner manage platfrom's security policy and can check integrity and
    security of a given UEFI Image
* UEFI Secure Boot is controlled by a set of UEFI Authenticated Variables
  which specify UEFI Secure Boot Policy
* UEFI Secure Boot Policy determine which images and certificates are
  allowed and which are not allowed to be loaded

---

# Recap from first part

* meta-secure-core overview:
  - provides couple of common and platform-specific security features
  - repository: https://github.com/jiazhang0/meta-secure-core

.center[<img src="../../img/meta-sec-core-over.svg" width="720px">]

???

---

# Recap from first part

* For test we used `meta-dts` layer
  - repository: https://github.com/Dasharo/meta-dts
* Status

.center[<img src="../../img/poc-state.svg" width="720px">]

---

# Build improvements

???

remove manual steps

---

# Build improvements

???

sbctl

---

# Build improvements

???

integrating more meta-signing-keys

---

# Build improvements



---

# UEFI Secure Boot compliance

* Importance of UEFI Secure Boot compliance
  - enhanced system security
  - regulatory and industry standards
  - system reliability and trust
* Tools
  - built-in UEFI menu
  - cmdlines utilities; e.g. `sbctl` on Linux, `bcdedit` on Windows
  - third-party tools
* Key management in context of compliance
  - verification not only of the implementation itself but also of maintenance
  - maintaining trust and integrity
  - adaptability and control


???

---

# UEFI Secure Boot compliance

* Test environment
.center[<img src="../../img/hw-sw-setup.svg" width="360px">]

* Remote Testing Environment
.left-column50[
* docs: https://docs.dasharo.com/transparent-validation/rte/introduction
* layer: https://github.com/3mdeb/meta-rte]
.right-column50[.center[<img src="../../img/rte-v1.1.0-trans.jpg" width="240px">]]

???


---

# UEFI Secure Boot compliance

* UEFI Secure Boot compliance for Dasharo
  - https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot
  - verifies basic functionality against UEFI specifications
  - can be used for different BIOS but need proper setup
* Tests logic
  - list of steps
  - simple, unambiguous actions to be carried out
  - every test verifies one isolated scenario
* Robot Framework
  - generic open source automation framework
  - implemented in Python
  - tests code: https://github.com/Dasharo/open-source-firmware-validation

---

# UEFI Secure Boot compliance

.center[<img src="../../img/uefi-sb-tests.svg" width="360px">]

---

# UEFI Secure Boot compliance

* Future improvements
  - we can come up with a lot of different scenarios
  - should comply with the UEFI Secure Boot specification
* Additional tests to consider
  - testing the execution of correctly signed firmware when the built-in RTC
    (Real-Time Clock) is malfunctioning, affecting certificate date verification
  - testing the execution of file signed for intermediate certificate
  - testing the range of supported cryptographic algorithms in the firmware

---

# Keys management

* Investigating meta-signing-key

.code-11px[
```bash
λ tree -L 2
.
├── classes
│   └── user-key-store.bbclass
├── conf
│   └── layer.conf
├── COPYING.MIT
├── files
│   ├── boot_keys
│   ├── ima_keys
│   ├── modsign_keys
│   ├── mok_sb_keys
│   ├── rpm_keys
│   ├── secondary_trusted_keys
│   ├── system_trusted_keys
│   └── uefi_sb_keys
├── README.md
├── recipes-devtools
│   ├── libsign
│   └── sbsigntool
├── recipes-support
│   └── key-store
└── scripts
    ├── create-user-key-store.sh
    └── openssl.cnf
```
]

---

# Keys management

.center[<img src="../../img/using-dev-keys.png" width="720px">]

* Last time we used dev keys provided in meta-signing-key
  - investigate `create-user-key-store.sh` script

---

# Certificate rotation

.center[<img src="../../img/uefi_sb_cert_rotation.svg" width="720px">]

* Certificate rotation using meta-secure-core
  - on host, generate certs, update build environment, rebuild and sign
    components
  - on target, apply update, enroll certificate

---

# CI/CD integration

* Speed-up processes
.center[<img src="../../img/ci_cd-icons.png" width="450px">]
* Presentation example
  - automatic release on tag pushed
  - setup with KAS tool
  - Yocto sstate-cache integrated

---

# CI/CD integration

* Current solution

.center[<img src="../../img/ci_cd-setup.svg" width="720px">]

---

# CI/CD integration

* Target solution

.center[<img src="../../img/ci_cd-setup-target.svg" width="720px">]

---

# Demo

* Demo scenario
  1. Generate custom keypair
  1. Build signed image to provision UEFI Secure Boot certificates via Automatic
     Certificate Provision
  1. Boot custom Linux-based operating system, signed with generated keys
  1. Generate new keypair, build another image, try to boot on platform
* Presentation

???

1. Generate custom keypair
2. Use signed image to provision SB certificates via Automatic Certificate
   Provision
3. Try to boot Ubuntu
4. Try to boot signed image

---

# Summary

* As on Yocto Summit 2022.11, we again leaned into the meta-secure-core and UEFI
  Secure Boot intergration in Yocto-based projects
* We have fixed several bugs and integrated another UEFI Secure Boot status tool
  into the system
* We devoted this year's presentation to additional aspects of maintaining a
  project with UEFI Secure Boot enabled
  - testing of the compliance
  - keys management
  - CI/CD integration

---
# Resources

* https://docs.oracle.com/en/operating-systems/oracle-linux/notice-sboot/OL-NOTICE-SBOOT.pdf


---

<br>
<br>
<br>
## .center[Q&A]
