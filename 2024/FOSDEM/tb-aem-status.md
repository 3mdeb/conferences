class: center, middle, intro

# TrenchBoot AEM Project Status

### FOSDEM 2024

### Open Source Firmware, BMC and Bootloader devroom

## Maciej Pijanowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
  src="/remark-templates/3mdeb-presentation-template/images/maciej_pijanowski.png"
  width="220px" style="margin-top:-50px">
]

.center[Maciej Pijanowski]
.center[_Engineering Manager_]
.right-column50[
* over 7 years in 3mdeb
* Open-source contributor
* Interested in:
    - build systems (e.g., Yocto)
    - embedded, OSS, OSF
    - firmware/OS security
]

.left-column50[
* <a href="https://twitter.com/macpijan">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @macpijan
    </a>
* <a href="mailto:maciej.pijanowski@3mdeb.com">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/email.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      maciej.pijanowski@3mdeb.com
    </a>
* <a href="https://www.linkedin.com/in/maciej-pijanowski-9868ab120">
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
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)]
]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

* coreboot licensed service providers since 2016 and leadership participants
* UEFI Adopters since 2018
* Yocto Participants and Embedded Linux experts since 2019
* Official consultants for Linux Foundation fwupd/LVFS project since 2020
* IBM OpenPOWER Foundation members since 2020

---

# Agenda

* Intro
* Qubes OS AEM
* Current state
* Further plans
* Dasharo integrations (?)
* Q&A

---

# Intro

* Today we will current state since Oct 2023 and further plans
* Qubes OS AEM project already discussed in past Qubes OS summits
    - https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s
    - https://www.youtube.com/live/xo2BVTn7ohs?si=BVUnKccSe-saRf2b&t=5441

.center.image-70[![](/img/tb_aem_2022_yt.png)]

???

In this presentation I want to focus on presenting the current plan, status,
and problems.

I will just briefly explain what AEM and TB is. It was already explained in the
last year's summit

---

# Qubes OS Anti Evil Maid

* A set of software packages and utilities
    - https://github.com/QubesOS/qubes-antievilmaid
* The goal to protect against
  [Evil Maid attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)
* Requires **TPM**
* Requires **Dynamic Root of Trust for Measurement (DRTM)**
    - technology from silicon vendor
    - needs to be present in hardware and supported by the firmware

.center.image-80[![](/img/tb_aem_attack.png)]

.footnote[https://blog.f-secure.com/de/evil-maid-attacken-wenn-die-putzfrau-den-pc-hackt/]

???

AEM attack is ...

In the current QubesOS implementation it reuiqres TPM and DRTM technology

---

# Current status

* Phase 2 released
* Phase 3 released
* Phase 4 started

---

# Phase 2 - released

* Qubes OS AEM on Intel boards with TPM 2.0
* GH release
    - GRUB: https://github.com/TrenchBoot/grub/releases/tag/aem_v0.2
    - Xen: https://github.com/TrenchBoot/xen/releases/tag/aem_v0.2
    - Qubes OS AEM: https://github.com/TrenchBoot/qubes-antievilmaid/releases/tag/aem_v0.2
* Blog post
    - https://blog.3mdeb.com/2023/2023-09-27-aem_phase2/

---

# Phase 3 - released

* Update to recent TrenchBoot boot protocol
* GH release
    - GRUB: https://github.com/TrenchBoot/grub/releases/tag/aem_v0.3
    - Xen: https://github.com/TrenchBoot/xen/releases/tag/aem_v0.3
    - Qubes OS AEM: https://github.com/TrenchBoot/qubes-antievilmaid/releases/tag/aem_v0.3
* Upstreaming into Qubes OS still in progress
    - Xen
        + https://github.com/QubesOS/qubes-vmm-xen/pull/160
    - GRUB
        + https://github.com/QubesOS/qubes-grub2/pull/13
* Blog post
    - https://blog.3mdeb.com/2024/2024-01-12-aem_phase3/

---

# Phase 4 - started

* Qubes OS AEM on AMD boards with TPM 1.2 and TPM 2.0
* HW selection
    - TBD

---

# Further plans

* Phase 5
* Testing and documentation improvements
* Upstream TrenchBoot AMD support to the Linux kernel

---

# Phase 5

* Phase 5
    - UEFI support
        + so far we focused on legacy boot
        + both Intel and AMD
        + both TPM 1.2 and TPM 2.0

---

# Testing and documentation improvements

TBD

---

# Upstream TrenchBoot AMD support to the Linux kernel

* Intel series
    - TBD link
* nlnet grant
    - https://nlnet.nl/project/TrenchBoot-AMD/

TBD

---

# Contact us

We are open to cooperate and discuss

* <a href="mailto:contact@3mdeb.com">
    <img src="/remark-templates/3mdeb-presentation-template/images/email.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      contact@3mdeb.com
  </a>

* <a href="https://www.facebook.com/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/facebook.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      facebook.com/3mdeb
  </a>

* <a href="https://twitter.com/3mdeb_com">
    <img src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @3mdeb_com
  </a>

* <a href="https://www.linkedin.com/company/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/company/3mdeb
    </a>

* <a href="https://3mdeb.com">https://3mdeb.com</a>

* <a href="https://calendly.com/3mdeb/consulting-remote-meeting">Book a call</a>

* <a href="https://newsletter.3mdeb.com/subscription/PW6XnCeK6">
    Sign up for the newsletter
  </a>

Feel free to contact us if you believe we can help you in any way. We are
always open to cooperate and discuss.

---

<br>
<br>
<br>

## .center[Q&A]
