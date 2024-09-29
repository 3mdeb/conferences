## Kudos for review and feedback

* Ross Philipson
* Daniel P. Smith
* Andrew Cooper
* Richard Pesaud

---

# Glossary

* LVFS - Linux Vendor Firmware Service
* HSI - Host Security ID
* HCL - Hardware Compatibility List
* FSF RYF - Free Software Foundation, Respect Your Freedom
* SMM - System Management Mode
* TEE - Trusted Execution Environment
* AMD PSP/ASP - AMD Platform Security Processor/AMD Security Processor
* Intel PPAM - Intel Platform Properties Assessment Module
* TCG DICE - Trusted Computing Group, Device Identifier Engine
* UEFI - Unified Extensible Firmware Interface
* OCP - Open Compute Project
* SNIA - Storage Networking Industry Association
* DMTF SPDM - Distributed Management Task Force, Security Protocol and Data Model

<!--

This presentation use abbreviations heavily, please referee to glossary if any
is not clear.

-->

---

## Goal

The presentation highlights five challenging areas and activities related to
Linux-based system booting and security from platform vendor and user
perspective.

The focus is on:
* Highlighting the problems to provide inspiration and work as an anchor for
future CfP processes. We see challenges and issues in the open source communities
in various areas, including only sometimes being able to get domain experts in
these topics.
* Make valuable references to past events.
* Get feedback on what is missing.

<!--

Those challenges are probably known to most of you, but let it be warmup.

-->

---

## Challenge 1: Assessment

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/2024/LPC/qos_sec_report.png" width="240"/>
  <img src="/2024/LPC/device-security-screenshot.png" width="260"/>
  <img src="/2024/LPC/firmware-security.png" width="260"/>
</div>

* Lack of OS awareness about hardware security capabilities leads to the
inability to evaluate and improve system security posture.
* Over the last two years, we have seen number of various communities
approaching this topic.
  - GNOME introduced the Device Security Settings page (based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html)).
  - KDE Plasma added Firmware Security page (based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html)).
  - Qubes OS Security Report (based on Qubes HCL).
  - FSF RYF Certification (unclear rules).

---
clicks: 4
---

## Assessment

* Some interfaces for CPU assessment already exist. We have tools like:
  - `lscpu`, which shows `/sys/devices/system/cpu/vulnerabilities`.
  - `/proc/cpuinfo` bugs.
* We could only secure our ecosystem if we knew what security mechanisms are
available on a given piece of hardware.
* Shipping hardware with Linux would be more challenging without exposing the
interface, which will help assess security configuration and help protect
against misconfiguration of security features.
* Achieving results requires broader cooperation between communities and vendors.
* Followed presentations and communities discussed this topic:
  - [Embedded Recipes: LVFS: The next 50 million firmware updates](https://embedded-recipes.org/2022/wp-content/uploads/2022/06/LVFS-ER-avec-compression.pdf).
  - [TrenchBoot Summit: LVFS Host Security ID (HSI) and Silicon-Based Core Security](https://www.youtube.com/live/xZoCtNV8Qs0).
  - Arm SystemArchAC Security Sub-team.

<!--

[click] many tools focus x86 UEFI ecosystem and compliance with silicon vendor
recommendations (hence OF != UEFI),

[click] How would we know that correct version of SBAT was applied and correct
revocation data included?

[click] How we would realize we booting Your-Favourite-IBV BIOS, U-Boot with
UEFI payload support or coreboot with UEFI Payload, or maybe different
combination? Or maybe we should admit we don't care about about niche use
cases.

[click] LVFS HSI brings some assumptions
  - arbitrary ranking, not actively maintained, limited number of security
capabilities enumeration,
  - limited support for hypervisor-based OSes (Qubes OS, xcp-ng, Proxmox),
of the system.

-->

---
clicks: 2
---

# Challenge 2: SMM (TEE?) as Chain of Trust Gap

* For various reasons, vendors add secure areas that try to guarantee the
confidentiality and integrity of the code and data inside it.
* This creates an exciting attack target that has been abused many times
in the past.
* Solutions:
  - SMI Transfer Monitor - Linux driver [out of
  tree](https://github.com/EugeneDMyers/stm_linux_module), probably far from
  making it first-class citizen.
  - Project Mu - has an SMM Supervisor integrated on top of STM API. Microsoft
  Secured Core PC makes it a requirement, as does other SMM threat-mitigating
  technology.
  - Ron Minnich: [Let's move SMM out of firmware and into the kernel](https://www.youtube.com/watch?v=6GEaw4msq6g).
* Followed presentations and communities discussed this topic:
  - [BSides Portland: ABC to XYZ of Writing System Management Mode (SMM) Drivers](https://youtu.be/BQajtsy6kp0).
  - [Dasharo Dev vPub: Overview of the Intel SMI Transfer Monitor on Dasharo Firmware](https://youtu.be/3PmOcjQX-9Y).
* SMM (TEE?), by definition, should not give direct access to the user, but it
needs to communicate the platform security state to the user. Is there a place
for it in the Linux kernel?

<!--

[click] Vendor value-added stuff very often lead to security by obscurity or
bloating something what was working quite not bad. It is very hard to keep KISS
with such powerful extension at hand. So we invent cure for the poison we
created.

[click] Brian Delgado from Intel and Eugene Mayers implemented and integrated
couple PoC. Unfortunately not much traction.

-->

---
clicks: 5
---

# Challenge 3: All your hardware belong to us
* The growth of hardware and firmware components like AMD PSP features, Intel
PPAM and ME features, or MS Pluton, and how those effectively block/enable
building trustworthy systems by the open-source community.
* In parallel, this creates an ecosystem in which we cannot leverage the the
full potential of hardware and firmware in our machines.
* On one side, this is an attack vector that we cannot do anything about. On
the other side, our hardware no longer belongs to us if anyone is surprised by
that fact.
* Followed presentations and communities discussed this topic:
  - [BlackHat: Breaking Firmware Trust From Pre-EFI: Exploiting Early Boot Phases](https://youtu.be/Z81s7UIiwmI)
  - [SMM isolation - SMI deprivileging (ISRD)](https://tandasat.github.io/blog/2024/02/29/ISRD.html)
* Why did it all happen?
  - [USENIX ATC '21/OSDI '21 Joint Keynote Address-It's Time for Operating Systems to Rediscover Hardware](https://www.youtube.com/watch?v=36myc8wQhLo)

<!--

[click] MS Pluton:
- chip-to-cloud technology
- Services
- hardware-based root of trust,
- secure identity,
- secure attestation,
- crypto,
Full potential can be leveraged only by MS Windows, and Linux gets fTPM.
- this is not the first tech that an open ecosystem cannot leverage,
- do we own our computers?

[click] Satoshi Tanada has excellent posts on his blog explaining how ISDR (aka
Devil's Gate Rock) works. Intel PPAM. The critical point is that no one can leverage it
except those with excellent vendor relations. Without working Intel
PPAM, our system is potentially more vulnerable. How many of us can verify if we
have a correctly working Intel PPAM module on our computers? It applies to all
Hardware Shield Technologies.

[click] AMD PSP features
- AMD attestation and SMM supervisor in the same problem category as Intel PPAM
and Management Engine.
- SMM Containerization is controlled by a key that you write to MSR, without
key your hypervisor is out of luck, and all your VMs are not protected

[click] Alex Matrosov and his Binarly team are closely looking at those components
and report CVEs.

[click] Timothy Roscoe from ETH Zurich has some criticism and reasons for
existence of peripheral processors and, IMHO, TEE firmware features, too.
-->

---
clicks: 4
---

# Challenge 4: Root of Trust

* There are promising plans for defeating the lack of consistent assessment,
implementation, and provisioning of Root of Trust on very different hardware
configurations through Caliptra, DICE, SPDM, and more, as well as what impact
it may have on the OS.
* Some SPDM-related patches are slowly landing in Linux.
* Followed presentations and communities discussed this topic:
  - [UEFI Forum: Using SPDM in UEFI for Device Attestation](https://youtu.be/RJHd3Mqk4Uw).
  - [OCP: OCP Attestation using SPDM and DICE](https://youtu.be/qO2BrMZZy2Y).
  - [OCP: TPM Transport Security: Defeating Active Interposers with DICE](https://youtu.be/DKfbkOTYzOU).
  - [OCP: And Update on Caliptra](https://youtu.be/DKfbkOTYzOU).
  - [SNIA: TCG DICE & DMTF SPDM Binding Overview](https://youtu.be/fxp7UHFaBLs).

<!--

[click] how attestation of Caliptra RoT would look like?

[click] In Caliptra there is plan to expose API which would serve as a signing
oracle for SPDM responder in SOC, as well as authentication to a discrete TPM
devices. Can we think that Linux could somehow help users and vendors expose
that information for better platform security?

[click] ASpeed 2700, OpenBMC, which is specialized Linux distro may have
support for Caliptra

[click] Narrow group who work on that.

- https://lkml.org/lkml/2024/6/8/175
- https://lkml.org/lkml/2023/1/26/305

-->

---

# Challenge 5: What we can do better with DRTM for AMD

<v-clicks>

  * Lessons learned from the 11-th series of making 20+ year-old security tech
  for Intel CPUs first-class citizens in the Linux kernel.
  * Make sure to consider platform-specific challenges and architectural
  alignment (Intel vs AMD, ARM inclusion). Design a robust ABI framework up
  front to reflect this.
  * Consider configuration impacts and document them upfront (e.g., KASLR,
  IOMMU in the Linux kernel).
  * Check various compilers and build environments from the beginning. Ensure
  successful builds with the new features turned on and off in the
  configuration.

</v-clicks>

---

# Challenge 5: What we can do better with DRTM for AMD

<v-clicks>

  * Plan for all entry points and boot protocols (32/64 bit, legacy/UEFI). Note
  that the upstream work assumes 64b environments to run in, but it should
  build in all environments
  * Be willing to accommodate feedback and suggestions where possible and
  attempt to get assistance from the community (e.g., WAIT/MONITOR,
  linker-based `kernel_info` placement).
  * Avoid tight coupling to specific hardware behaviors (e.g., TPM access).
  * Is there anything missing?

</v-clicks>

<!--

Why D-RTM is important?
- it brings some tools for assessment of platforms security,
- it provide as complete support for the components, which belongs to group of
vendor value added hardware features and TEE firmware to open ecosystem,
- it aligns with ideas for modern Root of Trust, device identity and attestation
It is not ideal, but we can build more on it and experience we gathered.

-->
---
layout: cover
background: /intro.png
class: text-center

---

# Q&A

piotr.krol@3mdeb.com

<!--

TODO: how conferences link with above topics?

- Common git repo for hosting Boot-firmware
- Accelerating Linux Kernel Boot-Up for Large Multi-Core Systems
- [LVFS HSI] Leveraging and managing SBAT revocation mechanism on distribution level
- [LVFS HSI] Using U-boot as a UEFI payload
- [LVFS HSI] no more bootloader: please use the kernel instead
- [LVFS HSI] OF != UEFI
- [LVFS HSI] Measured Boot, Secure Attestation & co, with systemd
- [AMD TrenchBoot] Secure Launch - DRTM solution on Arm platforms

It looks like Kirk Brannock (Intel author of PPAM whitepaper) has retired,
along with our request for more documentation.  We need to:
- Get a message to Intel to ask for PPAM docs through official channels.  Also
via Vincent Z and anyone else we know there.
- Reverse engineer PPAM calls made by Microsoft Windows launch.  What's the
best way to go about doing this: boot Windows on a bare-metal device with debug
UEFI device that is logging all interactions with boot loader / OS?  boot
Windows 11 on QEMU?
- 3mdeb should have NDA access to the Intel documentation for PPAM.
- You can give that document name and relevant page numbers to Brian.
- PPAM docs are available to 3mdeb.
- We can tell Intel that we want to get support into upstream Linux as part of
LSL and that it will be much slower and more expensive to do it later.  Public
docs are needed to support the OSS work.
- What you need is PPAM User Guide (doc 604868). It is for PPAM 1.1 and
describes the VMCALL interface between MLE and PPAM.

-->
