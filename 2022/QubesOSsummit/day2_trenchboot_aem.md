class: center, middle, intro

# TrenchBoot - the only AEM-way to boot Qubes OS

### Qubes OS Summit 2022

## Michał Żygowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Agenda

* Introduction
* Qubes OS Anti Evil Maid
* Qubes OS AEM status
* TrenchBoot project
* TrenchBoot as DRTM provider for Anti Evil Maid
* Project plans
* Demo
* Q&A

---

# `whoami`

.center[<img src="/img/miczyg.png" width="180px" style="margin-top:-60px">]
.center[Michał Żygowski]
.center[_Firmware Engineer_]
.right-column50[
* Braswell SoC, PC Engines and Protectli maintainer in coreboot
* OpenPOWER System Software Technical Workgroup chair
* 5 years in Open Source Firmware
* interested in advanced hardware and firmware security features
* OST2 instructor
* TrenchBoot developer
]

.left-column50[
* <a href="https://twitter.com/_miczyg_"><img src="/remark-templates/3mdeb-presentation-template/images/twitter.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @\_miczyg\_</a>

* <a href="mailto:michal.zygowski@3mdeb.com"><img src="/remark-templates/3mdeb-presentation-template/images/email.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> michal.zygowski@3mdeb.com</a>

* <a href="https://www.linkedin.com/in/miczyg"><img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> linkedin.com/in/miczyg</a>

* <a href="https://www.facebook.com/miczyg1395"><img src="/remark-templates/3mdeb-presentation-template/images/facebook.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> facebook.com/miczyg1395</a>
]

---

# Who we are ?

.center[.image-15[![](remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)] .image-15[![](remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)] .image-15[![](remark-templates/3mdeb-presentation-template/images/lvfs.png)] .image-15[![](remark-templates/3mdeb-presentation-template/images/yocto.png)]]
.center[.image-35[![](remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

* coreboot licensed service providers since 2016 and leadership participants
* UEFI Adopters since 2018
* Yocto Participants and Embedded Linux experts since 2019
* Official consultants for Linux Foundation fwupd/LVFS project since 2020
* IBM OpenPOWER Foundation members since 2020

---

# Qubes OS Anti Evil Maid

* Qubes OS Anti Evil Maid is a set of software packages and utilities to aid
  against [Evil Maid attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)
* **Requires TPM and Dynamic Root of Trust for Measurement (DRTM)** technology from
  silicon vendor to be present and supported by the firmware

.center.image-50[![](/img/qubes_trenchboot_aem/evil_maid.png)]

---

# Anti Evil Maid protection

**Questions:**

* Can we trust hardware features silicon vendors provide?
* If we can trust the hardware and software we use, can we feel safe?
* How to determine if the state of the platform is trusted and
  hardware/firmware/software has not been tampered?

**Solution:**

* Protection by ensuring the state of the platform
* Additional TOTP codes and secret sealing in TPM
* Trusted Execution / Trusted Computing:
    - TPM module by TCG
    - Intel TXT (DRTM)
    - AMD Secure Startup (DRTM)

---

# AEM AMD vs Intel

.left-column50[

### Intel TXT

* TPM required (discrete or integrated)
* BIOS ACM and SINIT ACM required
* Implementation: tboot
* BIOS needs to enable IOMMU, load and execute BIOS ACM
* Software needs to execute SINIT ACM (GETSEC\[SENTER\])
* Many GETSEC sub-instructions called leaf functions
]

.right-column50[

### AMD Secure Startup

* Discrete TPM required (integrated not supported?)
* No blobs required
* Implementation: TrenchBoot
* BIOS only needs to enable SVM
* Software needs to execute a 64KB module (can be self-written) with SKINIT
  instruction
* Only 3 instructions: SKINIT/STGI/CLGI
]

---

# Qubes OS Anti Evil Maid

`sudo qubes-dom0-update anti-evil-maid`

**Additional protection:**

* Multi-factor with AEM USB boot device and TOTP
* Using 2 AEM USB sticks in case one could be stolen
* Using non-default SRK password
* Using additional secret key file for LUKS on AEM USB

**Attack still not prevented:**

* Attacker can sniff passwords, keystrokes and access AEM USB stick
* Fake motherboard injection with radio link
* Successful measurement bypass by buggy CRTM implementations in BIOS
* Buggy BIOS updates leading to BIOS compromise
* SMM attacks leading to Intel TXT compromise

---

# AEM current status

Current upstream status:

* **only for Intel** silicon
* **not** supported on **UEFI** installations
* **TPM 1.2 only**

Ongoing work:

* [On QubesOS Summit 2020](https://www.youtube.com/watch?v=rM0vRi6qABE) a PoC
  has been shown on AMD hardware that integrated TrenchBoot framework into GRUB
  and used SKINIT to extend the Xen and Dom0 to PCRs 17 and 18.
* Efforts to further extend the AEM support with TrenchBoot are ongoing

---

# TrenchBoot project

### .center[TrenchBoot is a framework that allows individuals and projects to build security engines to perform launch integrity actions for their systems.]

.center.image-40[![](/img/qubes_trenchboot_aem/trenchboot_logo.png)]

* The framework builds upon Boot Integrity Technologies (BITs) that establish
  one or more Roots of Trust (RoT) from which a degree of confidence that
  integrity actions were not subverted.
* https://trenchboot.org/

---

# TrenchBoot project

* Boot Integrity Technologies (BITs):
* Intel TXT
* AMD Secure Startup
* Currently targets Linux and GRUB
    - Patches for Intel TXT on [grub-devel](https://mail.gnu.org/archive/html/grub-devel/2020-05/msg00011.html)
    - Patches for Intel TXT on [lkml](https://lwn.net/Articles/860350/)
* 3mdeb implemented AMD Secure Startup Support thanks to
  [NlNet NGI ZERO PET](https://nlnet.nl/project/OpenDRTM/)
    - Linux Secure Launch
    - Xen Secure Launch
    - GRUB support for SKINIT
    - Secure Kernel Loader extension with TPM event log

.center.image-80[![](/img/qubes_trenchboot_aem/nlnet.png)]

---

# TrenchBoot as DRTM provider for AEM

* TrenchBoot may fill the gap of missing hardware support

* Hardware agnostic support for DRTM: both Intel and AMD

* Support for TPM2 regardless of boot mode: UEFI or legacy

* Decreased TCB due to removal of persistent tboot kernel

---

# TrenchBoot AEM project plans

### Phase 1 (currently ongoing)

* Replace existing tboot implementation with TrenchBoot equivalent
* Support for Intel TXT and TPM 1.2
* Remove tboot kernel
* Reference hardware for testing:
    - Dell OptiPlex 9010 SFF (Intel Ivybridge, TPM 1.2 legacy boot)
    - Lenovo Thinkpad x230 (Intel Ivybridge, TPM 1.2 legacy boot)

.left-column50[
.center.image-40[![](/img/qubes_trenchboot_aem/optiplex-desktop-9010.png)]
]
.right-column50[
.center.image-60[![](/img/qubes_trenchboot_aem/lenovo_x230.png)]
]

---

# TrenchBoot AEM project plans

### Phase 2

* Extend AEM scripts with TPM 2.0 support
* Reference hardware for testing:
    - Protectli VP4670 (Intel Gen Comet Lake with TPM1.2 and TPM 2.0, legacy
    boot)

.center.image-60[![](/img/qubes_trenchboot_aem/protectli_vp46.png)]

---

# TrenchBoot AEM project plans

### Phase 3

* Integrate AMD Secure Startup support in AEM
* Reference hardware for testing:
    - ASUS KGPE-D16 (AMD OPtoren 15h family with TPM 1.2 and TPM 2.0, legacy boot)
    - Supermicro MS11SDV (AMD EPYC 3000 with TPM1.2 and TPM2.0, legacy boot)

.left-column50[
.center.image-85[![](/img/qubes_trenchboot_aem/Asus_KGPE_D16_1.png)]
]
.right-column50[
.center.image-65[![](/img/qubes_trenchboot_aem/M11SDV-8C-LN4F.png)]
]

---

# TrenchBoot AEM project plans

### Phase 4

* Support DRTM in Xen in UEFI mode
* Remove dependency on UEFI Boot Services in Xen for a cleaner separation
  between firmware and Qubes OS
* Make GRUB pass all information required by Xen via multiboot tags
* Reference hardware for testing:
    - Supermicro MS11SDV (AMD EPYC 3000 with TPM1.2 and TPM2.0, legacy and UEFI
    boot)

.center.image-30[![](/img/qubes_trenchboot_aem/M11SDV-8C-LN4F.png)]

---

# Demo

## .center[DEMO time!]

---

# Summary

* Anti Evil Maid is an awesome feature of Qubes OS
* Not easy to maintain and improve (mainly due to complexity of DRTM
  technologies and/or firmware stacks - UEFI vs legacy)
    - Probably the main reason why it hasn't moved forward much for the past few
    years
* AEM requires DRTM technology to be present and supported by firmware, which
  limits the hardware choice drastically (at least Intel-based)
* Open-source firmware still pursues correct support for Intel TXT on newer
  devices
* TrenchBoot can bring solution to almost all missing pieces in Qubes OS Anti
  Evil Maid

---

## .center[Q&A]

---

class: center, middle, intro

# Thank you
