class: center, middle, intro

# Challenges and Status of Enabling TrenchBoot in Xen Hypervisor

### Xen Project Summit 2024

## Michał Żygowski

<img src="../../remark-templates/3mdeb-presentation-template/images/logo.png"
     width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img src="../../remark-templates/3mdeb-presentation-template/images/miczyg.png"
             width="200px" style="margin-top:-50px">]
.center[Michał Żygowski]
.center[_Firmware Engineer_]
.right-column50[
- Braswell SoC, PC Engines, Protectli MSI MS-7D25/MS-7E06 maintainer in coreboot
- dedicated to the open-source firmware since 2017
- interested in advanced hardware and firmware security features
]
.left-column50[
- <a href="https://twitter.com/_miczyg_">
  <img src="../../remark-templates/3mdeb-presentation-template/images/twitter.png"
       width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  @\_miczyg\_
  </a>
- <a href="mailto:michal.zygowski@3mdeb.com">
  <img src="../../remark-templates/3mdeb-presentation-template/images/email.png"
       width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  michal.zygowski@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/miczyg">
  <img src="../../remark-templates/3mdeb-presentation-template/images/linkedin.png"
       width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  linkedin.com/in/miczyg
  </a>
- <a href="https://www.facebook.com/miczyg1395">
  <img src="../../remark-templates/3mdeb-presentation-template/images/facebook.png"
       width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  facebook.com/miczyg1395
  </a>
]

---

# D-RTM and S-RTM

.center[.image-90[![](/img/DRTM_flow.png)]]

<!-- Source: diagrams/DRTM_flow.drawio.xml -->

???

S-RTM complexity

- How hard it is to maintain firmware updates for correctly deployed S-RTM
  protection?
  * modern x86 platform may have 20 different keys and certificates
- How useful are information gathered during measured boot?
  * event log quality
  * forward sealing and updates

- DRTM can reestablish the trust at (theoretically) any moment of platform
  uptime
- The only prerequisite is the BIOS to initialize the D-RTM technology
  properly (only applicable to Intel TXT, AMD does not need special
  initialization from BIOS side, except keeping SVM enabled)
- Performs secure measurement of the environment responsible for launching the
  target software/operating system
  * Lesser complexity -> less things can go wrong
  * Less components to measure -> simpler event log, easier forward sealing
    and updates management
- Trust rooted only in the silicon/microcode (at least for x86 architecture)

- **D-RTM Configuration Environment (DCE) Preamble** - responsible for
  platform configuration and initiating **Dynamic Launch Event (DL Event)**
- **D-RTM Configuration Environment (DCE)** - entered via **DL Event**,
  performs DLME measurement and hands off the control to it
- **Dynamically Launched Measured Environment (DLME)** - the ultimate result
  of the dynamic launch, which effectively can be OS or bare metal software
- D-RTM does not care about initial measurements since it use PCR[17-22]
  which are locked until DL Event unlocks them in TPM locality 4

---

# TrenchBoot

.center[.image-50[![](/img/tb_logo.svg)]]

- [TrenchBoot Mailing List](https://groups.google.com/forum/#!forum/trenchboot-devel)
- The `#OSFW-Trenchboot` channel on [Matrix](https://matrix.to/#/#OSFW-Trenchboot:matrix.org)
  * Bridged with `#trenchboot` channel on [OSFW Slack](https://slack.osfw.dev)
- Twitter [@TrenchBoot](https://twitter.com/trenchboot)

???

TrenchBoot is a framework that allows individuals and projects to build
security engines to perform launch integrity actions for their systems. The
framework builds upon Boot Integrity Technologies (BITs) that establish one or
more Roots of Trust (RoT) from which a degree of confidence that integrity
actions were not subverted is derived.

The first TrenchBoot D-RTM implementation has been made for GRUB+Linux

---

# TrenchBoot vs TrustedBoot

.left-column50[

### TrustedBoot

- TrustedBoot (tboot) supports only Intel TXT
- Is an exokernel and Xen (or any other kernel) has to be aware of its
  presence
- Supports Linux and multiboot protocols
- Requires a couple of lines to be added to GRUB menu configuration file
]
.right-column50[

### TrenchBoot

- Aims for unified approach supporting AMD, Intel and ARM processors
- The goal is to implement a native support for D-RTM to let Xen have full
  control without any exokernels
- Potential to boot with any protocol/bootloader
- Needs just 1 or 2 lines to be added to perform DRTM launch
]

???

Some may know about tboot - Intel TXT reference implementation

With native support for DRTM, there are some additional steps to be performed
before the CPUs may be initialized (wait for SIPI state). There is also a
matter of handling power state transitions and event log.

---

# Usecase: Qubes OS Anti Evil Maid

.center[.image-30[![](/img/qubes-logo-home.svg)]]

- Qubes OS Anti Evil Maid (AEM) is a set of software packages and utilities to
  aid against [Evil Maid attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)
- Leverages DRTM and TPM to seal secrets, which are used by the owner to
  confirm whether the device has been tampered with or not
- Initially only Intel TXT and TPM1.2 with tboot was supported using legacy
  BIOS boot mode, now TrenchBoot replaces tboot, extending the support to
  TPM2.0 and AMD SKINIT

---

# Demo: Qubes OS Anti Evil Maid

.left-column50[

<a href="https://asciinema.org/a/661622?cols=80&rows=24"
target="_blank"> <img src="https://asciinema.org/a/661622.svg" width="400px"/></a>

]

.right-column45[

- **Hardware**: Protectli VP4670
- **TPM**: Infineon SLB9665 LPC TPM 2.0
- **Firmware**: Dasharo (coreboot+SeaBIOS) v0.9.0
  * coreboot 24.02.01
  * SeaBIOS rel-1.16.3
- **Software**:
  * [Qubes OS R4.2.1](https://www.qubes-os.org/downloads/#qubes-release-4-2-1)
  * [Xen 4.17.4 (AEM v0.4.1)](https://github.com/TrenchBoot/xen/releases/tag/v0.4.1)
  * [GRUB2 2.06 (AEM v0.4.1](https://github.com/TrenchBoot/grub/releases/tag/v0.4.1)
  * [Anti-Evil-Maid v0.4.1](https://github.com/TrenchBoot/qubes-antievilmaid/releases/tag/aem_v0.4.1)
- **Issue**: [Xen is booting very slowly after Dynamic
  Launch](https://github.com/TrenchBoot/xen/issues/16)

]

.footnote[
Watch on [asciinema](https://asciinema.org/a/661622?cols=80&rows=24)<br>
Installation instructions on [3mdeb blog](https://blog.3mdeb.com/2024/2024-04-11-aem_phase4/)
]

---

# Current status of the work

.center[.image-90[![](/img/aem_progress_2024.png)]]

.center[.image-40[![](/img/logo/nlnet.svg)]]

- https://github.com/TrenchBoot/trenchboot-issues/milestones

???

The project, sponsored by NLnet, is split into phases, where each phase builds
on the previous one and enables more usage scenarios.

Since the last year we progressed pretty significantly and finalize subsequent
3 phases.

---

# Phase 2 - TPM 2.0 support

.center[.image-95[![](/img/tb_aem_phase2.png)]]

???

- Added TPM 2.0 support for dom0 kernel and initrd measurements
- Added eventlog extraction and parsing
- Implemented support for booting with Intel TXT and TPM 2.0 in legacy BIOS
  boot mode

---

# Phase 3 - TrenchBoot boot protocol

.center[.image-95[![](/img/tb_aem_phase3.png)]]

???

- Rebased changes onto the most recent TrenchBoot support patches to Linux
  kernel introducing a unified TrenchBoot boot protocol
- Final shape of patches is not yet determined, the work on finalizing the
  boot protocol including UEFI boot mode is pending on the [Linux kernel
  mailing list, currently patchset
  v9](https://lkml.org/lkml/2024/5/30/1226)

---

# Phase 4 - AMD support

.center[.image-95[![](/img/tb_aem_phase4.png)]]

???

- Implemented support for booting with AMD SKINIT and TPM 1.2/2.0 in legacy
  BIOS boot mode
- Implemented the newest TrenchBoot boot protocol in the Secure Kernel Loader
- Simplified installation of the required packages by providing a RPM
  repository for Qubes OS

---

# Try TrenchBoot

It is relatively easy to get a hardware which supports DRTM:

- Intel-based tested and known to work:
  * Protectli VP4670 (open-source-firmware supported)
  * Dell OptiPlex 7010/9010 (open-source-firmware supported)
  * HP EliteDesk 800 G2 Desktop Mini

.center[
.image-20[![](/img/VP4600.png)]
.image-10[![](/img/tb_aem_optiplex.png)]
.image-20[![](/img/hp_elitedesk_800_g2.jpg)]
]

- AMD-based tested and known to work:
  * Terminal HP T630

.center[.image-20[![](/img/hp_t630.png)]]

???

These are the tested platforms that are working well. We have also faced
issues with other platforms with BIOS bugs, which could not be workarounded,
like Lenovo M920 or Supermicro M11SDV.

Not all Intel platform support DRTM technology - Intel TXT. It requires a
capable CPU and chipset. Typically vPro platforms satisfy these requirements,
although it is still possible to have a Intel TXT initialization bug in BIOS,
which prevents using DRTM unless a BIOS fix is issued.

For AMD platforms, almost every CPU supports AMD SKINIT (CPU needs to support
SVM basically and BIOS must not disable it).

---

# Current ongoing efforts

- Provide package repositories for other major distros (Debian, Ubuntu Fedora)
- Prepare tools for assessing the readiness of the system and BIOS to perform
  Dynamic Launch
- Adding DRTM Ready indicator to the system security reports: Qubes OS Security
  Report, [fwupd HSI](https://fwupd.github.io/libfwupdplugin/hsi.html)

.center[.image-40[![](/img/qubes-sec-report.png)]]

---

# Phase 5 - Xen as DLME for UEFI boot mode

.center[.image-85[![](/img/tb_roadmap.png)]]

More details about Secure Launch on [trenchboot.org](https://trenchboot.org/specifications/Secure_Launch/)

???

- Xen will be able to initiate the DL Event via the code module exposed by DCE
  Preamble (GRUB)
  * Although Xen does not use that much information from UEFI we want to unify
    the flow with TrenchBoot implementation for Linux kernel
  * Native EFI PE entry point shall be supported for UEFI Secure Boot purposes
- Xen will need to obtain the module from Secure Launch Resource Table linked
  in the EFI System Table Configuration Tables
- Xen will fill the necessary information for the DCE (like Xen address in
  memory to be measured) and call the module

---

<br>
<br>
<br>
## .center[Q&A]
