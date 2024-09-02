class: center, middle, intro

# TrenchBoot AEM - Project Status

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
* Q&A

---

# Intro

* Today we will cover current state since Oct 2023 and further plans
* Project has been already discussed during past Qubes OS summits
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

.center.image-75[![](/img/tb_aem_attack.png)]

.footnote[https://blog.f-secure.com/de/evil-maid-attacken-wenn-die-putzfrau-den-pc-hackt/]

???

Evil Maid attack is ...

In the current QubesOS implementation it requires TPM and DRTM technology

---

class: center, middle, intro

# Current state

---

# Current status

* Phase 2 released
    - https://github.com/TrenchBoot/trenchboot-issues/milestone/2
* Phase 3 released
    - https://github.com/TrenchBoot/trenchboot-issues/milestone/3
* Phase 4 started
    - https://github.com/TrenchBoot/trenchboot-issues/milestone/4

.center.image-80[![](/img/tb_aem_milestones_23_2024.png)]

.center[.image-30[![](/img/logo/nlnet.svg)]]

???

TBD: show graphic roadmap instead?

---

# Phase 2 - released

* Qubes OS AEM on Intel boards with TPM 2.0
* GH release
    - GRUB: https://github.com/TrenchBoot/grub/releases/tag/aem_v0.2
    - Xen: https://github.com/TrenchBoot/xen/releases/tag/aem_v0.2
    - Qubes OS AEM: https://github.com/TrenchBoot/qubes-antievilmaid/releases/tag/aem_v0.2
* Blog post
    - https://blog.3mdeb.com/2023/2023-09-27-aem_phase2/

.center.image-50[![](/img/hp_elitedesk_800_g2.jpg)]

???

TBD: photo of supported HW?

---

# Phase 3 - released

* Update to recent TrenchBoot boot protocol
* GH release
    - GRUB: https://github.com/TrenchBoot/grub/releases/tag/aem_v0.3
    - Xen: https://github.com/TrenchBoot/xen/releases/tag/aem_v0.3
    - Qubes OS AEM: https://github.com/TrenchBoot/qubes-antievilmaid/releases/tag/aem_v0.3
* Upstreaming into Qubes OS still in progress
    - Xen: https://github.com/QubesOS/qubes-vmm-xen/pull/160
    - GRUB: https://github.com/QubesOS/qubes-grub2/pull/13
* Blog post
    - https://blog.3mdeb.com/2024/2024-01-12-aem_phase3/

---

# Phase 4 - started

* Qubes OS AEM on AMD boards with TPM 1.2 and TPM 2.0
* HW selection
    - Asus KGPE-D16
    - Supermicro M11SDV-4C-LN4F (QubesOS 4.2 install issue)
    - subject to change

.center.image-40[![](/img/kgpe-d16.jpeg) ![](/img/M11SDV-4C-LN4F_spec.webp)]
.footnote[QubesOS installation issue: https://github.com/QubesOS/qubes-issues/issues/8322#issuecomment-1904423204]

---

class: center, middle, intro
# Further plans

---

# Phase 5

* Phase 5
    - UEFI support
        + so far we focused on legacy boot
        + both Intel and AMD
        + both TPM 1.2 and TPM 2.0
    - Finalizing scope
    - To be presented as another GH milestone
    - Opens up wider hardware variety

.center[.image-30[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)]]

---

# Testing and documentation improvements

* Project consists of multiple moving parts
* Installation of custom packages under QubesOS can be challenging
* A lot of manual work was required
* We have started some automation effort as shown in the last status

.center.image-70[![](/img/qubes_aem_installation.png)]

---

# Testing and documentation improvements

* The goal is to move that forward
    - Run tests on hardware, not only QEMU
    - Automatically install artifacts from Github Actions

.center.image-60[![](/img/tb_aem_openqa_screen.png)]

---

# Upstream TrenchBoot AMD Linux patches

* Intel series in progress
    - v7 and counting
    - https://lore.kernel.org/lkml/20231110222751.219836-1-ross.philipson@oracle.com/
* nlnet grant for AMD equivalent
    - https://nlnet.nl/project/TrenchBoot-AMD/
* Sync with Oracle's latest work
* Will need some more time to start this effort
    - ideally if some Intel part is already merged

.center[.image-40[![](/img/logo/nlnet.svg)] .image-20[![](/img/Tux.png)]]

---

# More Dasharo synergies

.left-column50[
.center[
  .image-40[![](/img/tb_aem_optiplex.png)]
  <br>
  .image-80[![](/img/NV4x-front-1.png)]]
]
.right-column-50[
.center[
  .image-30[![](/img/VP4600.jpg)]
  <br>
  .image-35[![](/img/dasharo-logo-3.png)]]
]

???

We already use some engineering release of Dasharo on Dell OptiPlex on one of
the development platforms.

With UEFI support in place, more Dasharo targets can take advantage of the
TrenchBoot AEM.

Because of full(*) control over firmware, we can ensure TXT compatibility and
fix problems in that area.

---

# Early Adopters

.center[.image-80[![](/img/tb_aem_early_adopter.drawio.svg)]]

* Interested? Join [Matrix channel](https://matrix.to/#/#OSFW-Trenchboot:matrix.org).

???

TBD: call to action?
* becoming one
* reporting feedback

---

# Matrix channel

* TrenchBoot Matrix channel
  - https://matrix.to/#/#OSFW-Trenchboot:matrix.org

.center[.image-50[![](/img/tb_matrix_channel.png)]]

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

---

# After party

.center[.image-85[![](/img/fosdem_2024_ppub_poster.png)]]
