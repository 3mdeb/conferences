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

# AMD coreboot status

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

# AMD coreboot status

- Starlabs could build coreboot firmware for their AMD laptops thanks to the
  publication of Cezanne FSP to
  [amd_blobs](https://github.com/coreboot/amd_blobs/tree/master/cezanne)
  repository in September 2022
    * [mb/starlabs/cezanne: Add Cezanne Byte Mk
      I](https://review.coreboot.org/c/coreboot/+/69404/)
    * [mb/starlabs/cezanne: Add Cezanne StarBook Mk VI
      variant](https://review.coreboot.org/c/coreboot/+/68338/)
    * **There is no update to the patches unfortunately**
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

# AMD coreboot status

- [patches covering KGPE-D16 bootblock support are out
  there](https://review.coreboot.org/q/topic:kgpe-d16-bootblock)
    * they have been abandoned because of lack of activity
    * KGPE-D16 needs some love and attention, which, unfortunately, 3mdeb
      can't humbly provide right now without any support from community
- Marty Plummer ("hanetzer") is working on adapting Picasso/Cezanne AMD FSP for
  on a non-Chromebook device ASRock x370 Killer SLI
    * [Dasharo vPub 0x8 recording](https://www.youtube.com/watch?v=LYPH2Oc6xqU&list=PLuISieMwVBpKevqcC9qEav9ZnCTwkZVW2&index=8&t=393s)
    * [Dasharo vPub 0x9 recording](https://www.youtube.com/watch?v=gAZw0fTKdYg)
    * Join [Dasharo Matrix Space](https://matrix.to/#/#dasharo:matrix.org) or
      [Dasharo vPubs](https://vpub.dasharo.com/o/1) to know more

.center[.image-20[![](/img/ryzen.jpg)]]

.center.footnote[
[Ryzen photo](https://www.flickr.com/photos/130561288@N04/51371399197)
by Fritzchens Fritz, CC0 1.0 Universal Public Domain Dedication
]

???

We tried to contact Immunefi to redirect funds; redirection was needed because
the whole plan fell apart when it was realized upstreaming was not feasible.
Unfortunately, we haven't gotten any response from them so far, so we assume
that some resources are stalled. We also get medium interest from testers;
some bugs were reported (maybe labeled to Dasharo issues about that), but no
developers activity from the community. Also, some configurations and bugs
were exotic enough. We could not invest in reproduction. We contacted NLNet,
and they said this is too old hardware to support. We also contacted Vikings,
offering the Dasharo Revenue Sharing Program, but we didn't get a response.

Also, most of the community seems to be interested in free support of that
platform, which means someone else would have to have serious business
interests. The last path we could consider is selling SPI chips with Dasharo
for KGPE-D16, but it is unlikely to render volumes, which could seriously
impact development.

The platform is still on Dasharo Roadmap but most likely would be removed.

hanetzer is putting some serous efforts here using SerialICE to trace the
hardware accesses in FSP and PSP. Observes hangs around accesses to PSP and
SMU.

- PSP binaries: Picasso's work, but Cezanne (and maybe others) do not work
  with anything but soldered memory and ChromeOS type devices
- FSP binaries: hardcoded CPUID checks for the mobile variants, which need
  patching or a wholly different compilation parameters.
- AMD OpenSIL would be the way forward here

---

# AMD server status

.left-column45[
.center[.image-60[![](/img/EpycProcessor.jpg)]]

- PoC for Genoa-based (AMD EPYC 9004) reference board Onyx on
  [GitHub](https://github.com/openSIL/openSIL)
- [coreboot source also available and merged to upstream
  repository]((https://review.coreboot.org/q/topic:%22amd_genoa_opensil%22)
- UEFI EDK2-based PoC code also available on GitHub:
    * [opensil-uefi-interface](https://github.com/openSIL/opensil-uefi-interface)
    * [EDK2 Platforms](https://github.com/openSIL/EDKII-Platform)
]

.right-column55[
- In the beginning of 2023 no news on official OSF support on servers from AMD
- Porting AGESA to AMD FSP and maintaining it was too costly
- New approach to open-source firmware on AMD server - OpenSIL
- OpenSIL announced on [OCP Regional Summit 2023
  Prague](https://www.youtube.com/watch?v=q_y6Y1JTq0I) (April 2023)
- OpenSIL - open-source Silicon Initialization Library
    * Scalable with any host firmware interface/framework
- More about OpenSIL:
    * [OCP Global Summit 2023](https://www.youtube.com/watch?v=nSVKKMkcIPE)
    * [OSFC 2023](https://vimeo.com/878219919)

]

.center.footnote[
[AMD EPYC photo](https://upload.wikimedia.org/wikipedia/commons/7/7d/EpycProcessor.jpg)
by Raysonho @ Open Grid Scheduler / Grid Engine, CC0, via Wikimedia Commons
]

---

# AMD OpenSIL coreboot

.left-column55[
- Building is quite trivial
    * Build toolchain: **`make crossgcc-i386 && make crossgcc-x64`**
    * Select mainboard **`AMD/Onyx_poc`** with **`make menuconfig`**
    * Run **`make`** to build
<br>
]

.right-column45[
.center[.image-80[![](/img/coreboot_logo.png)]]
]

- coreboot takes around 1MB in total (decompressed)
    * Although blobs' size is notable:
    ```console
    Name                           Offset     Type           Size   Comp
    ...
    apu/amdfw                      00x1ffc0    amdfw         4317184 none
    ```
- Not all blobs are present though:
    ```console
      ** WARNING **
    coreboot has been built without an APCB.
    This image will not boot.
    ```

???

OpenSIL requires meson to build, so it is impossible to use coreboot-sdk
docker container. Latest version from 2023-11-24 does not have meson yet.
Thus building cross toolchain.

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

# TrenchBoot DRTM on AMD platforms

.center[.image-50[![](/img/trenchboot_logo.png)]]

- Early attempts on SuperMicro M11SDV in 2020 on [Qubes OS Summit](https://www.youtube.com/watch?v=rM0vRi6qABE)
    * Only legacy boot mode, no UEFI support for booting Xen
- This years the effort will be continued to cover UEFI boot mode for both
  Linux and Xen
- More details on the **TrenchBoot status presentation at 16:20 CET (UTC+1)**
  in this room
    * Make sure you do not miss it!

---

# Dasharo

.center.image-99[![](/img/des_value_prop.png)]

.center.footnote[Sign up to [Dasharo
newsletter](https://newsletter.3mdeb.com/subscription/wwL90UkXP) to get up to
date information about supported platforms and the their status.]

???

- We have also introduced subscription model for selected platforms to help
  gather funds for development
    * in return the releases for subscribers are more frequent and available
      with subscriber's credentials
- There are also beta testers programs for selected platform, like [NovaCustom
  laptops](https://novacustom.com/forum/d/15-call-for-beta-testers)
    * Beta testers are given access to pre-release firmware to assist with
      testing features and reporting bugs

- Dasharo would like to be a central point for open-source firmware
  development for customers and embedded devices. Open-source firmware for
  mere mortals and species with reasonable budget? The goal is to create
  sustainable ecosystem by leveraging programs like Dasharo Revenue Sharing
  (worth to mention briefly how it works) and Dasharo Supporting Partner.

- Special Dasharo Updates.
- Exclusive newsletter.
- Access to Dasharo Primer Support invite-only Matrix channel.
- Direct access to Dasharo Team with ability to influence features roadmap.
- Formerly known as Dasharo Supporters Entrance
- Sustainable long-term development and maintenance of open-source firmware for
  your hardware.
- Meaningful release notes - no more "improved performance" or "fix for #4242"
  in release notes
- links to publicly available continuously improving documentation
- links to fixed issues
- clear description of know issues
- basic SBOM information, which we plan to extend with US executive order
- compliant supply chain information
- signed binaries with clear information about update procedure
- access to detailed test results spreadsheet
- and more

---

# Bonus

.center[AMD open-sourced the AMD PSP code for Secure Encrypted Virtualization (SEV)]

.center[[AMD PSP SEV FW on GitHub](https://github.com/amd/AMD-ASPFW)]

.center.image-80[![](/img/amd_psp_sev_github.png)]

---

## .center[Q&A]

---
class: center, middle, intro

# Thank you
