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

<!-- markdownlint-disable MD022 MD003 MD033 -->
---
layout: two-cols-header
class: text-center
---

# Introduction to modern server platforms

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

<!-- markdownlint-enable MD022 MD003 MD033

The pictures represent server platforms that are going to be available with
Dasharo firmware.

The ASRock SPC741D8-2L2T/BCM has already a v0.9.0 release published. Board uses
Sapphire Rapids CPU (4th Gen Intel Xeon Scalable Processors)

The GIGABYTE MZ33-AR1 is still work-in-progress as the coreboot support is
basically made from scratch.

As you can see the board may have lots of DIMM slots. The GIGABYTE MZ33-AR1
has 24 DIMM slots and can support up to 6TB of RAM (this is per socket).

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

<!-- markdownlint-enable MD033

Turin CPU has almost all line with Gen 5 speed.
There are couple Gen3 lines for less demanding connections.

Hard to obtain from non-China sources.

Also the length of cables may affect the PCIe bandwidth.

There are also PCIe to MCIO adapter with PCIe retimers for signal conditioning.

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
    <div style="float: right; width: 50%;">
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

# Secure Encrypted Virtualization (SEV)

* Set of technologies improving the confidentiality and integrity protection
  of guest VMs

* First technology introduced in 2016 with later generations further adding
  more features

* **SEV** - guest memory isolation by one key per guest encryption

* **SEV-ES** - Encrypted state of guest registers, even from the hypervisor

* **SEV-SNP** - Secure Nested Paging, provides a protected private memory to guest

* **SEV-TIO** - Trusted I/O, lets the guest choose whether it trusts a device
  enough to allow the device access to guest private memory

---

# SEV Encrypted State

<!-- markdownlint-disable MD033 -->

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/sev_es.png" width="95%">
  <figcaption>
    <a href= "https://www.amd.com/content/dam/amd/en/documents/epyc-business-docs/white-papers/Protecting-VM-Register-State-with-SEV-ES.pdf">
      Protecting VM register state with SEV-ES Whitepaper
    </a>
  </figcaption>
</figure>

<!-- markdownlint-enable MD033

Whenever a VM stops running, due to an interrupt or other event, its register
contents are saved to hypervisor memory and this memory is readable by the
hypervisor even if SEV is enabled. This information could allow a malicious or
compromised hypervisor to steal information or alter critical values in guest
state such as an instruction pointer, encryption key, etc.

With SEV-ES, both the initial memory image as well as the initial CPU register
state must be encrypted by the AMD Secure Processor (AMD-SP) before execution
of the guest VM can start. During this initialization process, the memory
image and initial CPU register state is measured cryptographically by the
AMD-SP to generate a launch receipt that may be used for attestation of the
guest. This attestation enables the owner of the guest VM to determine if the
VM started successfully with the correct image and register state prior to
releasing it secrets.

Using SEV-ES may help in limiting the problems of "hypervisor as a single point
of failure" and protect the AppVMs from compromised hypervisor.

-->

---

# SEV Secure Nested Paging

<!-- markdownlint-disable MD033 -->

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/sev_snp.png" width="100%">
  <figcaption>
    <a href="https://www.amd.com/content/dam/amd/en/documents/developer/sev-tio-whitepaper.pdf">
      AMD SEV-TIO: Trusted I/O for Secure Encrypted Virtualization Whitepaper
    </a>
  </figcaption>
</figure>

<!-- markdownlint-enable MD033

SEV-SNP allows a guest to separate its memory into shared and private memory.
Shared memory is accessible to host software and is marked as hypervisor-owned
in the Reverse Map Table (RMP), a data structure that stores the SEV-SNP
security attributes of each page of memory in the system. Private memory is
assigned to the guest in the RMP, writeable only by the guest, and encrypted
with the guest’s unique memory encryption keys. The guest uses private memory
to store sensitive data and its executable code. The CPU and IOMMU both
enforce the access control policy for guest private memory by checking the RMP
as required during address translation to ensure that the software or device
accessing memory has sufficient privileges.

SNP architecture protect guests from maliciously programmed devices by
treating all device accesses as if they originated from host software
and are therefore untrusted.

If the guest needs data to flow between its private memory and the assigned
device, the guest must copy the data in and out of a shared buffer that is
accessible by both the guest and assigned devices. This method is called
bounce buffering, depicted on the left portion of Figure 1, because the data
bounces to and from the shared memory buffer. This may have performance
impacts on I/O due to the extra memory movement required.

Further, because all communication between the guest and the device, including
device register access, must occur through shared memory, all traffic is
visible to host software. To protect the confidentiality and integrity of
device communication with the guest, device specific protocols must be
established between the guest and device.

It could serve as an enhancement to Qubes' vchan based on Xen Grant Tables.

-->

---

# SEV Trusted I/O

<!-- markdownlint-disable MD033 -->

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/sev_tio.png" width="500px">
  <figcaption>
    <a href="https://www.amd.com/content/dam/amd/en/documents/developer/sev-tio-whitepaper.pdf">
      AMD SEV-TIO: Trusted I/O for Secure Encrypted Virtualization Whitepaper
    </a>
  </figcaption>
</figure>

<!-- markdownlint-enable MD033 -->

<!--

AMD has worked with PCI SIG and industry partners to develop and ratify the
TEE Device Interface Security Protocol (TDISP), a standard intended to address
the need for trust in devices by guests in confidential compute environments.
TDISP defines new protocols and functions of devices that enable them to
authenticate themselves, prevent traffic interception or masquerading on the
PCIe fabric, attest to their configuration, and isolate guest workloads from
device controls available to host drivers.

The data path of a TDISP device to the guests it serves is protected with the
PCI Integrity and Data Encryption (IDE) protocol. IDE encrypts and
authenticates all device traffic in an end-to-end stream where only the root
port and the TDISP device possess the IDE stream keys which prevents
intervening PCIe switches, physical attackers, and maliciously designed
devices on the PCIe fabric from mounting man-in-the middle or masquerading
attacks on fabric traffic. Any bad actors in the fabric will only see
ciphertext and cannot alter the stream without detection by the device and
root port.

The AMD Secure Processor (ASP) hosts the SEV firmware which plays a central
role in orchestrating the lifecycle of secure guests. SEV-TIO brings new
commands and guest request messages to configure the IOMMU, the PCIe root
complex, and the architectural data structures necessary to bring TDIs into
the trust boundary of guests. Further, to serve the role of TSM, the ASP also
implements an SPDM responder which communicates with the DSMs of TDISP
devices.

As with SEV-SNP today, the IOMMU is responsible for address translation and
performing RMP checks on DMA to protect the confidentiality and integrity of
SEV-SNP guests. SEV-TIO enriches the RMP checks performed by the IOMMU to
allow devices to access guest private memory directly after the guest
indicates that it trusts the device and its configuration.

Finally, SEV-TIO adds support to the PCIe controller to construct IDE streams
for the purpose of protecting the confidentiality and integrity of guest data
over the PCIe fabric between the root complex and the TDISP device. IDE
streams also authenticate traffic to detect malicious agents on the PCIe
fabric attempting to masquerade as a trusted device or as the root complex.

Conventionally, the hypervisor is responsible for emulating IOMMU behavior to
a guest. When a guest needs to send a command to th IOMMU, the hypervisor
intercepts that access and submits the request to the IOMMU on behalf of the
guest. To improve performance of the guest IOMMU access path, AMD offers a
Virtualized IOMMU (vIOMMU). A vIOMMU is a virtual interface to the IOMMU’s
command buffers, event log, and Peripheral Page Request (PPR) log. Through
this interface, the guest interacts directly with the IOMMU instead of relying
on hypervisor emulation.

SEV TIO and TDISP PCI specification should help with malicious
PCIe devices impersonating other device, type or class of the device.

-->

---

# Smart Data Cache Injection

<!-- markdownlint-disable MD033 -->

<figure>
  <img src="/@fs/repo/public/2025/QubesOSsummit/amd_sdci.png" width="380px">
  <figcaption>
    <a href="https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/white-papers/58725.pdf">
      AMD Smart Data Cache Injection (SDCI) White Paper Whitepaper
    </a>
  </figcaption>
</figure>

<!-- markdownlint-enable MD033 -->

```bash
lspci |grep SDXI
01:00.1 SNIA Smart Data Accelerator Interface (SDXI) controller: Advanced Micro Devices, Inc. [AMD] SDXI
42:00.1 SNIA Smart Data Accelerator Interface (SDXI) controller: Advanced Micro Devices, Inc. [AMD] SDXI
a4:00.1 SNIA Smart Data Accelerator Interface (SDXI) controller: Advanced Micro Devices, Inc. [AMD] SDXI
e1:00.1 SNIA Smart Data Accelerator Interface (SDXI) controller: Advanced Micro Devices, Inc. [AMD] SDXI
```

<!--

Smart Data Cache Injection (SDCI) allows preloading of data in processor
caches by steering applicable I/O data directly to a core’s L2 cache.

Cache residency of critical code is key to overall application performance.
Unlike alternative cache injection solutions, SDCI enables endpoints to
control which data are injected into caches and thus reduces cache pollution
and enhances system performance.

Both host and endpoints must support the TPH feature; TLP Hints (TH) in the
TLP header identifies data that are candidates for cache insertion. In a
typical implementation, the host driver and endpoint firmware collaborate on
device settings to direct I/O packets to the correct cache locations.

-->

---

# Qubes Air

How this maps to the Qubes Air architecture?

* Server virtualization security features may provide a stronger foundation
  for confidential and privacy-sensitive qubes

* Server virtualization security features can potentially limit the impact of
  hypervisor vulnerabilities on the qubes

* Applicable to all Qubes Air use cases:

  - "Qubes in the cloud"

  - "Qubes Hybrid Mode"

  - Server as an "air-gapped" device with Qubes

---

# Roadmap to a certified Qubes OS server

<!-- markdownlint-disable MD033 -->

<center>
  <div style="display: table">
    <div style="float: left; width: 50%; padding: 30px;">
      <img src="/@fs/repo/public/2025/QubesOSsummit/Qubes_OS_Logo.svg" width="200px">
    </div>
    <div style="float: right; width: 50%;">
      <img src="/@fs/repo/public/2025/QubesOSsummit/gigabyte_mz33_ar1.png" width="200px">
    </div>
  </div>
</center>

<!-- markdownlint-enable MD033 -->

GIGABYTE MZ33-AR1 as a first Qubes certified server?

1. Open-source boot firmware.
2. Support for new virtualization features introduced by silicon vendors.
3. Creation of extended certification requirements for servers.
4. Validation and testing (?)

<!-- markdownlint-disable MD022 MD003 -->
---
layout: two-cols-header
---
<!-- markdownlint-enable MD022 MD003 -->

# Additional certification requirements

::left::

<!-- markdownlint-disable MD033 -->

<center><img src="/@fs/repo/public/2025/QubesOSsummit/Qubes_OS_Logo.svg" width="350px"></center>

<!-- markdownlint-enable MD033 -->

::right::

### Server certification additional requirements

<br>

* Strong guest memory and state (SEV, SEV-ES)
* Strong guest private memory protection (SEV-SNP)
* Strong guest device I/O isolation (SEV-TIO/vIOMMU)
* Any others?

Needs further analysis:

* Compute Express Link (CXL) - may pose challenges to protect against DMA
  properly

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Demo time

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
