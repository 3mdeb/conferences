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
    consist of BootROM, System ROM, Bootloader, OS

---

# Recap from first part

* Explained in chapter 32 of UEFI Specification
  - information from there should always take precedence over other documents
* Key goal
  - provide infrastructure for UEFI Image load time authentication
  - UEFI Secure Boot authenticates OS Loaders and UEFI drivers
  - Platform Owner manage platfrom's security policy and can check
    check integrity and security of a given UEFI Image
* UEFI Secure Boot is controlled by a set of UEFI Authenticated Variables
  which specify UEFI Secure Boot Policy
* UEFI Secure Boot Policy determine which images and certificates are
  allowed and which are not allowed to be loaded
* The subject of UEFI Secure Boot is very complex and multi-level
  - we will cover about 1%
  - want to focus on integrating that within Yocto Project
* Worth to check available training courses
  - https://p.ost2.fyi/

---

# Recap from first part

* meta-secure-core overview:
  - provides couple of common and platform-specific security features
* Divided into 9 sublayers
  - every one provide some functionality
  - every one got its own README with more detailed description
* Repository: https://github.com/jiazhang0/meta-secure-core
* meta-efi-secure-boot
  - provides extensive description through README
* Describes samples keys provided via `meta-signing-key`
  - those provides PK, KEK, DB and DBX
  - deployed into DEPLOYDIR on successful build
* Here we also have `Quick Start For The First Boot` section
* Gives description of verification procedure

---

# Recap from first part

* For test we used meta-dts layer
  - repository: https://github.com/Dasharo/meta-dts
* Platform used: NovaCustom NV4x 11th Gen (Tiger Lake)
  - https://configurelaptop.eu/nv41-series/
  - with Dasharo deployed
* Image compilation finished successfully
  - we produced .wic.gz file
* Modification needed while running "Automatic Certificate Provision"
  - failed on finding boot option
  - needed to manually deploy efi/EFI/BOOT into boot partition instead of
    EFI/BOOT
  - kernel command line definied wrongly
  - finally were able to verify Secure Boot state with `mokutil`

---

# Build improvements

---

# Build improvements

---

# Build improvements

---

# Build improvements

---

# UEFI Secure Boot compliance

---

# UEFI Secure Boot compliance

---

# UEFI Secure Boot compliance

---

# UEFI Secure Boot compliance

---

# UEFI Secure Boot compliance

---

# Keys management

---

# Keys management

---

# Keys management

---

# CI/CD integration

---

# CI/CD integration

---

# CI/CD integration

---

# Demo

???

1. Generate custom keypair
2. Use signed image to provision SB certificates via Automatic Certificate
   Provision
3. Try to boot Ubuntu
4. Try to boot signed image

---

# Summary


---
# Resources


---

<br>
<br>
<br>
## .center[Q&A]
