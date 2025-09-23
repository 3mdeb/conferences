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

# $ whoami

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="/@fs/repo/img/macpijan.png" style="width: 100px; border-radius: 50%;"
    alt="Profile Picture">
  <div>
    <b style="font-size: 1.5em;">Maciej Pijanowski</b><br>
    <i style="font-size: 1.2em;">Engineering Manager</i>
  </div>
</div>

<div style="display: flex; justify-content: space-between; align-items: center;
 font-size: 1.2em;">
  <div>
    🔑 <code>A766 C895 6989 5C0B 86D5  98D0 9963 C36A AC3B 2B46</code><br>
    ✉️ <a href="mailto:maciej.pijanowski@3mdeb.com">maciej.pijanowski@3mdeb.com</a><br>
    🐦 <a href="https://x.com/macpijan">@macpijan</a><br>
    🔗 <a href="https://www.linkedin.com/in/maciej-pijanowski-9868ab120">LinkedIn</a><br>
    🌐 <a href="https://www.3mdeb.com">3mdeb.com</a><br>
    💻 <a href="https://github.com/macpijan">GitHub</a><br>
  </div>
</div>

::: footer

<div style="color: black; font-size: 0.8em; text-align: center; margin-top: 20px;">
  🌟 Reach out for collaborations or inquiries!
</div>
:::

---

# Agenda

- QubesOS AEM
- TrenchBoot
- Hardware requirements
  + DRTM
- TrenchBoot HCL
- Project status
  + Completed milestones
  + Upstream status
  + Planned work

---

# Past presentations

- Past presentations about TrenchBoot AEM status:
  + [Qubes OS Summit 2022](https://www.youtube.com/watch?v=A9GrlQsQc7Q&t=17441s)
  + [Qubes OS Summit 2023](https://www.youtube.com/watch?v=xo2BVTn7ohs&t=5441s)
  + [FOSDEM 2024](https://archive.fosdem.org/2024/schedule/event/fosdem-2024-3724-trenchboot-project-status-update/)
  + [Qubes OS Summit 2024](https://youtu.be/5ieNhbLLTIU?si=_E_k6ct9LV0iXYeN)
  + [FOSDEM 2025](https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5979-trenchboot-project-status-update/)

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_aem_2022_yt.png" width="450">
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

# TrenchBoot

A framework that allows individuals and projects to build security engines to
perform launch integrity actions for their systems.

Delivers the DRTM support for Qubes OS AEM.

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/trenchboot_logo.png" width="300">
  </center>
</div>

<br>

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <img src="/@fs/repo/img/logo/apertus.svg" width="150">
  <img src="/@fs/repo/img/logo/oracle.svg" width="150">
  <img src="/@fs/repo/img/logo/3mdeb.png" width="175">
</div>

<br>

[https://trenchboot.org/](https://trenchboot.org/)

<!--
We already know what AEM is, so we need to talk about second part of our
presentation - TB
-->

---

# Hardware requirements

- **TPM**
  + fTPM - integrated into CPU/chipset
  + dTPM - additional chip connected via LPC/I2C/SPI bus
- **Dynamic Root of Trust for Measurement (DRTM)**
  + Technology from silicon vendor
  + Needs to be present in hardware and supported by the firmware
  + Creates a new, dynamic Root of Trust beyond the static one established by
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

# DRTM

- Intel
  + Intel Trusted Execution Technology (TXT)
  + SENTER CPU instruction
- AMD
  + AMD SVM (Secure Virtual Machine)
  + SKINIT CPU instruction

---
layout: two-cols
---

# Intel TXT

- TXT supported by the CPU
  + Limited availability on client CPUs (vPro)
  + Present on most server CPUs
- TXT supported by the mainboard chipset
- TXT properly supported by the firmware
- VT, VT-d, TXT enabled in the firmware
- Platform-specific ACM provided in the firmware

Source: https://www.intel.com/content/dam/www/public/us/en/documents/guides/intel-one-stop-txt-activation-guide.pdf

::right::

<br><br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/txt_stars.jpg" width="400">
  </center>
</div>

---

# AMD SVM

- SKINIT is part of the AMD virtualization instruction set
- It is not segmented - present on basically all AMD CPUs

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/intel_amd_meme.jpg" width="350">
  </center>
</div>

---

# So, can it run TrenchBoot?

- Once all requirements are in place, **you have a chance** that DRTM /
TrenchBoot works for you
  + other cases include:
    * undocumented TXT errors
    * reboots with no information whatsoever
    * weird cases like disappearing TPM devices
    * ...
- The only way to know for sure is to try it out
- But how?

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_boot_flow.drawio.png" width="550">
  </center>
</div>

---

# meta-trenchboot

- Used for testing and demonstration
- Generic image: legacy/UEFI, Linux/Xen, Intel/AMD
- https://github.com/zarhus/meta-trenchboot

```bash
 GNU GRUB  version 2.06

 +----------------------------------------------------------------------------+
 |*Boot Linux normally                                                        |
 | Boot Linux with TrenchBoot                                                 |
 | Boot Xen normally (MB2)                                                    |
 | Boot Xen with TrenchBoot (MB2)                                             |
 | Boot Xen normally (UEFI)                                                   |
 | Boot Xen with TrenchBoot (UEFI)                                            |
 |                                                                            |
 +----------------------------------------------------------------------------+

      Use the ^ and v keys to select which entry is highlighted.
      Press enter to boot the selected OS, `e' to edit the commands
```

---

# trenchboot-hcl

- Heavily inspired by QubesOS HCL (only selected YAML fields are presented here)

```yaml
tpm:
  '1.2'
brand: |
  Dell Inc.
model: |
  OptiPlex 5040
cpu: |
  Intel(R) Core(TM) i5-6600 CPU @ 3.30GHz
versions:
  - works:
      success
    tb-distro: |
      0.5.2
    boot-flow:
      xen
    kernel: |
      6.13.0-yocto-standard
    xen: |
      4.17.4
    txt-error-code: |
      0x00000000
```

---

# trenchboot-hcl

Dumping various logs to help diagnosing failures

- Standard Linux, Xen, TPM logs
- Tools from [tboot](https://sourceforge.net/projects/tboot/) project, such as `txt-stat`
- `txt-suite` from [converged-security-suite](https://github.com/9elements/converged-security-suite)
  + The latest (2.8.0/2.8.1) version does not work
    * https://github.com/9elements/converged-security-suite/issues/406
  + Cannot be build locally
    * https://github.com/9elements/converged-security-suite/issues/408
  + Version 2,6.0 produces results thate are helpful in diagnosis for us

<!--
some PRs tried to fix that, unmberged
-->

---

# trenchboot-hcl

- In [this discussion](https://github.com/zarhus/meta-trenchboot/issues/53#issuecomment-3109323608)
  we are working on narrowing down the list of tests
  critical for our use-case

```bash
04 - CPU supports SMX                        : PASS
05 - CPU supports VMX                        : PASS
[...]
07 - TXT not disabled by BIOS                : PASS
08 - BIOS ACM has run                        : PASS
[...]
12 - TPM connection                          : PASS
13 - TPM is present                          : PASS
14 - TPM NVRAM is locked                     : PASS
21 - PCR 0 is set correctly                  : PASS
23 - TXT mode is valid                       : PASS
36 - TXT not disabled by LCP Policy          : PASS
44 - TXT heap ranges valid                   : PASS
45 - TXT public area reserved in e820        : PASS
[...]
48 - MMIO TPMDecode space reserved in e820   : PASS
59 - CPU supports MTRRs                      : PASS
65 - ACPI RSDP exists and has valid checksum : PASS
66 - ACPI MCFG is present                    : PASS
67 - ACPI DMAR is present                    : PASS
```

---

# trenchboot-hcl - results summary

Results for meta-trenhboot v0.5.2

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_aem_hcl_results.png" width="700">
  </center>
</div>

---

# trenchboot-hcl - conclusions

<v-clicks depth="1">

- "Old" AMD platforms have the best support
  + We (3mdeb) have been focused on this area the most so far
- We do not support "modern" AMD (most likely Zen and newer)
  + DRTM flow is changed here, PSP is involved
  + There's been some work in this area by Oracle regarding AMD servers
  + It needs to be integrated, and applied to "modern" AMD clients as well
- We need proper integration of Intel and AMD Linux patches
  + Linux series should work on Intel, our integrated branch works only on AMD
  + We (3mdeb) have been focused more on AMD in case of Linux
- We **need much more testing**, especially on more modern units
  + Somewhat recent Intel vPro Essentials as a possible indication of
  broadening TXT availability
  + Help needed! (we could use hackaton on Sunday as well)

</v-clicks>

---

# Failure examples

ASRock server - Xen gets stuck when booting with TrenchBoot. Boots fine when
booting normally. No useful logs produced on serial.

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/asrock_xen_boot_fail.png" width="700">
  </center>
</div>

Needs further investigation.

---

# Failure examples

Lenovo m920 Tiny - TPM device disappears when booting Xen with TrenchBoot. Xen
boots fine (and TPM is present) when booting normally.

Needs further investigation.

---

# trenchboot-hcl - contribution

- Follow the README:
  + https://github.com/TrenchBoot/trenchboot-hcl

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_hcl_contributing.png" width="550">
  </center>
</div>

- Improvement ideas
  + Simplify contribution by uploading directly after report is generated
  + Would need to be stored somewhere else than GH (?)

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Project Status

---

# Major milestones

Completed since FOSDEM 2025 status report

- P4 (AMD): https://blog.3mdeb.com/2024/2024-04-11-aem_phase4/

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_aem_phase_4_completed.png" width="600">
    <img src="/@fs/repo/img/logo/nlnet.svg" width="150">
  </center>
</div>

<!--
- AMD has been initially implemented years ago
- needed to be rebased on top of the updated trenchboot approach
-->

---

# Major milestones

Completed since FOSDEM 2025 status report

- P5 (UEFI): https://blog.3mdeb.com/2025/2025-06-10-aem-uefi/

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_aem_phase_uefi_completed.png" width="600">
    <img src="/@fs/repo/img/logo/nlnet.svg" width="150">
  </center>
</div>

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Upstream

---

# Timeline

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_upstream_timeline.drawio.png" width="600">
  </center>
</div>

---

# Relation chain

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_upstream_deps.drawio.png" width="600">
  </center>
</div>

---

# Xen

Possibly the greatest chance of being merged?

- All TrenchBoot patch series are CCed to
  [trenchboot-devel list](https://groups.google.com/g/trenchboot-devel)
- Xen (v3)
  + https://lists.xenproject.org/archives/html/xen-devel/2025-05/msg01686.html
  + https://github.com/TrenchBoot/trenchboot-issues/issues/46#issuecomment-2922390285
  + v4 in the works

---

# GRUB

Needs to wait if/when Linux is merged

- Intel
  + v4 series posted to [grub-devel](https://lists.gnu.org/mailman/listinfo/grub-devel/)
  + https://lists.gnu.org/archive/html/grub-devel/2025-04/msg00273.html
- AMD
  + v2 RFC series posted to [grub-devel](https://lists.gnu.org/mailman/listinfo/grub-devel/)
  + https://lists.gnu.org/archive/html/grub-devel/2025-04/msg00268.html

---

# Linux

Current situation is rather complex

- Intel
  + v14 already - a lot of effort from Ross (Oracle)!
  + https://lore.kernel.org/lkml/20250421162712.77452-1-ross.philipson@oracle.com/
- AMD
  + RFC on top of the Intel patches
  + https://lore.kernel.org/lkml/cover.1734008878.git.sergii.dmytruk@3mdeb.com/

---

# Linux

- About QubesOS?
  + Perhaps worth responding here with QubesOS numbers?
  + Note: we do not **directly** need Linux support for QubesOS AEM
  + https://lkml.org/lkml/2025/4/22/1637

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/qubesos_lkml.png" width="500">
  </center>
</div>

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Further plans

---

# Enhancements

https://github.com/TrenchBoot/trenchboot-issues/milestone/16

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/plans_enhancements.png" width="600">
  </center>
</div>

---

# DRTM between coreboot and UEFI payload

https://github.com/TrenchBoot/trenchboot-issues/milestone/15

<div style="display: flex; justify-content: center; align-items: center;">
  <center>
    <img src="/@fs/repo/img/tb_aem_plans_payload.png" width="500">
  </center>
</div>

---

# Others

- More hardware support for QubesOS AEM
  + MSI PRO B650-A
  + Dasharo-supported hardware (NovaCustom ADL/MTL laptops?)
  + Intel and AMD server boards (?)
- Deliver QubesOS AEM packages for out-of-tree components
- Testing
- Move forward upstream

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Q&A
