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

* Previous presentation: https://www.youtube.com/watch?v=OA9TKkwFFIE
  - enabling UEFI Secure Boot on x86 platform with Yocto: getting started with
    meta-secure-core

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

* Building `iso` image
  - one of the requirements of base image
  - introduces regression
* Error

.code-11px[
```bash
| install: cannot stat '/build/tmp/deploy/images/genericx86-64/grub-efi-bootx64.efi':
  No such file or directory
| WARNING: exit code 1 from a shell command.
| DEBUG: Python function do_bootimg finished
ERROR: Task (/repo/meta-dts-distro/recipes-dts/images/dts-base-sb-image.bb:do_bootimg)
  failed with exit code '1'
```
]

* Solution
  - temporary: `IMAGE_FSTYPES:remove = "iso"`
  - cause of issue: `live-vm-common.bbclass` and `efi_populate_common` function

???

remove manual steps

---

# Build improvements

* Corect binaries in `/boot` partition
  - we need signed `grubx64.efi`
  - BIOS looks for `bootx64.efi`
* Signed `grubx64.efi`
  - signed by `grub-efi-efi-secure-boot.inc`
  - other binary provided while creating rootfs
  - workaround to deploy proper binary
* Signed `bootx64.efi`
  - signed by `shim_git.bb`
  - `bootx64.efi` deployed to DEPLOY_DIR
  - add `bootx64.efi;EFI/BOOT/ \` to `IMAGE_EFI_BOOT_FILES`

???

sbctl

---

# Build improvements

* sbctl
  - Secure Boot key manager
  - dependencies: `util-linux`, `binutils`, `Go`, asciidoc
  - another tool for Secure Boot management (similar to mokutil)
* Features
  - user-friendly
  - manages secure boot keys
  - live enrollment of keys
  - signing database to help keep track of files to sign
  - JSON output
* Recipe `sbctl_0.12.bb`
  - binary release installation
  - do not want to add golang to Yocto cache yet
  - missing in Yocto recipe index

???

integrating more meta-signing-keys

---

# Build improvements

* meta-signing-key
  - `create-user-key-store.sh` execution
  - creates user keys
* Output
.code-11px[
```bash
MASTER_KEYS_DIR = "/home/tzyjewski/projects/dts/meta-secure-core/meta-signing-key/scripts/user-keys"
IMA_KEYS_DIR = "${MASTER_KEYS_DIR}/ima_keys"
IMA_EVM_KEY_DIR = "${MASTER_KEYS_DIR}/ima_keys"
RPM_KEYS_DIR = "${MASTER_KEYS_DIR}/rpm_keys"
BOOT_KEYS_DIR = "${MASTER_KEYS_DIR}/boot_keys"
MOK_SB_KEYS_DIR = "${MASTER_KEYS_DIR}/mok_sb_keys"
SYSTEM_TRUSTED_KEYS_DIR = "${MASTER_KEYS_DIR}/system_trusted_keys"
SECONDARY_TRUSTED_KEYS_DIR = "${MASTER_KEYS_DIR}/secondary_trusted_keys"
MODSIGN_KEYS_DIR = "${MASTER_KEYS_DIR}/modsign_keys"
UEFI_SB_KEYS_DIR = "${MASTER_KEYS_DIR}/uefi_sb_keys"
GRUB_PUB_KEY = "${MASTER_KEYS_DIR}/boot_keys/boot_pub_key"
GRUB_PW_FILE = "${MASTER_KEYS_DIR}/boot_keys/boot_cfg_pw"
OSTREE_GPGDIR = "${MASTER_KEYS_DIR}/rpm_keys"
RPM_GPG_NAME = "PKG-Prod"
RPM_GPG_PASSPHRASE = "root"
RPM_FSK_PASSWORD = "root"
BOOT_GPG_NAME = "BOOT-Prod"
BOOT_GPG_PASSPHRASE = "root"
OSTREE_GPGID = "PKG-Prod"
OSTREE_GPG_PASSPHRASE = "root"
OSTREE_GRUB_PW_FILE = "${GRUB_PW_FILE}"
```
]
* Add to kas config file

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
* Next slides will present the results

???

1. Generate custom keypair
2. Use signed image to provision SB certificates via Automatic Certificate
   Provision
3. Try to boot Ubuntu
4. Try to boot signed image

---

# Demo

* Generate custom keypair
  - `create-user-key-store.sh`
  - take a list of inputs

.code-11px[
```bash
λ ./scripts/create-user-key-store.sh
KEYS_DIR: /home/tzyjewski/projects/dts/meta-secure-core/meta-signing-key/scripts/user-keys
Enter RPM/OSTree GPG keyname (use dashes instead of spaces) [default: PKG-SecureCore]: PKG-Sec
Enter RPM/OSTree GPG e-mail address [default: SecureCore@foo.com]: tomasz.zyjewski@3mdeb.com
Enter RPM/OSTREE GPG comment [default: Signing Key]: Prod Key
Using boot loader gpg name: BOOT-Sec
Using boot loader gpg email: tomasz.zyjewski@3mdeb.com
Using boot loader gpg comment: Prod Key
    Press control-c now if and use -bn -bm -bc arguments if you want
    different values other than listed above
Enter RPM/OSTREE passphrase: root
Enter IMA passphrase: root
Enter boot loader GPG passphrase: root
Enter boot loader locked configuration password(e.g. grub pw): root
```
]

* Creates `key.conf` mentioned earlier, need to be put in `local.conf`

---

# Demo

* For `Automatic Certificate Provision` process mention manual certs removal
  - go inside BIOS Menu
  - remove KEK, PK certs and databases
  - we cannot enable Secure Boot with PK removed
* With Secure Boot disabled boot image from USB

.code-11px[
```bash
Booting `Automatic Certificate Provision`
/EndEntire
file path: /ACPI(a0341d0.0)/PCI(0.14)/USB(0.0)
  /HD(1.800.14bfc.b030108e00000)/File(\EFI\BOOT)/File(\LockDown.efi)/EndEntire
Platform is in Setup Mode
Created KEK Cert
Created db Cert
Created dbx Cert
Created PL Cert
Platform is in User Mode
Platform is set to boot securely
Prepare to execute system warm reset after 3 seconds...
```
]

---

# Demo

* Boot testing
  - we removed default certs, so we should not be able to run Ubuntu/Windows
  - only our image should be able to boot
* Ubuntu/Windows
.code-11px[
```bash
SecureBoot is enabled
Booting `Windows Boot Manager` failed due to `Access Denied`.
Press any key to continue...
```
]
* Custom image
  - boots `grub`
  - enabling `UEFI_SB` add password protection, e.g. to change cmdline
  - here `root/root`

---

# Demo

* Scenario where we want to rotate our certificate
  - rerun script to generate new keys
  - rebuild images
* Any of images could not be boot (Ubuntu/Windows/custom)
.code-11px[
```bash
SecureBoot is enabled
Booting `Windows Boot Manager` failed due to `Access Denied`.
Press any key to continue...
```
]
* We could rerun `Automatic Certificate Provision` or investigate `sbctl` to
  rotate certs on live image

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

* https://p.ost2.fyi/
* https://uefi.org/specs/UEFI/2.10/
* https://docs.oracle.com/en/operating-systems/oracle-linux/notice-sboot/OL-NOTICE-SBOOT.pdf
* https://github.com/Wind-River/meta-secure-core

---

<br>
<br>
<br>
## .center[Q&A]
