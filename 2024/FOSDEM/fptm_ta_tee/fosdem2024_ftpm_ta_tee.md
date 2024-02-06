class: center, middle, intro

# Securing Embedded Systems with fTPM implemented as Trusted Application in TEE

### FOSDEM 2024

## Tymoteusz Burak

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
  src="/remark-templates/3mdeb-presentation-template/images/tymek_burak.png"
  width="150px" style="marking-top:-50px">
]

.center[Tymoteusz Burak]
.center[_Junior Embedded Systems Developer_]
.right-column50[
- 8 months in 3mdeb
- Integration of functionalities and the creation of Operating Systems for
embedded devices in Yocto
- Wrapping up my Bachelor's Degree in Automation and Robotics
]
.left-column50[
- <a href="mailto:tymoteusz.burak@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    tymoteusz.burak@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/tymoteusz-burak-a108252a0/">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    linkedin.com/in/tymoteusz-burak-a108252a0
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

.left-column50[

<img src="/remark-templates/3mdeb-presentation-template/images/openpower.svg"
    width="200px" style="margin-left:120px">
]

.right-column50[
<img src="/img/crosscon_logo.svg" width="200px" style="margin-left:40px;
margin-top:40px">
]

<br>
<br>
<br>
<br>
<br>
<br>

- coreboot licensed service providers since 2016 and leadership participants
- UEFI Adopters since 2018
- Yocto Participants and Embedded Linux experts since 2019
- Official consultants for Linux Foundation fwupd/LVFS project since 2020
- IBM OpenPOWER Foundation members since 2020

---

# Agenda

- What is TPM?
- What is fTPM?
- What is Arm TrustZone and how does it relate to fTPM?
- Arm TrustZone on different Cortex series
- Implementing fTPM in practice

---

# What is TPM (Trusted Platform Module)?

_"A computer chip (microcontroller) that can securely store artifacts used
to authenticate the platform (your PC or laptop). These artifacts can
include passwords, certificates, or encryption keys. A TPM can also be used to
store platform measurements that help ensure that the platform remains
trustworthy."_ *

.center[
<img src="/img/tpm_chip.png" height="350px" style="margin-top:-50px">
]

.footnote[

\* quote from
[Trusted Computing Group® - Trusted Platform Module (TPM) Summary](https://trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)
]

???

- TPM is independent and called from the userspace to perform cryptographic
operations
- Trusted Computing Group established a standard for TPM
    + They are an international organization that promotes open standards for
    hardware-enabled-trusted computing

---

# TPM features

Isolation from Host OS:
- Stores Secrets Safely: Encrypts and stores cryptographic keys separately
from the host operating system, enhancing security.
- Protection Against Tampering: Secrets (like encryption keys) are not exposed
to software vulnerabilities, protecting against unauthorized access and
tampering.

System Integrity Verification:
- Storing Measurements in PCR Registers: During the boot process, the TPM
measures components (like BIOS, bootloader, OS) and stores these measurements
as hashes in PCR registers.
- Detects Changes: Any alteration in the boot process changes these
measurements, enabling detection of unauthorized changes or tampering.

---

# TPM features

Secure Random Number Generation:
- High-Quality Random Number Generation: TPM includes a hardware-based random
number generator (RNG) to produce cryptographically secure random numbers.
These numbers are essential for creating unique encryption keys and for
various cryptographic operations, ensuring that the cryptographic processes
are robust against attacks.
- Enhances Cryptographic Security: By providing a source of entropy that is
less predictable than software-based RNGs, the TPM's RNG strengthens the
security of cryptographic operations as it's more difficult for attackers
to predict or reproduce the cryptographic keys.

---

# Variations of TPM

- Discrete TPM
- Integrated TPM
- Software TPM
- Firmware TPM

---

# Variations of TPM

- Discrete TPM
    + Most secure
    + Separate physical chip installed on the motherboard
    + Operates independently from the main CPU
- Integrated TPM
- Software TPM
- Firmware TPM

---

# Variations of TPM

- Discrete TPM
    + Most secure
    + Separate physical chip installed on the motherboard
    + Operates independently from the main CPU
- Integrated TPM
    + Integrated into another chip that provides functions other than security
    + Economical and space-saving, reducing the need for additional components
    + Integration makes it less tamper-resistant
- Software TPM
- Firmware TPM

---

# Variations of TPM

- Discrete TPM
    + Most secure
    + Separate physical chip installed on the motherboard
    + Operates independently from the main CPU
- Integrated TPM
    + Integrated into another chip that provides functions other than security
    + Economical and space-saving, reducing the need for additional components
    + Integration makes it less tamper-resistant
- Software TPM
    + Software emulation that runs in the user space
    + Least secure and susceptible to software attacks
    + Useful for testing and prototyping
- Firmware TPM

---

# fTPM

- Firmware TPM
    + Software implementation that runs in a Trusted Execution Environment
    (TEE)
    + Is separated from the rest of the programs that are running on the CPU
    + Cheap and can be implemented on already existing devices

???

- Needs a Trusted Execution Environment

---

# Arm TrustZone for Cortex-A

_"Confidential Computing is the protection of data in use by
performing computation in a hardware-based, attested Trusted
Execution Environment (TEE)."_

.center[
<img src="/img/TEE_ARM_Cortex-a.svg" height="250px">
]

???
- "The Trusted Computing Group whitepaper “Securing Mobile Devices on Converged
  Networks”
---

# Arm TrustZone for Cortex-A

<br>

.center[
<img src="/img/TEE_ARM_Cortex-a_exception_levels.svg"
    height="250px">
]

???

---

# Arm TrustZone for Cortex-M

<br>

.center[
<img src="/img/TEE_ARM_Cortex-m.svg" height="250px">
]

???

- More viable to
- More powerful processors like M23 or M33 could benefit from having an fTPM in
some scenarios

---

# Arm TrustZone Fallbacks

<br>
<br>

### The best protected systems have dedicated hardware security measures included from the beginning of their design process, starting with the specification for the processor core and the SoC infrastructure

---

# Arm TrustZone Fallbacks

- No secure storage*
- No secure counter
- No secure clock
- No secure source of entropy*

???

- eMMC storage controller can ensure secure storage
- Write-once secure fuses can act as sources of randomness
    + Basically acting as seed
- "The Trusted Computing Group whitepaper “Securing Mobile Devices on Converged
 Networks”

---

# fTPM Fallbacks

- Coldboot
- Bus sniffing
- JTAG
- Worlds can't run in parrarel
    + Running operations on fTPM freezes the normal OS

???

- Because data is stored in RAM
- This could work better on Cortex-M where TrustZone works through interrupts

---

# Implementing fTPM in practice

<br>
<br>

### 1. Build OP-TEE for your platform

### 2. Build fTPM as a TA for OP-TEE

### 3. Add userspace TPM/fTPM support

---

# Kernel module

### [drivers/char/tpm/tpm_ftpm_tee.c](https://elixir.bootlin.com/linux/latest/source/drivers/char/tpm/tpm_ftpm_tee.c)

```c
// SPDX-License-Identifier: GPL-2.0
/*
 * Copyright (C) Microsoft Corporation
 *
 * Implements a firmware TPM as described here:
 * https://www.microsoft.com/en-us/research/publication/ftpm-software-implementation-tpm-chip/
 *
 * A reference implementation is available here:
 * https://github.com/microsoft/ms-tpm-20-ref/tree/master/Samples/ARM32-FirmwareTPM/optee_ta/fTPM
 */

(...)
```

---

# Kernel module

### TPM

<img src="/2024/FOSDEM/fptm_ta_tee/img/tpm_ftpm_tee_driver1.svg" height="79px">
<br>
<br>
<br>

### fTPM

<img src="/2024/FOSDEM/fptm_ta_tee/img/tpm_ftpm_tee_driver2.svg" height="130px"style="margin-top:-25px">

---

# [microsoft/ms-tpm-20-ref](https://github.com/microsoft/ms-tpm-20-ref)

.center[
<img src="/2024/FOSDEM/fptm_ta_tee/img/false_instruction.png" width="500px">
<br>
<img src="/2024/FOSDEM/fptm_ta_tee/img/github_error.png" width="500px">
]

???
- Provided "As Is"

---

# Yocto

### [meta-arm - optee-ftpm_git.bb](https://layers.openembedded.org/layerindex/recipe/235743/)

```bitbake
SUMMARY = "OPTEE fTPM Microsoft TA"
DESCRIPTION = "TCG reference implementation of the TPM 2.0 Specification."
HOMEPAGE = "https://github.com/microsoft/ms-tpm-20-ref/"

COMPATIBLE_MACHINE ?= "invalid"
COMPATIBLE_MACHINE:qemuarm64 = "qemuarm64"
COMPATIBLE_MACHINE:qemuarm64-secureboot = "qemuarm64"
COMPATIBLE_MACHINE:qemu-generic-arm64 = "qemu-generic-arm64"
COMPATIBLE_MACHINE:qemuarm-secureboot = "qemuarm"

(...)
```

???

- Available as a Yocto recipe but only for QEMU
    + Can be adapted for custom boards

---

# Contact us

.left-column45[
<img src="/img/zarhus_logo.png" height="150px" style="margin-top:-10px; margin-left:200px">
]

.right-column55[

## [Zarhus OS](https://docs.zarhus.com/)

]

<br>
<br>
<br>
<br>
<br>

.right-column50[
- <a href="https://3mdeb.com">https://3mdeb.com</a>

- <a href="https://calendly.com/3mdeb/consulting-remote-meeting">Book a call</a>

- <a href="https://newsletter.3mdeb.com/subscription/PW6XnCeK6">
    Sign up for the newsletter
  </a>
]

.left-column50[
- <a href="https://www.linkedin.com/company/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/company/3mdeb
    </a>

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
]

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Feel free to contact us if you believe we can help you in any way. We are
always open to cooperate and discuss

???

- We're researching possibilities of using this technology on Embedded Devices
    + Especially in the context of our own Embedded Distribution Zarhus OS

---

# Resources

- ##### Will Arthur, David Challener, and Kenneth Goldman. _A Practical Guide to TPM 2.0: Using the Trusted Platform Module in the New Age of Security_. Apress Berkeley, CA, 2015. DOI: 10.1007/978-1-4302-6584-9

- ##### Sandro Pinto and Nuno Santos. 2019. _Demystifying Arm TrustZone: A Comprehensive Survey._ ACM Comput. Surv. 51, 6, Article 130 (January 2019), 36 pages. https://doi.org/10.1145/3291047

- #### [fTPM: A Software-only Implementation of a TPM Chip](https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_raj.pdf)

##### Himanshu Raj, ContainerX; Stefan Saroiu, Alec Wolman, Ronald Aigner, Jeremiah Cox, Paul England, Chris Fenner, Kinshuman Kinshumann, Jork Loeser, Dennis Mattoon, Magnus Nystrom, David Robinson, Rob Spiger, Stefan Thom, and David Wooten, Microsoft

#### [USENIX Security '16 presentation by Stefan Saroiu](https://www.youtube.com/watch?v=VdqOc4Rv7QQ)

- #### [Trusted Computing Group - TPM 2.0 A Brief Introduction](https://trustedcomputinggroup.org/wp-content/uploads/2019_TCG_TPM2_BriefOverview_DR02web.pdf)

- #### [TEEs are not Silver Bullets - David Cerdeira](https://crosscon.eu/blog/tees-are-not-silver-bullets)

- #### [OP-TEE Documentation](https://optee.readthedocs.io/en/latest/)

- #### [Introduction to Trusted Execution Environment and ARM's TrustZone](https://sergioprado.blog/introduction-to-trusted-execution-environment-tee-arm-trustzone/)

- #### [Develop Secure Cortex-M Applications with Trustzone - Kristoffer Martinsson](https://www.youtube.com/watch?v=TkFC4Q2BwCM)

- #### [jbech-linaro/manifest](https://github.com/jbech-linaro/manifest/tree/ftpm) and [jbech-linaro/docker_optee](https://github.com/jbech-linaro/docker_optee)

---

<br>
<br>
<br>

## .center[Q&A]
