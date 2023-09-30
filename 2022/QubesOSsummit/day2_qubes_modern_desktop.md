class: center, middle, intro

# Qubes OS on modern Alder Lake desktop

### Qubes OS Summit 2022

## Michał Żygowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Agenda

* Introduction
* Qubes OS on desktop. Why?
* Desktop and open-source firmware?
* Dasharo
* Qubes OS certification requirements
* Present and future of desktop support in OSF
* Demo
* Q&A

---

# `whoami`

.center[<img src="/img/miczyg.png" width="180px" style="margin-top:-60px">]
.center[Michał Żygowski]
.center[_Firmware Engineer_]
.right-column50[
- Braswell SoC, PC Engines and Protectli maintainer in coreboot
- OpenPOWER System Software Technical Workgroup chair
- 5 years in Open Source Firmware
- interested in advanced hardware and firmware security features
- OST2 instructor
- TrenchBoot developer
]

.left-column50[
- <a href="https://twitter.com/_miczyg_"><img src="/remark-templates/3mdeb-presentation-template/images/twitter.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @\_miczyg\_</a>

- <a href="mailto:michal.zygowski@3mdeb.com"><img src="/remark-templates/3mdeb-presentation-template/images/email.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> michal.zygowski@3mdeb.com</a>

- <a href="https://www.linkedin.com/in/miczyg"><img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> linkedin.com/in/miczyg</a>

- <a href="https://www.facebook.com/miczyg1395"><img src="/remark-templates/3mdeb-presentation-template/images/facebook.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> facebook.com/miczyg1395</a>
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

# Qubes OS on desktop - why?

* Qubes OS is magnificent in terms of security
* Sometimes with security come sacrifices
* Qubes OS heavily depends on virtualization which has a non-zero performance
  penalty
  * This can be noticeable on laptops (especially the older ones like Lenovo
    x230)
* Keeping the old machines well supported by fully open-source firmware, like
  coreboot for Lenovo Thinkpad x230 is great, but at some point we have to move
  forward

---

# Qubes OS on desktop - why?

* The main disadvantage of desktops is almost zero mobility, while laptops are
  all-in-one devices ready to use, but...
* Desktops outperform mobile devices
* Are they less secure?
  * Not necessarily ;)

.left-column50[
.image-75[![](/img/qubes_modern_desktop/desktop_lock.jpg)]
]
.right-column50[
.image-90[![](/img/qubes_modern_desktop/laptop_lock.jpg)]
]

???

Recent times weren't particularly favorable for travels. Having a solid
workstation at home became a need.

---

# Desktop and open-source firmware?

* Answer is: **YES**
* For a long time coreboot had no port of a modern desktop (except some single
  node mini-servers which could serve as workstation)
* Latest supported machine is 9th Gen Intel Core device
* Big elaboration about the state on [reddit](https://www.reddit.com/r/intel/comments/subaro/how_many_people_are_interesed_in_seeing_coreboot/)
* The time has come to break this status quo

---

# Dasharo

* An opportunity to support most recent 12th Generation Intel Core Alder Lake
  based desktop with open-source firmware appeared
* MSI PRO Z690-A has been selected as a new port target to Dasharo
* Now what is Dasharo you may ask?

.center.image-60[![](/img/qubes_modern_desktop/msi_pro_z690a.png)]

---

# Dasharo

.center[.image-30[![](remark-templates/dasharo-presentation-template/images/dasharo-sygnet.svg)]]

.center[
### Dasharo is open source firmware distribution, we prefer clean and simple code, long term maintenance, privacy-respecting implementation, liberty for the owners, and trustworthiness for all.
]

---

# Dasharo

* Dasharo compatible with MSI PRO Z690-A (WIFI) DDR4
* Most recent release v1.0.0 with basic support completed
* More on [docs.dasharo.com](https://docs.dasharo.com/variants/msi_z690/overview/) (including binaries and documentation)
* How you make it possible? Just like this:

.center.image-80[![](/img/qubes_modern_desktop/spiderweb_in_lab.jpg)]

---

# Dasharo

What we currently support:

* Booting Linux distros and Windows10/11
* Booting Qubes OS :) (apparently MSI firmware has some issues)
* UEFI compliant boot mode
* iPXE
* Boot from USB, NVMe, SATA
* PS/2 keyboard/mouse support
* UEFI Secure Boot
* TPM and measured boot

---

# Dasharo

.center.image-40[![](/img/qubes_modern_desktop/finding-nemo-seagull.gif)]

.left-column50[
What we WANT to support:

* Overclocking
* Firmware setup password
* ME disabling
* Firmware flashing with USB with FLASHBIOS button
* Power state after power fail
* And many many more...
]
.right-column50[
### But what we would really like is to meet Qubes certification requirements.
]

---

# Qubes Certification requirements

* In June this year Demi Marie Obenour started a new thread on
  [qubes-devel](https://groups.google.com/g/qubes-devel/c/08uSf2i-FTo/m/ii9DpjQ-AgAJ?pli=1)
  mailing list called "Future certification requirements"
* The thread describes 7 security aspects of the hardware and firmware that
  must be met to be eligible for certification
* These mostly touch the following:
  * PCI devices state
  * DMA
  * USB and Network controllers
  * and PCI Option ROMs

---

# Qubes Certification requirements

* We plan a new release of Dasharo v1.1.0 compatible with MSI PRO Z690-A DDR4
  WIFI
* One of the new features addresses one of the future certification
  requirements:

  ```txt
  3. The firmware’s network stack (if any) must be disabled by default.

  Rationale: This is a large attack surface that is almost never useful
  for desktops or laptops, except in corporate environments.
  ```

* Other features included:
  * Codebase rebased on recent coreboot tree with various Alder Lake support
    improvements and fixes
  * [Bugfix for Ventoy delay bug](https://github.com/Dasharo/dasharo-issues/issues/160)
  * Bugfix for incorrectly parsed PCI aperture above 4G
  * Implement network boot enable/disable option

---

# Present and future of desktop support in OSF

* In the new release we also planned to cover the performance differences
  compared to MSI firmware
* However these settings are SKU dependent and their change may be dangerous on
  different CPU:
  * Custom AC/DC loadline for voltage regulator
  * Custom power limits
  * Custom IccMax (current limit)
* Dasharo provides Intel recommended defaults for these
* In the future it will be possible to tune these parameters when overclocking
  setup options become available

---

# Present and future of desktop support in OSF

Cinebench R23 results after applying same settings for i5-12600K CPU:

.pure-table.pure-table-bordered.pure-table-striped[
| Firmware | Multi Thread | Single Thread |
|:---------|:------------:|:-------------:|
| MSI 1.70 | 17020        | 1852          |
| Dasharo v1.1.0, Intel defaults | 15438 | 1731 |
| Dasharo v1.1.0, AC/DC loadline 0.8 mOhm | 16760 | 1634 |
| Dasharo v1.1.0, AC/DC loadline 0.8 mOhm, IccMax 250A | 16722 | 1714 |
| Dasharo v1.1.0, AC/DC loadline 0.8 mOhm, <br>IccMax 250A,<br> Power Limits 241W | 16712 | 1621 |
| Dasharo v1.1.0, all modifications | 16702 | 1640 |
]

* All modifications mean: AC/DC loadline 0.8 mOhm, IccMax 250A, Power Limits
  288W, Energy Efficient Turbo Disabled, Cache frequency Limit equal 49
* Abnormal Single Thread score are caused by irregular CPU affinity (sometimes
  the load is generated on Efficient core)

---

# Present and future of desktop support in OSF

* We would like to continue efforts with supporting the desktops with
  open-source firmware
* Raptor Lake 13th Gen Intel Core CPU can be supported on the ported MSI PRO
  Z690-A (WIFI) DDR4
* Z690 chipset allows full overclocking capabilities of Intel system, so can
  generate the most performance
* We see much interest in the desktop segment, hopefully Qubes OS project also
  has some demand on such machines :)

---

# Demo

## .center[DEMO time!]

---

# Summary

* Securing the desktop from firmware side is possible thanks to open-source
  firmware
* Securing the desktop from software side is possible thanks to Qubes OS
  project
* What do you need more?
* More Hz on the CPU cores? Sure go ahead.
  * But this machine already boots Qubes OS insanely fast!
  * Actually typing disk password takes longer than loading whole system :)

---

## .center[Q&A]

---

class: center, middle, intro

# Thank you!
