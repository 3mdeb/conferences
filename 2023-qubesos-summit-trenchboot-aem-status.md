class: center, middle, intro

# TrenchBoot Anti Evil Maid: Roadmap, Challenges, and Advancements

### Qubes OS Summit 2023

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
- over 7 years in 3mdeb
- Open-source contributor
- Interested in:
    + build systems (e.g., Yocto)
    + embedded, OSS, OSF
    + firmware/OS security
]

.left-column50[
- <a href="https://twitter.com/macpijan">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
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
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)]
]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

- coreboot licensed service providers since 2016 and leadership participants
- UEFI Adopters since 2018
- Yocto Participants and Embedded Linux experts since 2019
- Official consultants for Linux Foundation fwupd/LVFS project since 2020
- IBM OpenPOWER Foundation members since 2020

---

# Agenda

- AEM in QubesOS (what it is, what is the current support)
- TrenchBoot (what it is, what are the components)
- Project plan
- Challenges
- Current Status (Advancements)
- Q&A

---

# Intro

- Short overview of the AEM and TrenchBoot
- Already presented last year in the QubesOS summit
    + Michał Żygowski
    + TrenchBoot - the only AEM-way to boot Qubes OS
    + https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s

.center.image-80[![](/img/tb_aem_2022_yt.png)]

???

It was already presented last year, so no need to duplicate this.

---

# Qubes OS Anti Evil Maid

- A set of software packages and utilities
    + https://github.com/QubesOS/qubes-antievilmaid
- The goal to protect against
  [Evil Maid attacks](https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html)
- Requires **TPM**
- Requires **Dynamic Root of Trust for Measurement (DRTM)**
    + technology from silicon vendor
    + needs to be present in hardware and supported by the firmware

TBD: Some AEM / TPM image?

---

# TrenchBoot

.center[
**TrenchBoot is a framework that allows individuals and projects to build
security engines to perform launch integrity actions for their systems.**
]

.center.image-50[![](/img/trenchboot_logo.png)]

- https://trenchboot.org/

???

We already know what AEM is, so we need to talk about second part of our
presentation - TB

---

# TrenchBoot components

- Secure Kernel Loader (SKL)
    + Secure Loader for AMD Secure Startup
    + https://github.com/TrenchBoot/secure-kernel-loader
- GRUB
    + https://github.com/TrenchBoot/grub
- Xen
    + https://github.com/TrenchBoot/xen
- Linux
    + https://github.com/TrenchBoot/linux

.center[
.image-20[![](/img/logo/grub.png)]
.image-40[![](/img/logo/xen.png)]
.image-15[![](/img/logo/linux.png)]
]

???

In the context of AEM support, we are now focused on QubesOS and Intel
platforms. So we are interested in the GRUB and Xen repositories.

---

# Project Plan

.center.image-99[![](/img/tb_aem_milestones_12.png)]

.center[.image-40[![](/img/logo/nlnet.svg)]]

- https://github.com/TrenchBoot/trenchboot-issues/milestones

???

- Phase 1
    + Intel TXT and TPM1.2
    + https://github.com/TrenchBoot/trenchboot-issues/milestone/1
    + Replace existing tboot implementation with TrenchBoot equivalent
    + Support for Intel TXT and TPM 1.2
- Phase 2
    + Intel TXT and TPM2.0
    + Extend AEM scripts with TPM 2.0 support
    + https://github.com/TrenchBoot/trenchboot-issues/milestone/2

---

# Project Plan

.center.image-99[![](/img/tb_aem_milestones_34.png)]

.center[.image-40[![](/img/logo/nlnet.svg)]]

- Phase 5
    + UEFI support, scope to be precised
    + No GH milestone

???

- Phase 3
    + Update to the newest TrenchBoot boot protocol
    + https://github.com/TrenchBoot/trenchboot-issues/milestone/3
- Phase 4
    + AMD support for Qubes OS AEM with TrenchBoot
    + https://github.com/TrenchBoot/trenchboot-issues/milestone/4
- Phase 5
    + No GH milestone yet
    + This work is less precise right now
    + Not yet scheduled

---

# Project Plan

### Phase 3

- Specification
    + https://trenchboot.org/specifications/Secure_Launch/
    + Currently, it is focused on booting Linux only
    + We need to extend specification with Xen boot flow
- Adjust our GRUB patches to the latest version of boot protocol

### Phase 4

- Integrate AMD Secure Startup support in AEM
- We expect more changes to the specification to support AMD

???

A few more details on the P3 and P4 which are next in our schedule

---

# Challenges

**Building and installing QubesOS packages**

- It is not trivial to ramp-up non-QubesOS developers
- Building GRUB/Xen with custom TrenchBoot changes
    + Creating patches from TrenchBoot changes
    + Applying them on top of the QubesOS GRUB/Xen patches
- AEM/TB packages need to be installed into dom0
    + copying to dom0 is hard
    + https://www.qubes-os.org/doc/how-to-copy-from-dom0/#copying-to-dom0
- Some dev notes
    + https://gist.github.com/krystian-hebel/4359297e4ca3d9e9e3da01f9695d0e27

???

Maybe for many of you here this does not look like a challenge, but it is
really not that trivial to ramp-up non-QubesOS users to into QubesOS
development.

It is an additional challenge that AEM/TB packages must be installed into dom0.

---

# Challenges

**Reproducing OpenQA setup on VM**

- Reproducing https://openqa.qubes-os.org/ would be useful
- Testing changes from TrenchBoot repository, before pushing to QubesOS
- Added some documentation on basic OpenQA setup
    + https://github.com/QubesOS/openqa-tests-qubesos/pull/21/files
- Faced several problems, discussing with Marek in the Matrix chat
- Could not get the full QubesOS installation test (in VM) to work
- Latest problem

.code-12px[
```md
libxl_device.c:1200:device_backend_callback: Domain 4:unable to add device with path /local/domain/2/backend/vif/4/0
libxl_create.c:2000:domcreate_attach_devices: Domain 4:unable to add vif devices
libxl_device.c:1200:device_backend_callback: Domain 4:unable to remove device with path /local/domain/2/backend/vif/4/0
libxl_domain.c:1589:devices_destroy_cb: Domain 4:libxl__devices_destroy failed
```]

---

# Challenges

**Reproducing OpenQA setup on VM**

.center.image-90[![](/img/tb_aem_openqa_sys_firewall.png)]

---

# Challenges

**Reproducing OpenQA setup on real hardware**

- We have some HW in lab hooked-up with PiKVM
- Wanted to run QubesOS OpenQA test (especially AEM) on these
- Wanted to retain the functionality of the PiKVM
- QubesOS setup uses OpenQA worker installed directly on the RPI
  + The /dev/video is exposed directly to the worker
- Not trivial to make the video stream work over network
- OpenQA can accept VNC, but requires RAW or ZRLE encoding
- PiKVM exposes VNC, but supports TightJPEG and H.264 encoding

---

# Challenges

**Hardware selection for P2 (legacy boot, Intel, TPM2.0)**

- Legacy BIOS (or in reality - proper CSM support in UEFI firmware)
- TPM2.0 discrete module
- TXT supported by the CPU
- TXT supported by the PCH
  + if platform has vPro sticker, there is a good chance of compatibility
- TXT supported by the firmware
- ACM provided in the firmware
  + if not, we can still load it from GRUB
- **Physical serial port**
  + BIOS serial console redirection is a plus

---

# Challenges

**Hardware selection for P2 (legacy boot, Intel, TPM2.0)**

- Supermicro X11SSH-F
  + 8th Gen Intel server board
- Long boot time
- Poor BMC experience in general
  + Partial (or not working) Redfish implementation
  + Cannot automate BIOS actions (as changing boot devices)
- Serial (both SoL and from physical port) always goes through BMC
  + The output was malformed, we could not get reliable logs from Xen
- More details
  + https://github.com/TrenchBoot/trenchboot-issues/issues/16#issuecomment-1693399379

???

Some reports in the link below

---

# Challenges

**Hardware selection for P2 (legacy boot, Intel, TPM2.0)**

.center.image-99[![](/img/tb_aem_x11ssh_serial.png)]

???

Depending on the serial console redirection, the output was malformed in a
number of different ways, which made it very difficult to debug problems with
Xen booting.

---

# Challenges

**Hardware selection for P2 (legacy boot, Intel, TPM2.0)**

- No TXT support in AMI BIOS
- No TXT support in current Dasharo releases
  + They are UEFI-only anyway, no CSM
  + https://github.com/Dasharo/dasharo-issues/issues/94#issuecomment-1296210422
- We made some dev-build with TXT support and SeaBIOS payload
  + Xen does not boot in legacy mode
  + Not investigated further yet

.center.image-85[![](/img/tb_aem_protectli_vp4670.jpg)]

---

# Challenges

**Hardware selection for P2 (legacy boot, Intel, TPM2.0)**

- Lenovo ThinkCentre M920q (M920 Tiny)
  + i5-8500T (vPro), TPM2.0
  + Some lower models have TXT support in CPU, but not in PCH 🤯
  + No ACM in the firmware image
  + ACM exits with undocumented error: `0xC00014A1`

.center.image-60[![](/img/tb_aem_lenovo_m920q_front.png)]
.center.image-60[![](/img/tb_aem_lenovo_m920q_back.png)]

???

ACM loaded manually via GRUB

---

# Challenges

**Hardware selection for P2 (legacy boot, Intel, TPM2.0)**
- HP Elite Desk 800 G2
  + i5-6500T (vPro)
  + TPM1.2 upgradable to TPM2.0
  + (Almost) a success
  + AMT came locked and there was no way to reset password
  + No graphical output from BIOS via PiKVM (tried various EDIDs) 🙁
  + Gave up on automation, implementing with hardware on a desk

.center.image-60[![](/img/hp_elitedesk_800_g2.jpg)]

???

At this point we gave up with hardware automation and developed with the HW on
desk - thankfully it is so small

---

# Current Status

### Phase 1

- Intel, legacy boot, TPM1.2, TrenchBoot
- Released January 2023
- Blog posts
  + https://www.qubes-os.org/news/2023/01/31/trenchboot-aem-for-qubes-os/
  + https://blog.3mdeb.com/2023/2023-01-31-trenchboot-aem-for-qubesos/
- MRs still pending review to be merged in QubesOS
  + https://github.com/QubesOS/qubes-grub2/pull/13
  + https://github.com/QubesOS/qubes-vmm-xen/pull/160

---

# Current Status

### Phase 1

- Hardware used for testing
    + Dell OptiPlex 9010 SFF (Intel Ivybridge, TPM 1.2)
    + dev-build of Dasharo with TXT and SeaBios

.center.image-30[![](/img/tb_aem_optiplex.png)]

---

# Current Status

### Phase 2

- The main development is finalized
- We are working on integration and testing

---

# Current status

### Phase 2

**Extend the AEM scripts to detect TPM version on the platform**

- GitHub task
    + https://github.com/TrenchBoot/trenchboot-issues/issues/14
- Contributions
   + https://github.com/QubesOS/qubes-antievilmaid/pull/45

**Integrate TPM 2.0 software stack into Qubes OS Dom0**

- GitHub task
    + https://github.com/TrenchBoot/trenchboot-issues/issues/13
- Contributions
    + https://github.com/QubesOS/qubes-builder-rpm/pull/124
    + https://github.com/QubesOS/qubes-antievilmaid/pull/46

???

The first change was to extend the AEM scripts with TPM detection. The path for
1.2 was the same, and for 2.0 we just exit with error.

Then, we have added TPM2.0 software stack to dom0 and initrd, so the stack can
later be used by AEM scripts.

---

# Current status

### Phase 2

**Extend the AEM scripts to use appropriate software stack for TPM 2.0**
- GitHub task
    + https://github.com/TrenchBoot/trenchboot-issues/issues/15
- Contributions
    + https://github.com/QubesOS/qubes-antievilmaid/pull/43
    + https://github.com/QubesOS/qubes-antievilmaid/pull/47
    + https://github.com/QubesOS/qubes-tpm-extra/pull/7
    + https://github.com/QubesOS/qubes-trousers-changer/pull/6
    + https://github.com/QubesOS/qubes-antievilmaid/pull/42
    + https://github.com/QubesOS/openqa-tests-qubesos/pull/23

???

Finally, we have added full support for the TPM2.0 to the AEM scripts by
reorganizing the code of AEM scripts, and providing implementation of TPM2.0
functions that serve equivalent roles of the existing TPM1.2 functions.

---

# Current status

### Phase 2

**OpenQA test for AEM**

- Example run
    + https://openqa.qubes-os.org/tests/80924#
- PR
    + https://github.com/QubesOS/openqa-tests-qubesos/pull/22

---

# Current status

### Phase 2

**OpenQA test for AEM**

.center.image-85[![](/img/tb_aem_openqa_results.png)]

---

# Current status

### Phase 2

**OpenQA test for AEM**

.center.image-75[![](/img/tb_aem_openqa_screen.png)]

---

# Current status

### Phase 2

**CI for GRUB TB packages**

- https://github.com/TrenchBoot/grub/pull/9

.center.image-50[![](/img/tb_aem_grub_ci.png)]

---

# Current status

### Phase 2

**CI for Xen TB packages**

- https://github.com/TrenchBoot/xen/pull/5

.center.image-50[![](/img/tb_aem_xen_ci.png)]

---

# Next steps

- P2
    + Integration
    + Demo/blog post
    + Upstream to QubesOS repositories
- P3
    + Adjust to the most recent TB boot protocol

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
    <img src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
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

Feel free to contact us if you believe we can help you in any way. We are
always open to cooperate and discuss.

---

<br>
<br>
<br>

## .center[Q&A]
