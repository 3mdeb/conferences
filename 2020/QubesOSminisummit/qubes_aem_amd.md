class: center, middle, intro

# Anti Evil Maid for modern AMD<br>UEFI-based platform

### Qubes OS and 3mdeb minisummit 2020

## Michał Żygowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Agenda

* Introduction
* Evil Maid attacks
* Anti Evil Maid
* Qubes OS Anti-Evil-Maid
* Qubes OS Anti-Evil-Maid status
* Enabling AEM in Qubes OS for AMD platform
* Enabling AEM in Qubes OS for TPM2
* Demo
* Q&A

---

# Introduction

.center[<img src="/img/miczyg.png" width="220px" style="margin-top:-50px">]
.center[Michał Żygowski]
.center[_Firmware Engineer_]
.right-column50[
- Braswell SoC, PC Engines and Protectli maintainer in coreboot
- interested in:
  - advanced hardware and firmware features
  - coreboot
  - security solutions
]
.left-column50[
- <a href="https://twitter.com/_miczyg_"><img src="/remark-templates/3mdeb-presentation-template/images/twitter.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @_miczyg_</a>

- <a href="mailto:michal.zygowski@3mdeb.com"><img src="/remark-templates/3mdeb-presentation-template/images/email.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> michal.zygowski@3mdeb.com</a>

- <a href="https://www.linkedin.com/in/miczyg"><img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> linkedin.com/in/miczyg</a>

- <a href="https://www.facebook.com/miczyg1395"><img src="/remark-templates/3mdeb-presentation-template/images/facebook.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> facebook.com/miczyg1395</a>
]

---

# Evil Maid attacks

.center[<img src="/img/evil_maid.jpg" width="450px" style="centered">]

---

# Evil Maid attacks

Short recap:

- burn Evil Maid USB stick
- boot target machine from the prepared stick
- injecting key loggers, password sniffers
- wait machine owner launches the machine and types password
- boot again from Evil Maid stick
- retrieve password saved by key-logger or password sniffer on the disk
- enjoy a new laptop/PC

1st phase take about 2 minutes (first boot of Evil Maid USB and malicious
software installation). 2nd phase also may take about 2 minutes.

Very high reward ("ownership" of a new PC) at a cost of single USB stick and
some amount of time.

.footnote[
Source: __http://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html__
]

---

# Anti Evil Maid

Protection by ensuring the state of the platform.

If we can trust the hardware and software we use, can we feel safe?

How to determine if the state of the platform is trusted and
hardware/firmware/software has not been tampered?

**Trusted Execution / Trusted Computing**:

- TPM module by TCG
- Intel TXT
- AMD Secure Launch with SKINIT

---

# AEM AMD vs Intel

Short recap from Qubes OS minisummit 2019...

.right-column50[
**AMD Secure Launch**
- TPM required
- no blobs required
- implementation: Trenchboot (WIP)
- BIOS needs to enable SVM

- Only 1 SKINIT instruction
]

.left-column50[
**Intel TXT**
- TPM required
- BIOS ACM and SINIT ACM required
- implementation: tboot
- BIOS needs to enable VT-x, VT-d, load BIOS ACM
- many GETSEC sub-instructions called leaf functions
]

---

# Qubes OS Anti-Evil-Maid

`sudo qubes-dom0-update anti-evil-maid`

Additional protection:

- multi-factor with AEM USB boot device and TOTP
- using 2 AEM USB sticks in case one could be stolen
- using non-default SRK password
- using additional secret key file for LUKS on AEM USB

Attack still not prevented:

- attacker can sniff passwords, keystrokes and access AEM USB stick
- fake motherboard injection with radio link
- successful measurement bypass by buggy CRTM implementations in BIOS
- buggy BIOS updates leading to BIOS compromise
- SMM attacks leading to Intel TXT compromise (can be prevented by STM)

.footnote[
https://www.qubes-os.org/doc/anti-evil-maid/

https://github.com/QubesOS/qubes-antievilmaid/blob/master/anti-evil-maid/README
]

---

# Qubes OS Anti-Evil Maid status

.left-column50[
Qubes minisummit 2019 AEM status:

- only for Intel silicon
- not supported on UEFI installations
- TPM 1.2 only
]

.right-column50[
Current AEM status:

- not only for Intel but also for AMD silicon thanks to TrenchBoot
- can be supported by UEFI installations on AMD (not tested yet on Qubes OS)
- also available for TPM 2.0 - WIP (available at https://github.com/3mdeb/qubes-antievilmaid-amd)
]

---

# Enabling AEM in Qubes OS for AMD platform

The installation comes down to a few simple steps:

1. Use [qubes-builder](https://github.com/QubesOS/qubes-builder) to build
   necessary packages:
  - [landing-zone](https://github.com/3mdeb/qubes-landing-zone)
  - [custom GRUB2](https://github.com/3mdeb/qubes-grub2/tree/trenchboot_support)
  with TrenchBoot support
  - [Anti Evil Maid for AMD with TPM 2.0 support](https://github.com/3mdeb/qubes-antievilmaid-amd/tree/aem_amd)
2. Install _**tpm2-tools**_ and _**tpm2-abrmd**_ with _**qubes-dom-update**_.
3. Copy the built packages to Dom0 and install them with `dnf`.
4. Install the anti-evil-maid as described in [AEM README](https://github.com/3mdeb/qubes-antievilmaid-amd/blob/aem_amd/README) (WIP)
5. Test the installation by booting the Qubes OS with AEM entry. (WIP)

_*Most of these packages are still work in progress, contributions welcome.
GRUB2 support still awaits for upstream contributions. TPM 2.0 may not work
well yet.*_ **Kudos to my colleague from 3mdeb - Krystian Hebel - for help in
developing the multiboot support for Secure Launch**

---

# Enabling AEM in Qubes OS for TPM2

Challenges and differences:

- Huge specifications consuming time to get familiar with

- Software stack different than TPM 1.2 and not compatible

- Specification is written in very technical way and hard to understand

- TPM 2.0 is based on contexts

- Different approach to sealing/unsealing data

---

# Demo

## .center[Demo time...]

---

# Repositories

- landing-zone Qubes package:<br>https://github.com/3mdeb/qubes-landing-zone/tree/lz_support
- ladning-zone code: <br>https://github.com/3mdeb/landing-zone/tree/multiboot2
- GRUB2 Qubes package: <br>https://github.com/3mdeb/qubes-grub2/tree/trenchboot_support
- GRUB2 code: <br>https://github.com/3mdeb/grub2/tree/trenchboot_mb2
- Anti Evil Maid for AMD with TPM 2.0 support: <br>https://github.com/3mdeb/qubes-antievilmaid-amd/tree/aem_amd

---
class: center, middle, intro

# .center[Q&A]

---
class: center, middle, intro

# Thank you
