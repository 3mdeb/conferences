---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## Welcome to Qubes OS Summit 2025 Day 1

### Piotr Król and Marek Marczykowski-Górecki

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /@fs/repo/public/2024/QubesOSsummit/qoss_welcome.png
---

---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Platinum Sponsors

---

<div style="display: flex; justify-content: center; align-items: center;
  margin-top:150px;">
  <center>
    <img src="/@fs/repo/public/2024/QubesOSsummit/fopf_logo.png" width="1200">
  </center>
</div>

<!--

Freedom of the Press Foundation’s generous contribution and commitment to
defending press freedom and digital privacy by building secure communication
tools aligns with Qubes OS Summit goals of coordinating Qubes OS and associated
projects development, like SecureDrop, with community.

-->

---

<div style="display: flex; justify-content: center; align-items: center;
  margin-top:100px;">
<center><img src="/@fs/repo/public/2024/QubesOSsummit/mullvad_logo.png" width="1200"></center>
</div>

<!--

Mullvad’s support for transparency and privacy enhancing technologies is known
in our community. What is more important you can support those who support us
by choosing their products in that way your getting great VPN with possibility
for anonymous or cryptocurrency payment, which is well recognized by
independent reviewers.

-->

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Silver Sponsors

---

<div style="display: flex; justify-content: center; align-items: center;
  height: 40vh;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/novacustom_logo.png"
    style="max-width: 50%; height: auto;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/nitrokey_logo.png"
    style="max-width: 500%; height: auto;">
</div>

<!--

NovaCustom’s deliver Qubes OS Certified Hardware maximizing transparency and
trustworthiness of our computing.

Nitrokey’s secure our digital life with USB FIDO-compliance tokens as well as
hardware with Heads firmware.

You can always thank them by recommending them and their products.

-->

---

# Supporting Contributor

* ## StarApps Ltd

We are grateful for the support from StarApps Ltd., company which use and rely
on Qubes OS and support FOSS philosophy.

---

<img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2024_logo.png">

<div style="display: flex; flex-wrap: wrap; justify-content: center;
  align-items: center;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2023_logo.png" alt="Image
    1" style="max-width: 50%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2022_logo.png" alt="Image
    2" style="max-width: 50%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2021_logo.png" alt="Image
    3" style="max-width: 35%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2020_logo.jpeg" alt="Image
    4" style="max-width: 30%; height: auto; margin: 10px;">
  <img src="/@fs/repo/public/2024/QubesOSsummit/qubes_2019_logo.png" alt="Image
    5" style="max-width: 25%; height: auto; margin: 10px;">
</div>

<!--

History

-->

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
