class: center, middle, intro

# TrenchBoot AEM - Project Status

### FOSDEM 2025

### Open Source Firmware, BMC and Bootloader devroom

## Maciej Pijanowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
src="/remark-templates/3mdeb-presentation-template/images/maciej_pijanowski.png"
width="220px" style="margin-top:-50px"> ]

.center[Maciej Pijanowski] .center[_Engineering Manager_] .right-column50[

- Over 8 years in 3mdeb
- Open-source contributor
- Interested in:
  + build systems (e.g., Yocto)
  + embedded, OSS, OSF
  + firmware/OS security

]

.left-column50[

- <a href="https://twitter.com/macpijan">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/x.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @macpijan
    </a>
- <a href="mailto:maciej.pijanowski@3mdeb.com">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/email.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      maciej.pijanowski@3mdeb.com
    </a>
- <a href="https://www.linkedin.com/in/maciej-pijanowski-9868ab120">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/maciej-pijanowski-9868ab120
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

- Intro
- TrenchBoot
- Qubes OS AEM
- Finished/ongoing tasks and associated changes
- Future work
- Progress with automation and upstreaming
- Q&A

---

# Intro

TrenchBoot is an open source project led by 3mdeb, Apertus Solutions, and
Oracle. It aims at the security and integrity of the boot process by leveraging
advanced silicon security features, like Intel Trusted Execution Technology
(TXT) and AMD Secure Startup. It integrates with open source projects like
GRUB2, Xen, and Linux, to perform a measured launch of the operating system
software, also called Dynamic Root of Trust for Measurement (DRTM).

The presentation will provide an overview of the project's current status,
emphasizing the key developments during the last year such as progress towards
upstreaming patches in Linux and GRUB, as well as bringing UEFI support for Xen
boot path.

???

In this presentation I want to focus on presenting the current plan, status, and
problems.

I will just briefly explain what AEM and TB is. It was explained in more detail
on previous conferences and summits.

---

# Previous presentations

The project has already been discussed during past Qubes OS summits and on
FOSDEM:
- https://archive.fosdem.org/2024/schedule/event/fosdem-2024-3724-trenchboot-project-status-update/
- https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s
- https://www.youtube.com/live/xo2BVTn7ohs?si=BVUnKccSe-saRf2b&t=5441

.center.image-60[![](/img/tb_aem_2022_yt.png)]

???

These presentations can provide more details or background.

---

# Qubes OS Anti Evil Maid

- A set of software packages and utilities
  + https://github.com/QubesOS/qubes-antievilmaid
- The goal is to protect against
  [Evil Maid attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)
- Requires **TPM**
- Requires **Dynamic Root of Trust for Measurement (DRTM)**
  + technology from a silicon vendor
  + needs to be present in hardware and supported by the firmware

.center.image-75[![](/img/tb_aem_attack.png)]

.footnote[https://blog.f-secure.com/de/evil-maid-attacken-wenn-die-putzfrau-den-pc-hackt/]

???

AEM attack is ...

In the current QubesOS implementation it requires TPM and DRTM technology.

---

# How TrenchBoot maps onto DRTM process

.center.image-95[![](/img/tb_drtm.png)]

For Qubes OS AEM:
- The Gap: GRUB
- DCE-Preamble: Secure Launch commands of GRUB
- [DL Event]: `SENTER` instruction on Intel, `SKINIT` on AMD
- [DCE]: [ACM] on Intel, [SKL] on AMD
- [DLME]: Xen

[DL Event]: https://trenchboot.org/theory/Glossary/#dynamic-launch-event-dle
[SKL]: https://github.com/TrenchBoot/secure-kernel-loader/
[DCE]: https://trenchboot.org/theory/Glossary/#dynamic-configuration-environment-dce
[DLME]: https://trenchboot.org/theory/Glossary/#dynamic-launch-measured-environment-dlme
[ACM]: https://trenchboot.org/theory/Glossary/#authenticated-code-module-acm

.footnote[https://trustedcomputinggroup.org/wp-content/uploads/TCG_D-RTM_Architecture_v1-0_Published_06172013.pdf]

???

Pre-gap: from power on to starting GRUB and picking AEM boot.
The gap: GRUB initiates DRTM.
Post-gap: Xen runs securely after a successful DRTM.

---

# Finished since FOSDEM 2024

TrenchBoot as AEM v1 (legacy) / Phase 4 (the final phase):<br/>
AMD support for Qubes OS AEM with TrenchBoot:
- https://github.com/TrenchBoot/trenchboot-issues/milestone/4
- https://blog.3mdeb.com/2024/2024-04-11-aem_phase4/

<br/>
Actualized TrenchBoot's website to be more up to date with current development:
- https://trenchboot.org/

<br/><br/>
.center[.image-30[![](/img/logo/nlnet.svg)]]

---

# TrenchBoot as AEM v1 (legacy) / Phase 4

Changes:
- Support for legacy boot on AMD (uses [SKL] as [DCE])
- GRUB now tries out all DCEs found in `/boot` and uses the last valid one, so
  users don't need to pick the right DCE manually
- Introduced an RPM-repository for distribution of AEM packages<br/>
  https://dl.3mdeb.com/rpm/QubesOS/r4.2/current/dom0/fc37/

<br/>

Tested on:
- Asus KGPE-D16 with TPM 1.2
- HP Thin Client t630 with TPM 2.0

---

# In progress as of now

TrenchBoot for AMD platform in Linux kernel:
- Done<br/>
  https://github.com/TrenchBoot/trenchboot-issues/milestone/5<br/>
  https://github.com/TrenchBoot/trenchboot-issues/milestone/6<br/>
  https://github.com/TrenchBoot/trenchboot-issues/milestone/7<br/>
  https://github.com/TrenchBoot/trenchboot-issues/milestone/8
- In progress<br/>
  https://github.com/TrenchBoot/trenchboot-issues/milestone/9<br/>
  https://github.com/TrenchBoot/trenchboot-issues/milestone/10

<br/>
TrenchBoot as AEM v2 (UEFI) / Phase 1: UEFI boot mode with DRTM<br/>
https://github.com/TrenchBoot/trenchboot-issues/milestone/11

---

# TrenchBoot for AMD platform in Linux kernel

- Old and by now outdated AMD support for Linux was updated to use SLRT

- Includes changes for DRTM Service developed by Oracle<br/>
  https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/user-guides/58453.pdf

- Revived meta-trenchboot Yocto distribution that can be used for testing and
  demonstration<br/>
  https://github.com/zarhus/meta-trenchboot

???

DRTM services makes DRTM on AMD more secure by closing the gap with unprotected
memory in DCE during which security could be compromised.  This comes at a cost
of somewhat increased complexity.  Which DRTM version is used depends on PSP
firmware version as well as on CPU family.

---

# TrenchBoot as AEM v2 (UEFI) / Phase 1

Making AEM work on UEFI installations of Qubes OS:

- CPUs:
  + Intel (TXT)
  + AMD (SKINIT)

- TPM:
  + 1.2
  + 2.0

- Both versions of SKINIT:
  + original (since 2005)
  + with DRTM service (since 2024)

---

# Future work

TrenchBoot as AEM v2 (UEFI) / Phase 2: Compatibility Test Suite<br/>
https://github.com/TrenchBoot/trenchboot-issues/milestone/12

<br/>
TrenchBoot as AEM v2 (UEFI) / Phase 3: Upstream<br/>
https://github.com/TrenchBoot/trenchboot-issues/milestone/13

---

# Testing automation

[openQA](https://open.qa/) is employed for testing AEM:
- Installation and configuration of Qubes OS
- Installation of TrenchBoot packages and setting up AEM
- Verification of AEM's functionality (e.g., correct secret or TOTP code)

.center.image-90[![](/img/tb_aem_openqa_testing.png)]

???

TOTP code is extracted from a screenshot via OCR to check against expected
value.

---

# Upstreaming

- Linux Intel series in still in progress
  + went from v7 to v12 in a year
  + https://lore.kernel.org/lkml/20241219194216.152839-1-ross.philipson@oracle.com/
- Upstreaming of AMD changes depends on upstreaming Intel changes that contain
  common part of the code
- Small portion of generic GRUB patches landed, but the rest depends on Linux
  upstreaming

.center[.image-20[![](/img/Tux.png)] &nbsp;&nbsp;&nbsp;&nbsp; .image-30[![](/img/logo/grub.png)]]

---

# More Dasharo synergies

.center[ .image-45[![](/img/dasharo-logo-3.png)] ]

.center[ .image-20[![optiplex]] .image-40[![nv4x]] .image-30[![vp4600]] ]

[optiplex]: /img/tb_aem_optiplex.png
[nv4x]: /img/NV4x-front-1.png
[vp4600]: /img/VP4600.jpg

???

We already use some engineering release of Dasharo on Dell OptiPlex on one of
the development platforms.

With UEFI support in place, more Dasharo targets can take advantage of the
TrenchBoot AEM.

Because of full(\*) control over firmware, we can ensure TXT compatibility and
fix problems in that area.

---

# Early Adopters

.center[.image-80[![](/img/tb_aem_early_adopter.drawio.svg)]]

???

TBD: call to action?

- becoming one
- reporting feedback

---

# Contact us

We are open to cooperate and discuss

- <a href="mailto:contact@3mdeb.com">
    <img src="/remark-templates/3mdeb-presentation-template/images/email.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      contact@3mdeb.com
  </a>

- <a href="https://www.facebook.com/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/facebook.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      facebook.com/3mdeb
  </a>

- <a href="https://twitter.com/3mdeb_com">
    <img src="/remark-templates/3mdeb-presentation-template/images/x.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @3mdeb_com
  </a>

- <a href="https://www.linkedin.com/company/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/company/3mdeb
    </a>

- <a href="https://3mdeb.com">https://3mdeb.com</a>

- <a href="https://calendly.com/3mdeb/consulting-remote-meeting">Book a call</a>

- <a href="https://newsletter.3mdeb.com/subscription/PW6XnCeK6">
    Sign up for the newsletter
  </a>

Feel free to contact us if you believe we can help you in any way.

---

<br>
<br>
<br>

## .center[Q&A]
