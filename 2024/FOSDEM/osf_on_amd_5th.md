class: center, middle, intro

# Open Source Firmware status on AMD platforms 2023 - 4th edition

### FOSDEM'23 - Open Source Firmware, BMC and Bootloader devroom

## Michał Żygowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img src="/img/miczyg.png" width="200px" style="margin-top:-50px">]
.center[Michał Żygowski]
.center[_Firmware Engineer_]
.right-column50[
- Braswell SoC, PC Engines and Protectli maintainer in coreboot
- OpenPOWER System Software Technical Workgroup chair
- dedicated to the open-source firmware since 2017
- interested in advanced hardware and firmware security features
]
.left-column50[
- <a href="https://twitter.com/_miczyg_"><img
  src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
  width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @\_miczyg\_</a>

- <a href="mailto:michal.zygowski@3mdeb.com"><img
  src="/remark-templates/3mdeb-presentation-template/images/email.png"
  width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  michal.zygowski@3mdeb.com</a>

- <a href="https://www.linkedin.com/in/miczyg"><img
  src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
  width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
  linkedin.com/in/miczyg</a>

- <a href="https://www.facebook.com/miczyg1395"><img
src="/remark-templates/3mdeb-presentation-template/images/facebook.png"
width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
facebook.com/miczyg1395</a> ]

---

# Who we are ?

.center[.image-15[![](/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/lvfs.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)]]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

- coreboot licensed service providers since 2016 and leadership participants
- UEFI Adopters since 2018
- Yocto Participants and Embedded Linux experts since 2019
- Official consultants for Linux Foundation fwupd/LVFS project since 2020
- IBM OpenPOWER Foundation members since 2020

---

# AMD microarchitetcures in coreboot

- **Puma** - Steppe Eagle core architecture, AMD 2nd Gen G series embedded SoCs
  (PC Engines apu2)
- **Bulldozer** - Interlagos core architecture, AMD Opteron 6200 series (server),
  KGPE-D16
- **Piledriver** - Abu Dhabi core architecture, AMD Opteron 6300 series (server),
  KGPE-D16
- **Picasso** - Zen+ core architecture, Ryzen 3000 APU series with RX Vega
  (desktop & laptop), AMD Family 17h, Model 18h
- **Cezanne** - Zen3 core architecture, Ryzen 5000 series (desktop & laptop),
  AMD Family 19h, Model 50h
- **Mendocino** - Zen2 core architecture, Ryzen 7000-series Mobile CPUs with
  RDNA2 graphics, formerly **Sabrina**, AMD Family 17h, Model A0h
- **Phoenix** - Zen4 core architecture, Ryzen 7000-series Mobile CPUs
  with RDNA3 graphics, formerly **Morgana**, AMD Family 19h, Models 70h-7Fh?
- **Glinda** - very new and very little information about it, also probably a
  temporary codename

---

# AMD coreboot status - last year

- family14, Trinity and Kabini removed from the master branch and moved to 4.18
  branch
- [boards
  affected](https://doc.coreboot.org/releases/coreboot-4.19-relnotes.html#removed-mainboards):
    * PC Engines apu1
    * MSI MS-7721 (FM2-A75MA-E35)
    * Lenovo AMD G505s
    * HP Pavilion m6 1035dx
    * ASUS F2A85-M (LE, PRO), A88XM-E and AM1I-A
    * ASRock E350M1 and IMB-A180
    * and others...
- **Since then there were no AMD board removals yet**

---

# AMD coreboot status - last year

- Starlabs could build coreboot firmware for their AMD laptops thanks to the
  publication of Cezanne FSP to
  [amd_blobs](https://github.com/coreboot/amd_blobs/tree/master/cezanne)
  repository in September 2022
    * [mb/starlabs/cezanne: Add Cezanne Byte Mk
      I](https://review.coreboot.org/c/coreboot/+/69404/)
    * [mb/starlabs/cezanne: Add Cezanne StarBook Mk VI
      variant](https://review.coreboot.org/c/coreboot/+/68338/)
    * **NO UPDATE TO THE PATCHES**
- AMD Mendocino and Phoenix still in development with the former being in more
  advanced state, FSP not published yet
    * **FSP published for Mendocino, but not for Phoenix**
- The FSP publication interval is quite long (1.5 a year between Picasso FSP
  and Cezanne FSP release to public, and 1.25 a year after Cezanne APU release
  FSP has been published)
    * **Interval between Cezanne and Mendocino is only 5 months**
    * **Mendocino is Zen2 while Cezanne is Zen3, so maybe not so big update**
    * **Mendocino has been released to the market at the end of 2022**

???

Cezanne is newer core architecture, but Mendocino is a newer processor in
terms of release date.

---

# AMD coreboot status - now

- [patches covering KGPE-D16 bootblock support are out
  there](https://review.coreboot.org/q/topic:kgpe-d16-bootblock)
    * they have been abandoned because of lack of activity
    * KGPE-D16 needs some love and attention, which, unfortunately, 3mdeb
      can't humbly provide right now without any support from community
- Marty Plummer ("hanetzer") is working on adapting AMD FSP for
  Picasso/Cezanne to work on a non-Chromebook device ASRock x370 Killer SLI
    * Join [Dasharo Matrix Space](https://matrix.to/#/#dasharo:matrix.org) or
      [Dasharo vPubs](https://vpub.dasharo.com/o/1) to know more

.center[.image-20[![](/img/ryzen.jpg)]]

.center.footnote[
[Ryzen photo](https://www.flickr.com/photos/130561288@N04/51371399197)
by Fritzchens Fritz, CC0 1.0 Universal Public Domain Dedication
]

???

hanetzer is putting some serous efforts here using SerialICE to trace the
hardware accesses in FSP and PSP. Observes hangs around accesses to PSP and
SMU.

- PSP binaries: Picasso's work, but Cezanne (and maybe others) do not work
  with anything but soldered memory and ChromeOS type devices
- FSP binaries: hardcoded CPUID checks for the mobile variants, which need
  patching or a wholly different compilation parameters.

---

# AMD server status - last year vs now

.center[.image-30[![](/img/EpycProcessor.jpg)]]

.center.footnote[
[AMD EPYC photo](https://upload.wikimedia.org/wikipedia/commons/7/7d/EpycProcessor.jpg)
by Raysonho @ Open Grid Scheduler / Grid Engine, CC0, via Wikimedia Commons
]

.left-column50[

### Early 2023

- Some new initiative from Oxide on OSF for AMD Milan (EPYC 7002 series)
  server platform presented at [OSFC
  2022](https://www.osfc.io/2022/talks/i-have-come-to-bury-the-bios-not-to-open-it-the-need-for-holistic-systems/)
- Nothing new on official OSF support on servers from AMD
]

.right-column50[

### Now

- New approach to open-source firmware on AMD server - OpenSIL
- Porting AGESA to AMD FSP and maintaining it was too costly
- OpenSIL announced on [OCP Regional Summit 2023
  Prague](https://www.youtube.com/watch?v=q_y6Y1JTq0I)
]

---

# AMD server status - OpenSIL

- OpenSIL - open-source Silicon Initialization Library
    * Scalable with any host firmware interface/framework
    * Proof of Concept code for Genoa-based (AMD EPYC 9004 processors)
      reference board Onyx available on
      [GitHub](https://github.com/openSIL/openSIL)
- [coreboot source also available and merged to upstream
  repository](https://review.coreboot.org/q/topic:%22amd_genoa_opensil%22)
- UEFI EDK2-based PoC code also available on GitHub:
    * [opensil-uefi-interface](https://github.com/openSIL/opensil-uefi-interface)
    * [EDK2 Platforms](https://github.com/openSIL/EDKII-Platform)
- More about OpenSIL:
    * [OCP Global Summit 2023](https://www.youtube.com/watch?v=nSVKKMkcIPE)
    * [OSFC 2023](https://vimeo.com/878219919)

---

# AMD OpenSIL future

.left-column55[
.center[.image-90[![](/img/opensil_github.png)]]
]

.right-column45[
- The OpenSIL is constantly developed and improved by AMD and partners
- Planned to go **production in 2026** with the 6th generation of AMD EPYC
  processors
- AMD plans to cover the **client segment with OpenSIL support** too (Ryzen
  desktop and mobile processors)
]

---

# PC Engines platforms - yet another chance?

- Last year we announced the end of PC Engines' sponsorship of open-source
  firmware
- We tried to gather community interested in the open-source firmware for apu2
  board and launch a subscription model, however the response was very little
  and we didn't succeed
- This year we see another chance to revive the project under
  [Dasharo](https://dasharo.com) brand

.center.image-40[![](/img/pcengines_logo.png)]
.center[
.image-30[![](/img/apu4d4.png)]
.image-20[![](/img/dasharo-sygnet.png)]
]

???

---

# Dasharo

- In [Dasharo](https://dasharo.com) we carefully select hardware platforms,
  which are quite popular
    * Of course most such boards will be community-driven effort and the work
    would be done in free time thus the releases may not be that frequent
- Value offered by Dasharo:
    * [high quality documentation](https://docs.dasharo.com) explaining:
      initial deployment, firmware update and recovery
    * hardware and software tools available
    * active and helpful community on Matrix
    * binary releases
    * transparent validation
- Sign up to [Dasharo
  newsletter](https://newsletter.3mdeb.com/subscription/wwL90UkXP) to get up
  to date information about supported platforms and the their status

???

Briefly explain what Dasharo is

---

# Dasharo

- We have also introduced subscription model for selected platforms to help
  gather funds for development
    * in return the releases for subscribers are more frequent and available
      with subscriber's credentials
- There are also beta testers programs for selected platform, like [NovaCustom
  laptops](https://novacustom.com/forum/d/15-call-for-beta-testers)
    * Beta testers are given access to pre-release firmware to assist with
      testing features and reporting bugs

---

## .center[Q&A]

---
class: center, middle, intro

# Thank you
