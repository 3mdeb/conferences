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
  * [FOSDEM 2025](https://archive.fosdem.org/2024/schedule/event/fosdem-2024-3724-trenchboot-project-status-update/)
  + [Qubes OS Summit 2024](https://youtu.be/5ieNhbLLTIU?si=_E_k6ct9LV0iXYeN)
  * [FOSDEM 2025](https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5979-trenchboot-project-status-update/)

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

## Intel

In order for Intel TXT to function properly the following dependencies need to be established:
 Intel Xeon processor-based server platform with Intel TXT Enabled BIOS
 Intel Virtualization Technology (Intel VT) must be enabled
 Intel Virtualization Technology with Directed I/O (Intel VT-d) must be enabled
 A Trusted Platform Module (TPM) v1.2 must be enabled and activated
 The platform specific Intel SINIT ACM needs to be installed into the platform
 Finally, you need a hypervisor that supports trusted boot (t-boot

Source: https://www.intel.com/content/dam/www/public/us/en/documents/guides/intel-one-stop-txt-activation-guide.pdf

OpenQA:

AEM setup: https://openqa.3mdeb.com/tests/416
AEM first run: https://openqa.3mdeb.com/tests/417
AEM second run: https://openqa.3mdeb.com/tests/418

# meta-trenchboot

# trenchboot-hcl

- about the project
- some results

---

# Upstream

* Linux
 - Intel (v14): https://lkml.org/lkml/2025/4/21/688
 - AMD (RFC)
   - Intel must go in first
* GRUB
  -
  - latest info: https://github.com/TrenchBoot/trenchboot-issues/issues/38#issuecomment-2843602445
    - list archive does not work for me?
* Xen (v3)
  - https://lists.xenproject.org/archives/html/xen-devel/2025-05/msg01686.html
  - https://github.com/TrenchBoot/trenchboot-issues/issues/46#issuecomment-2922390285
  - v4 in the works
All TrenchBoot patch series are CCed to trenchboot-devel:
- https://groups.google.com/g/trenchboot-devel

---

# nlnet phases

Chagned since FOSDEM 2025 status report
- P4 (AMD): https://blog.3mdeb.com/2024/2024-04-11-aem_phase4/ 
- P5 (UEFI): https://blog.3mdeb.com/2025/2025-06-10-aem-uefi/

---

# plans

https://github.com/TrenchBoot/trenchboot-issues/milestones
- 

## enhancements

https://github.com/TrenchBoot/trenchboot-issues/milestone/16

plans_enhancements.png

## DRTM between coreboot and UEFI payload

https://camo.githubusercontent.com/aaf8708e3ca99122a50cc3ee8a5797a2bc9e0c34cec218dfcb26160deba1f2de/68747470733a2f2f696d672e706c616e74756d6c2e62697a2f706c616e74756d6c2f7376672f5a4c4e315258656e3442747841715266444a486a7171434c384847324134423935574752444c394c4c4d4f7a6d3059704868514e62624a767a75777a42366d574833615073735f6370526e7651777754627a4f4e496f7351706379716a694a37664c3471394c4a6d4a6d33536f366e6e51717348677578486e6941376f735f67772d4b646c68636437444376504f6953644f4646737643494454345339667635797341524c365953556c3036424374633758485070336f504e385a434d396d4f752d34416d5a424858594468587a4f696b5347503269364248735764744c574f4742615f677831643831724b637a794963697367614c51685a585f56744b5365686f536e6731505638595a79454370724e394e49707074677a6e483366756c66562d2d6471457561434f334e71724e474b484b78624867444c6772704b4845317a5045625662536c5a6e6b575a4c4757536d4e75357845322d4f385762336b46563677634f37354d51366258394a53315558572d395173584d37366a6a6958794f48366346465947477176437551696d6669626163374961536c4934587561694568486858324b6b5a54743442447248636130774a30334e63376a45434846726744306b3475623054574c63584e64336353396332424853514c6e6f5a327044354830314e4f7648524153504d314c775463316167587a4642454d70713550642d453357335f61765a466c335658736f7575332d3834615547356251656e4b4c6641387844487549444c6b794558757743507841416b79514b666261424a4d6675414e71434f4c43686b493444376232546d5943716d6f57455368514a387a6d41796a6f4d787131586e77495433486f534d3053554f48346f70544251302d766f357058717a654b78666e6870744958576958396365763236692d52387676695a6a6132513166544732786d6869646e4a4662507358415537794f5336326265487062746f6e657975546b55655a595a794661355656616265626e6f596959676337416f414a7a7334557a745a59416e5f4a38336c4c486742717a71464753637a787157674d4133724131377667444a7661693646464a31413348706d4d74567a6a396e685f4670485f6b6b7a7033794c4f7a7a71764d71415f6462366e396c4f705a63536738484b3852596b71617854454242397a686a4b4d4c4e4b5464326c49786667712d4e4153696d64364a4f772d7974745356555664464a374d7942736b626848374b545a5750795679724d32647a4d5f6d3430

## New hardware support for QuubesOS AEM

- MSI PRO B650m-A

## Testing, upstream

---

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Q&A
