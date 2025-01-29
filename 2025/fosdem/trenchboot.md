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

# Kudos

- Most TrenchBoot development on 3mdeb side and support with this presentation
  + Krystian Hebel
  + Sergii Dmytruk

---

# Agenda

- Intro
- TrenchBoot for AMD
- TrenchBoot as QubesOS AEM
- Future work
- Q&A

---

# Intro

- Main areas of 3mdeb's involvement in TrenchBoot right now
  + implementation of "the original" DRTM path for AMD
    - booting Linux
  + practical application of TrenchBoot in QubesOS
    - booting Xen
    - https://github.com/QubesOS/qubes-antievilmaid

.center.image-50[![](/img/trenchboot_logo.png)]

???

---

# TrenchBoot for AMD

### Done

- Old and by now outdated AMD support for Linux was updated to use SLRT
- Includes changes for DRTM Service developed by Oracle
  + https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/user-guides/58453.pdf
- Revived meta-trenchboot Yocto distribution that can be used for testing and
  demonstration
  + https://github.com/zarhus/meta-trenchboot
- Refreshed TrenchBoot's website to be more up to date with current development:
  + https://trenchboot.org/

???

DRTM services makes DRTM on AMD more secure by closing the gap with unprotected
memory in DCE during which security could be compromised.  This comes at a cost
of somewhat increased complexity.  Which DRTM version is used depends on PSP
firmware version as well as on CPU family.

---

# TrenchBoot for AMD

### In progress - upstream process

- Linux Intel series in still in progress
  + as shown in Oracle's part
- Upstreaming of AMD changes depends on upstreaming Intel changes that contain
  common part of the code
- Small portion of generic GRUB patches landed, but the rest depends on Linux
  upstreaming

.center[.image-20[![](/img/Tux.png)] &nbsp;&nbsp;&nbsp;&nbsp; .image-30[![](/img/logo/grub.png)]]

---

# TrenchBoot as QubesOS AEM

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

 How TrenchBoot maps onto DRTM process

Pre-gap: from power on to starting GRUB and picking AEM boot.
The gap: GRUB initiates DRTM.
Post-gap: Xen runs securely after a successful DRTM.

https://trenchboot.org/theory/Glossary

---

# TrenchBoot as QubesOS AEM

### Done

- Support for legacy boot on AMD (uses [SKL] as [DCE])
- GRUB now tries out all DCEs found in `/boot` and uses the last valid one, so
  users don't need to pick the right DCE manually
- Introduced an RPM-repository for distribution of AEM packages
  + https://dl.3mdeb.com/rpm/QubesOS/r4.2/current/dom0/fc37/

- Tested on:
  + Asus KGPE-D16 with TPM 1.2
  + HP Thin Client t630 with TPM 2.0

---

# TrenchBoot as QubesOS AEM

### In progress

- Making AEM work on UEFI installations of Qubes OS
- CPUs
  + Intel (TXT)
  + AMD (SKINIT)
- TPMs
  + 1.2
  + 2.0
- Both versions of AMD SKINIT
  + original (since 2005)
  + with DRTM service (since 2024)

---

# TrenchBoot as QubesOS AEM

- [openQA](https://open.qa/) is employed for testing AEM:
  + Installation and configuration of Qubes OS
  + Installation of TrenchBoot packages and setting up AEM
  + Verification of AEM's functionality (e.g., correct secret or TOTP code)

.center.image-90[![](/img/tb_aem_openqa_testing.png)]

???

TOTP code is extracted from a screenshot via OCR to check against expected
value.

---

# Future work

- TrenchBoot Compatibility Test Suite
  + https://github.com/TrenchBoot/trenchboot-issues/milestone/12

- TrenchBoot as QubesOS AEM - Upstream
  + https://github.com/TrenchBoot/trenchboot-issues/milestone/13

---

# Links

- Presentations
  + https://archive.fosdem.org/2024/schedule/event/fosdem-2024-3724-trenchboot-project-status-update/
  + https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s
  + https://www.youtube.com/live/xo2BVTn7ohs?si=BVUnKccSe-saRf2b&t=5441
- Blog
  + https://blog.3mdeb.com/2024/2024-04-11-aem_phase4/
- GitHub milestones
  + https://github.com/TrenchBoot/trenchboot-issues/milestones

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

- <a href="https://cloud.3mdeb.com/index.php/apps/calendar/appointment/yiqxCTTdioPN">
    Book a call
   </a>

- <a href="https://newsletter.3mdeb.com/subscription/PW6XnCeK6">
    Sign up for the newsletter
  </a>

Feel free to contact us if you believe we can help you in any way.

---

<br>
<br>
<br>

## .center[Q&A]
