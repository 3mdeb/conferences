class: center, middle, intro

# Anti Evil Maid status and future plans

<img src="/img/qubes_os_summit_24_logo.png" width="400px" >

## Michał Żygowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px">

---

# `whoami`

.center[
<img src="/remark-templates/3mdeb-presentation-template/images/miczyg.png"
 width="180px" style="margin-top:-60px">
]
.center[Michał Żygowski] .center[_Senior Firmware Engineer_]
.right-column50[

- Braswell SoC, PC Engines, Protectli, MSI PRO Z690-A/Z790-P maintainer in
  coreboot
- Engaged in Open Source Firmware since 2017
- Interested in advanced hardware and firmware security features
- OST2 instructor
- TrenchBoot developer

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
  facebook.com/miczyg1395</a>

]

---

# Past presentations

- Recommend to watch the past presentations about AEM:
  + [Qubes OS Summit 2022](https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s)
  + [Qubes OS Summit 2023](https://www.youtube.com/watch?v=xo2BVTn7ohs&t=5441s)

.center.image-90[![](/img/tb_aem_2022_yt.png)]

---

# Qubes OS Anti Evil Maid

- A set of software packages and utilities
  + https://github.com/QubesOS/qubes-antievilmaid
- The goal is to protect against [Evil Maid
  attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)

.center.image-80[![](/img/qubes_aem_prompt.png)]

???

When everything is provisioned and working properly, this is the screen one is
presented when unlocking the disk (after giving a proper TPM SRK password).

---

# Qubes OS Anti Evil Maid

- Requires **TPM**
  + Present almost on any board, at least in a form of firmware TPM
    (integrated into the chipset or CPU, but AMD fTPMs do not work with DRTM!)
- Requires **Dynamic Root of Trust for Measurement (DRTM)**
  + technology from silicon vendor
  + needs to be present in hardware and supported by the firmware
  + creates a new, dynamic Root of Trust beyond the static one established by
    the firmware

.center.image-99[![](/img/qubes_aem_pcrs.png)]

???

One of the advantages of DRTM is that the PCRs that are normally locked in TPM
are available after DRTM command is issued. It serves as an additional
protection and policy input to seal secrets.

---

# TrenchBoot

.center[ **TrenchBoot is a framework that allows individuals and projects to
build security engines to perform launch integrity actions for their
systems.** ]

### .center[TrenchBoot delivers us the DRTM support for our system (Qubes OS)]

.center.image-40[![](/img/trenchboot_logo.png)]

### .center[https://trenchboot.org/]

???

We already know what AEM is, so we need to talk about second part of our
presentation - TB

---

# Project Status - January 2024

.center[<img src="/img/tb_aem_milestone_3_2024.png" width="90%" style="margin-top:-40px">]

.center[.image-50[![](/img/logo/nlnet.svg)]]

.center[https://github.com/TrenchBoot/trenchboot-issues/milestone/3]

???

The project is split into phases, where each phase builds on the previous one
and enables more usage scenarios.

- Phase 3
  + Update to the newest TrenchBoot boot protocol
  + https://github.com/TrenchBoot/trenchboot-issues/milestone/3

---

# Project Status - May 2024

.center[<img src="/img/tb_aem_milestone_4_2024.png" width="90%" style="margin-top:-40px">]
.center[https://github.com/TrenchBoot/trenchboot-issues/milestone/4]

???

- Phase 4
  + AMD support for Qubes OS AEM with TrenchBoot, TPM 1.2 and TPM2.0
  + https://github.com/TrenchBoot/trenchboot-issues/milestone/4
  + DRTM Event log parsing for AMD SKINIT with SKL

---

# AEM packages simplified

**Building and installing QubesOS packages**

- It is not trivial to ramp-up non-QubesOS developers
- Building GRUB/Xen with custom TrenchBoot changes
  + Creating patches from TrenchBoot changes
  + Applying them on top of the QubesOS GRUB/Xen patches
- AEM/TrenchBoot packages need to be installed into dom0
  + Copying to dom0 is hard
  + https://www.qubes-os.org/doc/how-to-copy-from-dom0/#copying-to-dom0

**NEW: Simplified releasing, publishing and deployment of the packages**

- [Building of the packages happens in
  CI](https://github.com/TrenchBoot/.github)
- For tags, a GitHub release is created with code snippets how to download
  RPMs (links to artifacts with wget/curl)
- RPMs are published in a custom [package repository for Qubes
  R4.2](https://dl.3mdeb.com/rpm/QubesOS/r4.2/current/dom0/fc37) to avoid
  copying to dom0 as explained in the [blog
  post](https://blog.3mdeb.com/2024/2024-04-11-aem_phase4/#installation)

???

Maybe for many of you here this does not look like a challenge, but it is really
not that trivial to ramp-up non-QubesOS users to into QubesOS development.

It is an additional challenge that AEM/TB packages must be installed into dom0.

Downsides: the CI still uses builder v1. For Qubes R4.3, we will have to
switch to builder v2.

---

# What now?

- TrenchBoot was mostly tested on some random hardware, typically with
  proprietary firmware
- On [Xen Summit
  2024](https://www.youtube.com/watch?v=RVK52BCM-ZM&list=PLQMQQsKgvLntZiKoELFs22Mtk-tBNNOMJ&index=14)
  I have shown a demo of running TrenchBoot on Dasharo open-source firmware
  supported Protectli VP4670
  + Good for development and testing (bless the serial port!)
  + But this is more like a network appliance hardware.
  + AEM shines best on devices which are susceptible to actual evil maid
    attacks, i.e. laptops

## .center[Goal:]

## .center[Qubes-certified laptop with Anti Evil Maid support!]

---

# AEM on NovaCustom NV4x AlderLake laptop

.center.image-35[![](/img/NV4x-front-1.png)]

.left-column50[
Pros:
- Relatively modern (~3 years old)
- Already Qubes-certified
- Open-source firmware supported
- DRTM capable
]
.right-column50[
Cons:
- Not in production anymore
- Running out of stock
- DRTM/Intel TXT is tightly-coupled with Boot Guard manifests (new since 11th
  generation Tiger Lake processors)
]

???

Despite Protectli VP4670 being 10th generation Intel Core processor, jumping
with TXT support onto 12th generation Intel Core processor did not work out of
the box. Architectural changes to Boot Guard and TXT caused additional effort
on the firmware side (partially on Xen/GRUB side too).

---

# Reporting AEM status in Qubes OS

.center[<img src="/img/qubes_sec_report_aem.png" width="70%" style="margin-top:-40px">]

.footnote[
- Using SeaBIOS because UEFI boot mode is not yet supported
- Blooper: SeaBIOS is not a certified variant of firmware &#128512;
]

???

Extended Qubes OS security report to indicate DRTM capability and AEM service
status.

DRTM capability is tricky, because Xen lies to Dom0 about Intel SMX capability
(hides it). Also the command necessary to determine the Intel TXT supported
chipset causes VM exit, so detection has to be done on Xen side. Made by
printing the SMX capability and TXT chipset capability to `xl dmesg`.

AEM status is just the anti-evil-maid-unseal.service status from systemd. It
says active only when the anti-evil-maid-unseal.service finished with code 0
(SUCCESS). Otherwise it may be a yellow (installed, inactive, configured but
failed) or red indicator (not supported or not installed).

---

# Qubes-certified devices with Dasharo

.center.image-100[![](/img/qubes_certified_dasharo.png)]

---

# Main issues

- [Lack of UEFI
  support](https://github.com/TrenchBoot/trenchboot-issues/milestone/11)
  &#128542;
  + We miss all the setup features and other value added stuff in Dasharo
    payload
  + Most Dasharo releases support UEFI only and that configuration is tested
  + Although the firmware is much more lightweight with SeaBIOS (SeaBIOS is
    roughly 60KB vs 2MB TianoCore UEFI Payload).
- [When Secure Launch with TrenchBoot DRTM is used, the qubes/VMs requiring
  some devices to be passed through don't
  start](https://github.com/TrenchBoot/xen/issues/18)
  + This defeats the purpose of using Qubes OS...
  + Probably some state clean-up after DRTM is missing in Xen, which was done
    previously by tboot
- [Xen boots terribly slowly with Secure
  Launch](https://github.com/TrenchBoot/xen/issues/16)
  + Probably for the same reason as above issue

---

# Demo time

### .center[Evil maid incoming... Securing the system...]

.center.image-70[![](/img/qubes_trenchboot_aem/evil_maid.png)]

---

# Plans for the future

- Resolve the current outstanding issues and make the system usable
- Offer Qubes-certified devices with pre-configured AEM and supported firmware
- &#128557; **UEFI support** &#128557; (most, if not all of recent, Dasharo
  releases are UEFI variants)
- Develop and test support for the newest NovaCustom Meteor Lake-based laptops
  V560TU, which are Qubes-certified already &#128525;

.center.image-40[![](/img/NovaCustom-V54-Series-1.png)]

???

Get things working finally! Preferably on the newest hardware that is
available.

Getting the Intel TXT working on Meteor Lake causes yet more effort, because
Intel changed the BootGuard/Intel TXT architecture slightly again.

We would also like to upstream everything finally, however Linux patches are
constantly pushed back (patch v11 and still counting). Thus the interface is
still not set in stone.

---

# Support us

Sign up for a paid tech preview to help us with development and testing.

<!-- Placeholder for QR code -->

---

<br>
<br>
<br>

## .center[Q&A]
