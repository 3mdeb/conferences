---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## Can It Run TrenchBoot?

### Maciej Pijanowski

### QubesOS Summit 2025 

---

# whoami

---

# Past presentations

- Recommend to watch the past presentations about AEM:
  + [Qubes OS Summit 2022](https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s)
  + [Qubes OS Summit 2023](https://www.youtube.com/watch?v=xo2BVTn7ohs&t=5441s)
  + [Qubes OS Summit 2024](https://youtu.be/5ieNhbLLTIU?si=_E_k6ct9LV0iXYeN)

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_aem_2022_yt.png" width="600">
  </center>
</div>

---

# Qubes OS Anti Evil Maid

- A set of software packages and utilities
  + https://github.com/QubesOS/qubes-antievilmaid
- The goal is to protect against [Evil Maid
  attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/qubes_aem_prompt.png" width="580">
  </center>
</div>

<!---
When everything is provisioned and working properly, this is the screen one is
presented when unlocking the disk (after giving a proper TPM SRK password).
-->

---

# Qubes OS Anti Evil Maid

- Requires **TPM**
  + fTPM - integrated into CPU/chipset
  + dTPM - additional chip connected via LPC/I2C/SPI bus
- Requires **Dynamic Root of Trust for Measurement (DRTM)**
  + technology from silicon vendor
  + needs to be present in hardware and supported by the firmware
  + creates a new, dynamic Root of Trust beyond the static one established by
    the firmware

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/qubes_aem_pcrs.png" width="580">
  </center>
</div>

<!--
One of the advantages of DRTM is that the PCRs that are normally locked in TPM
are available after DRTM command is issued. It serves as an additional
protection and policy input to seal secrets.
-->

---

# TrenchBoot

- A framework that allows individuals and projects to build security engines to
perform launch integrity actions for their systems.
- Delivers us the DRTM support for our system (Qubes OS)

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/trenchboot_logo.png" width="400">
  </center>
</div>

[https://trenchboot.org/](https://trenchboot.org/)

<!--
We already know what AEM is, so we need to talk about second part of our
presentation - TB
-->

# TPM

TPM
You need a Trusted Platform Module (TPM) of some sort. It may come as a discrete module attached to the board (dTPM), or as a firmware TPM (fTPM). Usually it's configurable in BIOS settings and enabled by default. In case of no TPM being detected by the tools, check the BIOS settings.

# DRTM

## AMD

SINIT
basically all AMD out there have it

There are no prerequisites to check.
[AMD Zen](https://en.wikipedia.org/wiki/Zen_(microarchitecture)) or newer CPUs
will likely not work in the current stage of development. Refer to
[this issue](https://github.com/TrenchBoot/trenchboot-issues/issues/66) for
further progress on this.



OpenQA:

AEM setup: https://openqa.3mdeb.com/tests/416
AEM first run: https://openqa.3mdeb.com/tests/417
AEM second run: https://openqa.3mdeb.com/tests/418


# meta-trenchboot

# trenchboot-hcl

- about the project
- some results

---

# Accomplishments - 2023-2024

* Recap of vision and challenges presented last year.
* We added 50% to Qubes OS Certified Hardware (from 6 to 9)
  - although we have to admit that some old certified hardware is no longer
available,
* Qubes HCL statistics: 1055 (+61)
* Released Qubes OS 4.2 and three subsequent point releases
* Greatly improved updates experience
* Several UX improvements and new GUI tools - including new Qubes Global
  Config, more to come
* fwupd integration installed by default
* Community projects:
  - Automated configurability extended thanks to community contribution from Ben
  Grande in form of [qusal](https://github.com/ben-grande/qusal) based on
  previous unman work.

<!--

Qubes HCL snapshot date 18/09/2024

-->
---

# Accomplishments - 2023-2024

* Event organization improved:
  - A lot external talks in CfP, we had to reject some.
* Coming soon:
  - UEFI Secure Boot integration - more about that in tomorrow's talk.
    + TL;DR we are not there yet, but we are close. safeboot approach is still
  alive.
  - TrenchBoot AEM - we have some exciting news and demo for you.
  - Certified Hardware with Intel Boot Guard and UEFI Capsule Update coming in
  following months.
  - As mentioned last year SMI Transfer Monitor was integrated for Qubes OS
  Certified Hardware MSI PRO Z690-A by Brian Delgado.
    + code is PoC, but it was presented at [vPub 0xB](https://youtu.be/3PmOcjQX-9Y)
    + the challenge would be to make Xen and dom0 aware of that,

<!-- markdownlint-disable MD022 MD003 -->
---
transition: fade
---
<!-- markdownlint-enable MD022 MD003 -->

# Accomplishments - 2022-2023

<center><img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2023_stats.png" width="600"></center>

---

# Accomplishments - 2023-2024

<center><img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2024_stats.png" width="600"></center>

---

<div style="display: flex; flex-wrap: wrap; justify-content: center;
  align-items: center;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/secure_boot_main1.png"
    alt="Image 1" style="max-width: 35%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/secure_boot_main3.png"
    alt="Image 2" style="max-width: 35%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/secure_boot_main4.png"
    alt="Image 3" style="max-width: 35%; height: auto; margin: 10px;">
</div>

<!--

- PoC was created during Qubes OS Summit 2023 Hackathon

-->

---

# Vision and challenges - 2024-2025

* Continue growth of number of Qubes OS Certified Hardware
  - Dell OptiPlex 7010/9010 with AEM
  - Odroid H4?
  - Novacustom Laptops
* Finalize Qubes AEM support for Intel
  - Legacy BIOS (through SeaBIOS) is close to be completed.
  - UEFI is planned and founded.
* Finalize Qubes AEM for AMD
  - Waiting for release of documentation by AMD
  - If it would not happen early we have to rely on existing documentation and
    will adjust after that.
* UEFI Secure Boot have to become first-class citizen in Qubes OS.
* Qubes Security Report - road to OSS security leadership.
* More in Marek's talk dedicated to Qubes OS Project plans.

<!--

Not much changed since last year.

-->

---

# What is our lineup this year?

<br>

* ## September 20th: Conference Day 1 and Afterparty

<br>

* ## September 21th: Conference Day 2

<br>

* ## September 22th: Hackathon

<br>

---

# Day 1 agenda

### 10:00-10:25

#### **_Welcome to Qubes OS Summit 2024 Day 1_** - Piotr (3mdeb), Marek (ITL)

### 10:30-11:00

#### **_Qubes OS development status update_** - Marek (ITL)

### 11:10-11:30

#### **_Qubes OS GUI Changes and Future Perspectives_** - Marta (ITL)

### 11:40-12:10

#### **_Enhancing OS Awareness of Hardware Security Capabilities in Qubes OS_** - Piotr (3mdeb)

### 12:15-13:00

#### **_Passwordless encrypted Qubes? Exploring some concepts_** - nestire (Nitrokey)

### 13:00-14:30

#### **_Lunch_**

---

# Day 1 agenda

### 14:30-15:00

#### **_How to architect your Qubes OS with SaltStack_** - Ben (FOSS Maintainer)

### 15:10-15:40

#### **_FlashKeeper: where SpiSpy meets Stateless Laptop jaded dreams: A retrofit plan first_** - Thierry (Heads Maintainer)

### 15:50-16:20

#### **_Anti Evil Maid status and future plans_** - Michał (3mdeb)

### 16:30-17:00

#### **_Rolling out Qubes_** - unman (Qubes OS Maintainer)

### 17:10-17:40

#### **_Update on Qubes Air_** - Marek&Frédéric (ITL/Qubes Team)

### 17:50-18:00

#### **_Closing Notes_** - Piotr (3mdeb)

### 19:30+

#### **_Afterparty_**

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---

## Details on

### https://cfp.3mdeb.com/qubes-os-summit-2024/

### https://vpub.dasharo.com/e/16/qubes-os-summit-2024#schedule

---

<div style="display: flex; flex-wrap: wrap; justify-content: center;
  align-items: center;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/sudblock.jpg" style="max-width:
    50%; height: auto; margin: 10px;">
</div>

<center><img src="/@fs/repo/public/2024/QubesOSsummit/sudblock_address.png"
  style="max-width: 100%"></center>

<div class="absolute left-30px bottom-30px">
  <small>Photo by Maciej Klimiuk</small>
</div>

---

<center><img src="/@fs/repo/public/2024/QubesOSsummit/qoss_format.png"
  style="max-width: 70%"></center>

<center>

https://vpub.dasharo.com

</center>

* Respect Code of Conduct.
* Please follow Safety and Health protocols and respect others.
* Talks are streamed and recorded and will be published on Youtube.
* Drinks and sweets are free.
* Matrix `#qubes-summit:matrix.org` will be used for communication during event.
* In case of any issues please contact with organizers.

---

# Merchandise

<div style="display: flex; flex-wrap: wrap; justify-content: center;
  align-items: center;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_front.png"
    style="max-width: 35%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_back.png"
    style="max-width: 35%">
</div>

* Paid and free merchandise available (at location and in 3mdeb Shop).
* There are also partners selling their merchandise.

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Q&A
