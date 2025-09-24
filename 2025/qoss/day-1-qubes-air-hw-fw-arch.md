---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Qubes Air: Hardware, Firmware, and Architectural Foundations

### Michał Żygowski

---

# $ whoami

<!-- markdownlint-disable MD033 -->

<figure>
  <img src="/@fs/repo/public/miczyg.png" width="250px">
  <figcaption>
    <b>Michał Żygowski</b><br>
    <i>3mdeb Senior Firmware Engineer</i>
  </figcaption>
</figure>

<!-- markdownlint-enable MD033 -->

* Core developer of coreboot.
* Maintainer of Braswell SoC, PC Engines, Protectli, MSI and Libretrend
  platforms.
* Interested in advanced hardware features, security and coreboot.
* Open-source firmware enthusiast and conference speaker.

---

# Agenda

* An introduction to modern server platforms
* Dasharo firmware integration leveraging AMD OpenSIL
* OpenBMC (ZarhusBMC) as the secure Root of Trust
* Server security implications
  - BMC security
  - AMD Platform Security Processor (PSP/ASP)
  - Platform Firmware Resiliency (PFR)
* Roadmap toward certifiable, secure, server-grade Qubes OS implementations

---

# Introduction to modern server platforms

* More complex hardware designs than regular client desktop/laptop

* More PCIe expansion slots, although may often need special MCIO cables and
  adapters

* Many DIMM slots - harder to run out of RAM if you can afford denser modules

* Longer boot times - often multiple PCI domains and many internal devices to
  initialize
  - especially on AMD where memory training happens on every boot

* Remotely manageable - each server has a Baseboard Management Controller (BMC)
  providing KVM

* Pinnacle of current technology and features, including IOMMU/DMA

* \$\$\$ Pricey \$\$\$! Can be 2-3 times more expensive than client
  desktop/laptop even with the lower grade components

<!--

Bullets split to cover slide page evenly.

Some of the points we will discuss along with the presentation.

-->

<!-- markdownlint-disable MD022 MD003 -->
---
layout: two-cols-header
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Introduction to modern server platforms

<!-- markdownlint-disable MD033 -->

::left::

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/asrock_spc741d8.png" width="400px">
  <figcaption>
    ASRock SPC741D8-2L2T/BCM<br>
    4th Gen Intel(R) Xeon(R) Scalable Processors - Sapphire Rapids
  </figcaption>
</figure>

::right::

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/gigabyte_mz33_ar1.png" width="290px">
  <figcaption>
    GIGABYTE MZ33-AR1<br>
    5th Gen AMD EPYC(TM) 9005 Processors - Turin
  </figcaption>
</figure>

<!-- markdownlint-enable MD033 -->

<!--

The pictures represent server platforms that are going to be available with
Dasharo firmware.

The ASRock SPC741D8-2L2T/BCM has already a v0.9.0 release published. Board uses
Sapphire Rapids CPU (4th Gen Intel Xeon Scalable Processors)

The GIGABYTE MZ33-AR1 is still work-in-progress as the coreboot support is
basically made from scratch.

As you can see the board may have lots of DIMM slots. The GIGABYTE MZ33-AR1
has 24 DIMM slots and can support up to 6TB of RAM (this is per socket).

-->

<!-- markdownlint-disable MD022 MD003 -->

---
layout: two-cols
---

<!-- markdownlint-enable MD022 MD003 -->

## ASRock SPC741D8-2L2T/BCM

<br>

* Silicon init: [Intel
  FSP](https://github.com/intel/FSP/tree/master/EagleStreamFspBinPkg)
  (closed-source) &#x274C;
  - Intel FSP ecosystem is pretty stable, although server FSP is
     functionally-limited on non-UEFI
* **Boot time: < 1 min** with fast boot &#x2705;
* **Open-source SMM code** &#x2705;
* Server version of Intel Management Engine, Server Platform Services (SPS) on
  chipset
  - **Footprint: occupies 48MB (75%) of flash** &#x1F631; &#x274C;
  - Provides management capabilities &#x274C;
  - A minimalistic ME Ignition FW could be used to reduce this blob footprint
    and remove management features &#x2705;

::right::

## GIGABYTE MZ33-AR1

<br>

* Silicon init: [AMD
  OpenSIL](https://github.com/openSIL/openSIL/tree/turin_poc) (open-source)
  &#x2705;
  - Proof of Concept, evaluation only, without support for production
    implementations
* **Boot time: 2 min+**, memory trained on each boot &#x274C;
* **Open-source SMM code** &#x2705;
* AMD Platform Security Processor (ASP), equivalent to Intel ME, but on CPU
  - **Footprint: ~3MB** (reasonably acceptable) &#x2705;
  - Responsible for memory init and encryption &#x274C;
  - Also involved in SEV-ES/SNP/TIO &#x274C;

<!--

Each board and silicon it is made of has some pros and cons.

On AMD the boot time is strictly dependent on memory capacity. Servers do not
seem to support any fast-boot with previously trained memory settings saved in
non-volatile storage.

-->

<!-- markdownlint-disable MD022 MD003 -->

---
layout: two-cols-header
---

<!-- markdownlint-enable MD022 MD003 -->

## Dasharo firmware for servers

<center><img src="/@fs/repo/public/dasharo-logo-3.png" width="400px"></center>

<br>

::left::

## ASRock SPC741D8-2L2T/BCM

<br>

* [v0.9.0 released 18.09.2025](https://docs.dasharo.com/variants/asrock_spc741d8/releases/#v090-2025-09-18)

::right::

## GIGABYTE MZ33-AR1

<br>

* v0.9.0 estimated Q4 2025

<!-- markdownlint-disable MD022 MD003 -->

---
layout: two-cols-header
class: text-center
---

<!-- markdownlint-enable MD022 MD003 -->

# PCIe expansion on servers

* Almost all lanes are PCIe Gen 5.0 on AMD Turin CPU
* Standard PCIe x16 slots
* MCIO (x8 lanes per connector)
  - requires adapters to standard PCIe slots and MCIO cables

<!-- markdownlint-disable MD033 -->

::left::

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/pcie_to_mcio.png" width="500px">
  <figcaption>
    PCIe to MCIo adapter
  </figcaption>
</figure>

::right::

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/mcio_to_pcie.png" width="500px">
  <figcaption>
    MCIO to PCIe adapter
  </figcaption>
</figure>

<!-- markdownlint-enable MD033 -->

<!--

Turin CPU has almost all line with Gen 5 speed.
There are couple Gen3 lines for less demanding connections.

Hard to obtain from non-China sources.

Also the length of cables may affect the PCIe bandwidth.

There are also PCIe to MCIO adapter with PCIe retimers for signal conditioning.

-->

<!-- markdownlint-disable MD022 MD003 -->

---
layout: two-cols-header
class: text-center
---

<!-- markdownlint-enable MD022 MD003 -->

# Remote management

<!-- markdownlint-disable MD033 -->

<center><img src="/@fs/repo/public/2025/QubesOSsummit/bmc_kvm.png" width="100%"></center>

<!-- markdownlint-enable MD033 -->

* Remote Management through Baseboard Management Controller (BMC)
* Offers Power management and KVM
  - Can be a big threat to dom0 if the remote access is not secured
  - Remote KVM can be "killed" by unplugging the Ethernet from IPMI port
  - Or by disabling given USB port connecting the BMC to host in the firmware
    setup (if available)

---

# ZarhusBMC as secure Root of Trust

<!-- markdownlint-disable MD033 -->

<center>
  <div style="display: table">
    <div style="float: left; width: 50%;">
      <img src="/@fs/repo/public/2025/QubesOSsummit/zarhus-logo-new.png" width="220px">
    </div>
    <div style="float: left; width: 50%;">
      <img src="/@fs/repo/public/2025/QubesOSsummit/OpenBMC_logo.png" width="270px">
    </div>
  </div>
</center>

<!-- markdownlint-enable MD033 -->

* ZarhusBMC - OpenBMC-based solution to improve trusworthiness
* Hardware Root of Trust is possible on AST2600 used on both server boards
  - BMC reads the portion of BIOS flash that should be authenticated/verified
  - If verification passes the board can be powered on, otherwise refuse to
    power on
  - No need to fuse the CPU and bind the CPU to the board vendor, just fuse
    BMC chip

<!--

Server platform have a BMC and a FPGA/CPLD to assist in power sequencing and
platform booting.

* BMC has access to BIOS flash
* Power button goes through the BMC to host, BMC sends the power button
  signal to the CPU. But there is a possibility that this logic is handled
  automatically by the AST2600 chip without software intervention.
* This can be used to provide Root of Trust for the host without fusing the
  CPU itself

The GIGABYTE MZ33-AR1 comes unfused, so we have freedom of implementing our own
root of trust.

-->

---

# Server security implications - BMC security

<br>

* ASPEED chips are the most common on the market

* Hardware-based Root of Trust/Secure Boot possible since ASPEED AST2600

* OTP memory for key storage

* Only signed and verified U-boot SPL image is executed

* [Public tools](https://github.com/AspeedTech-BMC/socsec) available

<!-- markdownlint-disable MD022 MD003 -->

---
layout: two-cols-header
---

<!-- markdownlint-enable MD022 MD003 -->
# Server security implications - PFR

::left::

<!-- markdownlint-disable MD033 -->

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/intel_pfr.png" width="350px">
  <figcaption>
    Platform Firmware Resiliency<br>
    Intel Platform Security (document #784473, public)
  </figcaption>
</figure>

<!-- markdownlint-enable MD033 -->

::right::

## Platform Firmware Resiliency

<br>

* Described by NIST SP 800-193: Platform Firmware Resiliency Guidelines
* Root of Trust inside CPLD/FPGA for whole platform, including BMC and host
  firmware
* FPGAs/CPLDs with special security properties compliant with NIST guidelines
* Silicon vendor agnostic

---

# Server security implications - AMD PSP/ASP

## AMD Secure Processor/Platform Security Processor

<br>

* ARM co-processor living inside each AMD CPU/APU

* Performs early HW initialization before x86 CPU is released from reset

* Responsible for memory training and encryption features

* Nowadays also participates in dynamic measured launch (DRTM/TrenchBoot)

* Overly privileged, like Intel ME. If broken through, may pose a huge threat
  to the system

* Some of Secure Encrypted Virtualization (SEV) source code has been
  [published on GitHub](https://github.com/amd/AMD-ASPFW)

---

# Roadmap to a certified Qubes OS server

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Questions?

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Thank you
