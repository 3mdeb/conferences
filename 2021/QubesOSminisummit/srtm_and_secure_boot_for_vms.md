class: center, middle, intro

# S-RTM and Secure Boot for VMs

### Qubes OS mini-summit 2021

## Piotr Król

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---
# `whoami`

.center[<img src="/remark-templates/3mdeb-presentation-template/images/piotr_krol.jpg" width="150px">]

.center[Piotr Król]
.center[_3mdeb Founder & CEO_]

.left-column55[
* coreboot contributor and maintainer
* Conference speaker and organizer
* Trainer for military, government and industrial organizations
* Former Intel BIOS SW Engineer
]

.left-column45[
* 12yrs in business
* Qubes OS user since 2016
* C-level positions in<br>
.image-30[![](remark-templates/3mdeb-presentation-template/images/3mdeb.svg)]
.image-30[![](remark-templates/3mdeb-presentation-template/images/lpnplant.png)]
.image-30[![](remark-templates/3mdeb-presentation-template/images/vitro.svg)]
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
  - Our Firmware Engineer Michał is chair of SSWG since 2021

---
# Agenda

* Presentation goal and terminology
* S-CRTM
* What happen over last year in S-RTM and Secure Boot
  - key takeaways
* Challenges
* Q&A

---

# Presentation goal

### .center[To discuss state of integration of various S-RTM and verified boot technologies for virtual machines]

* There are many topics involved and we need some checkpoints to gather and
  discuss how things going on
* It is always good to have resources where developers can quickly grasp what
  is current state of the art

---

# Little bit about terminology

* **S-RTM** (_Static-Root of Trust for Measurement_) in reality would be either
  **S-CRTM** (_Static-Code/Core Root of Trust for Measurement_) or **S-HRTM**
  (_Static-Hardware Root of Trust for Measurement_)
  - static in this case means point in time in contradiction to dynamic, which
    would be arbitrary point in time of platform operation
  - we are not aware of any widely available S-HRTM (despite many pretend to be implemented in hardware)
* **Secure Boot** was used just for presentation marketing and general
  understanding of topic
  - **Secure Boot** term is technically imprecise what will be explained later
  - we will use verified boot term
* Depending on situation if Root of Trust is used for Measurement or/and
  Verification, we should use S-CRTM, S-CRTV, S-CRTMV

---

# Little bit about terminology

* System ROM - place where boot firmware is stored
* Boot process according to Platform Initialization (PI) and Unified Extensible
  Firmware Interface (UEFI) specifications, which are controlled by UEFI Forum
  - **SEC** - Security Phase, first boot phase according to PI specification
  - **PEI** - Pre-EFI Initialization
  - **DXE** - Driver Execution Environment
  - **BDS** - Boot Device Selection
* **TPM** - Trusted Platform Module international standard for secure cryptoprocessor

---

# S-CRTM

.center[.image-99[![](/img/s-crtm.svg)]]

* Saying "Secure Boot" typically means all security technologies in red
* In a reasonably secure world:
  - S-CRTM would implementation would be open (LibreBMC? lpnTPM?)
  - System ROM would contain Open Source Firmware without binary blobs
  - Bootloader/OS/Hypervisor would use standardized way for taking over and continuing chain of trust

---

# How is this related to VMs?

.center[.image-99[![](/img/scrtm_for_vms.svg)]]

* Without chain of trust rooted in Static Root of Trust for Measurement and
  Verification both VM measured boot and verified boot adds nothing (or very
  little) to security properties of the system
  - this could be fixed by D-RTM and TrenchBoot project
  - it does not mean we shouldn't try to create PoC and experiment with
    solution that moves us towards measured and verified boot for VMs as
    default for our systems
* Further we discuss what happen over last year in scope of measured and
  verified boot

???

* S-RTM builds foundation for transitive trust chain which establish chain of
  trust e.g. during boot process (aka measured boot)
* Real value came from verification of gathered measurements (aka Attestation)
  or unlocking secret when measurements are correct&trade; (aka Sealed Storage)
* Both attestation and sealed storage may have interesting use cases in virtual
  machine world
  - hardened ChallengerVM that attest AppVMs measurement
  - LUKS2 encrypted disk of AppVMs that decrypts only in light of correct PCR
    value
* S-RTM implies use of TPM, what may give further security benefits by enabling
  new use cases
  - secure storage
  - entropy source
  - key hierarchies
* To limit what software may be run in VM
  - From VM users perspective it gives software authenticity assurance
  - From VMs admin perspective it adds way of differentiating VMs between critical (with verified boot) and
* We can allow only software components signed by us or trusted parties to boot
  VM
* To comply with some software standards or regulations
  - especially valid for UEFI Secure Boot and Microsoft certifications

# Why we discussing SRTM and Secure Boot together

* Windows requires both features
* Having both is better for security
* Both cannot work without correctly implemented Root of Trust

---

# What happen in the topic over last year

* May 2020: Qubes OS mini-summit
  - [SRTM for Qubes OS VMS](https://youtu.be/Eip5Rts6S2I) - Piotr Król, 3mdeb
  - Discussion after the talk with Andrew and Marek
* Mar 2021: Xen Secure Boot and Lockdown WG Meeting
* May 2021: Xen Developer & Design Summit 2021
  - [Enabling UEFI Secure Boot on Xen](https://youtu.be/A_IhKjK7EgA) - Bobby Eshleman, Vates SAS
  - [Alternative vTPM 2.0 Backend to Comply with Upcoming SVVP Changes](https://www.youtube.com/watch?v=ZFaJQCxHbhY) - Igor Druzhinin, Citrix
* XCP-ng work around Secure Boot for VMs
* Trammel work around swtpm and safeboot
* Not directly involved by may affect openness of discussed solutions
  - LibreBMC
  - lpnTPM

---

# SRTM for Qubes OS VMS

.center[.image-70[![](/img/srtm_for_qubes_os_vms.png)]]

* TCG Roots of Trust and practical use cases of those for VM environment
* Design ideas and limitation of introducing TPM through QEMU features
* Introduced swtpm and potential configurations that can leverage it
* Outdated vTPM architecture and 3mdeb's dream design
* assumptions and potential future idea for TPM usage in Qubes OS


---

# Key takeaways

* Building features in correct order is key to accomplish anything meaningful
  - however it is important to proceed with PoC and testing, since problem is
    complex, so we should divide and conquer
* There are significant difference how this could be handled by various types
  of VMs: PV, HVM, PVHVM, Xen/Arm, PVH
  - PVH seem to be the trend so considerations related to QEMU become obsolete
    and there is need to have TPM PV driver
* Look into "Virtualized Trusted Platform Architecture Specification"

---

# TCG VPWG Architecture

* 2011 spec covers architecture, terminology, deployment models and properties
  that virtualised trusted computing platforms (vPlatform) are expected to offer
  - great food for thought for anyone working on vTPMs and virtual root of trusts
* Use cases
  - Creating a New vPlatform (e.g. OS requires certain TC properties)
  - Instantiating a Previously Executed vPlatform (e.g. after migration or shutdown)
  - vPlatform Operation (e.g. any application using TPM in virtualized OS)
  - Hot Stand-by (e.g. when high availability trusted vPlatfroms are needed)
  - vPlatform Upgrade
  - vPlatform Migration (e.g. migration based on attestation result)

.footnote[https://trustedcomputinggroup.org/wp-content/uploads/TCG_VPWG_Architecture_V1-0_R0-26_FINAL.pdf]

---

# TCG VPWG Architecture

.center[.image-99[![](/img/vpas_three_layer.png)]]

---

# TCG VPWG Architecture

.center[.image-90[![](/img/vpas_attestation.png)]]
---

# Enabling UEFI Secure Boot on Xen

.center[.image-40[![](/img/enabling_uefi_secure_boot_on_xen.png)]]

* Presentation discussed
  - what is Secure Boot and how it works
  - key hierarchy for UEFI Secure Boot
  - chain of trust in shim-present system and how it can be used on Xen systems
  - various configurations in which Xen can leverage UEFI Secure Boot and its limitations
* Side note: Microsoft CA as signing authority
  - according to rumors, they took that position because nobody else in UEFI
    Forum wanted or had capability

---

# Potential configurations

.center[.image-80[![](/img/xen_and_shim.svg)]]

* Key problem with this configuration is that it works only with xen.efi
  PE/COFF, but not with multiboot1/2, what means maintenance of multiple Xen
  build targets and lack of legacy support
* This configuration works for unified (including cmdline, params etc.) and not-unified xen.efi

---

# Potential configurations

.center[.image-80[![](/img/xen_shim_grub.svg)]]

* GRUB2 currently support GnuPG detached signatures and Shim compatible
  verifier
  - it means this configuration give ability to support different then UEFI
    chain of trust schemes
* [Deniel Kiper talk from PSEC 2018 discuss UEFI Secure Boot, Xen and Shim](https://www.platformsecuritysummit.com/2018/speaker/kiper/)
  - this patches were picked by XCP-ng team
  - there is ongoing discussion on xen-devel


---

# Key takeaway

* From Bobby email to xen-devel, the goal is to have Xen binary that can be:
  * Verifiable with shim (PE/COFF)
  * booted on BIOS platforms via grub2
  * booted on EFI platforms via grub2 or EFI loader
* Both Linux and Xen suffer from the same issue, which is potential of using
  some software features to subvert at runtime security properties provided by
  UEFI Secure Boot - Linux addressing that through Linux Kernel Lockdown
* This problem means locking down some features and that's why Xen Lockdown is
  the thing which have to be addressed first to get value from Secure Boot
    - Linux Kernel Lockdown would be used as model
    - unfortunately it would not be enough, because of the dom0 superpowers

.footnote[https://man7.org/linux/man-pages/man7/kernel_lockdown.7.html]

---

# Key takeaway

* From OSF, Qubes OS and Xen project perspective we should think how to not
  break LVFS/fwupd and other firmware update methods, while implementing Xen
  Lockdown
    - we know that assuming proprietary/IBV SMM-based updates are the solution
      is not the way to go

---

# vTPM 2.0 and SVVP

* Recent Microsoft Server Virtualization Validation Program seem to put
  pressure on hypervisors providers in light of TPM2.0 support
  - this may revive old vTPM Xen architecture in long run
  - it make TCG VPWG Architecture and its use cases relevant
  - it cloud be another use for swtpm in Xen
* Certification will start very soon (H1'21)

---

# XCP-ng UEFI Secure Boot for VMs

* Current state of the work related to Secure Boot is on Github: https://github.com/beshleman/xcp-host-secure-boot
* VMs using OVMF already support Secure Boot
* based on compilation and provisioning process all required UEFI databases can
  be populated according to user or admin needs
* One of the discussion threads: https://github.com/xcp-ng/xcp/issues/294
* Kudos to XCP-ng team for picking up the topic

---

# Secure Boot and Lockdown WG

* Meeting was initiated by Olivier from XCP-ng team and happen 29th March 2021
  and gathered quite big crowd
* Key accomplishment was gathering of requirements for Xen Lockdown
* Verified boot chain
* Linux Lockdown - basic stuff seem to work with Qubes OS but more testing is needed
* Xen Lockdown work items
  - Live patching
  - kexec
  - /priv/cmd
  - PCI pass-through
  - QEMU
  - command line

---

# OSFW Slack

* Trammel and couple other people work with swtpm, kexec and safeboot
* They proved it to work in couple scenarios
  - coreboot+heads testing in QEMU
  - OVMF testing in QEMU
  - attestation for both above cases
  - kexec Windows
  - safeboot support
* Overall this effort proves swtpm in various use cases discussed in this
  presentation

---

# Challenges

* Wide spread and it will definitely take time to enable all necessary component
* Luckily presented concepts are already on corporate agenda and there is some pressure to move some of mentioned concepts forward
* verified boot (including UEFI Secure Boot) needs
  - hardware root of trust
  - correctly implemented chain of trust
  - ideally if would support provisioning and re-owning using open tools
  - verified boot for VMs does not have those properties, so it is as good as
    the weakest component executed before (BIOS, firmware, hypervisor, dom0)
* covering hypervisor and dom0 with verified boot is challenging
  - BIOS and firmware should already be covered by other verified boot technologies (coreboot vboot, UEFI Secure Boot)
  - Xen verified boot has similar challenges as Linux - this was covered by Linux lockdown mechanism

---

<br>
<br>
<br>
## .center[Q&A]
