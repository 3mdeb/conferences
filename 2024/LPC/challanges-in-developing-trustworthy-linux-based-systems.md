## Goal

The presentation highlights five challenging areas and activities related to
Linux-based system booting and security from platform vendor and user
perspective.

The focus is on:
* Highlighting the problem to provide inspiration and work as anchor for future
CfP process, because we see challenges and issues in community in various areas
and not always can get domain experts in those topics.
* Make useful reference to past events.
* Get feedback what is missing.

<!--

Those challenges are probably known to most of you.

-->

---

## Assessment

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/2024/LPC/qos_sec_report.png" width="240"/>
  <img src="/2024/LPC/device-security-screenshot.png" width="260"/>
  <img src="/2024/LPC/firmware-security.png" width="260"/>
</div>

* Lack of OS awareness about hardware security capabilities leads to the
inability to evaluate and improve system security posture.
* Over last two years we have inflation of various communities approaching this
topic.
  - GNOME introduced Device Security Settings page (based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html))
  - KDE Plasma added Firmware Security page (based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html))
  - Qubes OS Security Report (based on Qubes HCL)
  - FSF RYF Certification (unclear rules)

---

## Assessment

* LVFS HSI brings some assumptions
  - focus x86 UEFI ecosystem and compliance with silicon vendor recommendations
  (hence OF != UEFI),
  - arbitrary ranking, not actively maintained, limited number of security capabilities enumeration,
  - limited support for hypervisor-based OSes (Qubes OS, xcp-ng, Proxmox),
of the system.
* Without exposing interface which will protect against misconfiguration of
security features shipping hardware with Linux would be harder.
* We don't know how to secure our ecosystem because we
don't know what mechanisms are available on given hardware. Current approach is
spread in ecosystem, but it is very challenging to achieve something useful
without wide cooperation.
* Topic was discussed on:
  - [Embedded Recipes: LVFS: The next 50 million firmware updates](https://embedded-recipes.org/2022/wp-content/uploads/2022/06/LVFS-ER-avec-compression.pdf)
  - [TrenchBoot Summit:LVFS Host Security ID (HSI) and Silicon-Based Core Security](https://www.youtube.com/live/xZoCtNV8Qs0)
  - Arm SystemArchAC Security Sub-team

<!--

- Security capabilities enumeration is big issue for fwupd/LVFS HSI as well as
for rest of the ecosystem. We don't know how to secure our ecosystem because we
don't know what mechanisms are available on given hardware. Current approach is
spread in ecosystem, but it is very challenging to achieve something useful
without wide cooperation.

-->

---

# SMM (TEE?) as Chain of Trust Gap

* For various reason vendors add secure area which can guarantee the
confidentiality and integrity of the code and data inside it. This create very
interesting attack target abused many times in the past.
* Closing System Management Mode (SMM)-created gap in an open-source way.
* Solutions:
  - SMI Transfer Monitor - Linux driver [out of tree](https://github.com/EugeneDMyers/stm_linux_module), probably very far from making it first class citizen
  - Project Mu - has STM integrated, Microsoft Secured Core PC makes it requirement
  - Ron Minnich: [Let's move SMM out of firmware and into the kernel](https://www.youtube.com/watch?v=6GEaw4msq6g)
* Topic was discussed on:
  - [BSides Portland: ABC to XYZ of Writing System Management Mode (SMM) Drivers](https://youtu.be/BQajtsy6kp0)
  - [Dasharo Dev vPub: Overview of the Intel SMI Transfer Monitor on Dasharo Firmware](https://youtu.be/3PmOcjQX-9Y)
* SMM (TEE?) by definition should not give direct access to user, but it needs
to communicate platform security state to user. Is there place for it in Linux
kernel?

<!--

TODO: do a picture on which SMM/TEE gap would be presented

-->

---

# All your hardware belong to us

- The growth of hardware and firmware components like AMD PSP features, Intel
PPAM and ME features, or MS Pluton and how effectively those block building
trustworthy systems by open-source community.
- In parallel, creating an ecosystem in which we cannot leverage the full
potential of hardware and firmware in our machines.
- On one side this is attack vector which we cannot do anything about on the
other sides our hardware no longer belong to us, if anyone is surprised with
that fact.
* Topic was discussed on:
  - [BlackHat: Breaking Firmware Trust From Pre-EFI: Exploiting Early Boot Phases](https://youtu.be/Z81s7UIiwmI)
  - [OffensiveCon22: UEFI Firmware Vulnerabilities](https://youtu.be/F2HbtmGPE6Y)

<!--

TODO: make a diagram, probably from lecture about peripheral processors in modern computers

MS Pluton:
- chip-to-cloud technology
- Services
	- hardware-based root of trust,
	- secure identity,
	- secure attestation,
	- crypto,
- Potential relation in WLS?
- Looks like full potential can be leveraged only by MS Windows,
	- do we own our computers?
	- this is not first tech which cannot be leveraged by open ecosystem,
- AMD SMM attestation
	- AMD attestation and SMM supervisor is the same problem category as Intel PPAM
- Intel PPAM
	- It looks like Kirk Brannock (Intel author of PPAM whitepaper) has retired, along with our request for more documentation.  We need to:
		- Get a message to Intel to ask for PPAM docs through official channels.  Also via Vincent Z and anyone else we know there.
		- Reverse engineer PPAM calls made by Microsoft Windows launch.  What's the best way to go about doing this: boot Windows on a bare-metal device with debug UEFI device that is logging all interactions with boot loader / OS?  boot Windows 11 on QEMU?
	- 3mdeb should have NDA access to the Intel documentation for PPAM.
		- You can give that document name and relevant page numbers to Brian.
		- PPAM docs are available to 3mdeb.
		- We can tell Intel that we want to get support into upstream Linux as part of LSL and that it will be much slower and more expensive to do it later.  Public docs are needed to support the OSS work.
		- What you need is PPAM User Guide (doc 604868). It is for PPAM 1.1 and describes the VMCALL interface between MLE and PPAM.

-->

---

# Root of Trust

* Plans for defeating the lack of consistent assessment, implementation, and
provisioning of Root of Trust on very different hardware configurations through
Caliptra, DICE, SPDM, and more, and what impact it may have on the OS.
* Some SPDM relates patches slowly land in Linux.
* Topic was discussed on:
  - [UEFI Forum: Using SPDM in UEFI for Device Attestation](https://youtu.be/RJHd3Mqk4Uw)
  - [OCP: OCP Attestation using SPDM and DICE](https://youtu.be/qO2BrMZZy2Y)
  - [OCP: TPM Transport Security: Defeating Active Interposers with DICE](https://youtu.be/DKfbkOTYzOU)
  - [OCP: And Update on Caliptra](https://youtu.be/DKfbkOTYzOU)
  - [SNIA: TCG DICE & DMTF SPDM Binding Overview](https://youtu.be/fxp7UHFaBLs)

<!--

- OCP Caliptra
	- ASpeed 2700 will have support for Caliptra
	- how attestation of such RoT would look like?
- Device boot (SPDM) attestation and NVMe over Fabric
	- Device authentication in EDKII and how Linux kernel can use that information for any purposes
	- https://lkml.org/lkml/2024/6/8/175
	- https://lkml.org/lkml/2023/1/26/305
	- This can be related to Caliptra because there is plan to expose API which would serve as a signing oracle for SPDM responder in SOC, as well as authentication to a discrete TPM devices.

-->

---

# What we can do better with DRTM for AMD

<v-clicks>

  - Lessons learned from 11-th series of making 20+ YO security tech for Intel
  CPUs a first-class citizen in Linux kernel.
  - Make sure to consider platform-specific challenges and architectural
  alignment (Intel vs AMD, ARM inclusion).
  - Consider KASLR and IOMMU configuration impact and document it in front.
  - Plan for all entry points (32/64 bit, legacy/UEFI).
  - Check various compilers from beginning.
  - Avoid tight coupling to specific hardware behaviors (e.g. TPM access).

</v-clicks>

Anything missing?
How to avoid miscommunication in ABI changes?

---
layout: cover
background: /intro.png
class: text-center

---

# Q&A

<!--

TODO: how conferences link with above topics?

- Common git repo for hosting Boot-firmware
- Accelerating Linux Kernel Boot-Up for Large Multi-Core Systems
- Leveraging and managing SBAT revocation mechanism on distribution level
- Using U-boot as a UEFI payload
- no more bootloader: please use the kernel instead
- [LVFS HSI] OF != UEFI
- Measured Boot, Secure Attestation & co, with systemd
- [AMD TrenchBoot] Secure Launch - DRTM solution on Arm platforms


-->
