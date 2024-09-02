class: center, middle, intro

# Practical Security for Embedded Systems: Implementing TEE and Secure Storage

### Yocto Project DevDay 2024

## Tymoteusz Burak

## Daniil Klimuk

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.left-column50[.center[
<img
src="/remark-templates/3mdeb-presentation-template/images/tymek_burak.png"
width="150px" style="marking-top:-50px">

Tymoteusz Burak

_Junior Embedded Systems Developer_]

- <a href="mailto:tymoteusz.burak@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    tymoteusz.burak@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/tymoteusz-burak/">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/tymoteusz-burak
    </a>]

.right-column50[.center[
<img
src="/remark-templates/3mdeb-presentation-template/images/tymek_burak.png"
width="150px" style="marking-top:-50px">

Daniil Klimuk

_Junior Embedded Systems Developer_]
Normal vs Secure Worlds
- <a href="mailto:daniil.klimuk@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    daniil.klimuk@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/daniil-klimuk-9358a1271/">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/daniil-klimuk-9358a1271/
    </a>
  ]

---

# Who we are ?

.center[
.image-15[![](/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/lvfs.png)]
.image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)] ]

.left-column50[

<img src="/remark-templates/3mdeb-presentation-template/images/openpower.svg"
    width="200px" style="margin-left:120px"> ]

.right-column50[ <img src="/img/crosscon_logo.svg" width="200px"
style="margin-left:40px; margin-top:40px"> ]

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

- What is Trusted Execution Environment?
  + Normal World vs Secure World
    - Different architecture overview
  + Root of trust
  + TEE use cases
    + Secure storage
- Integrating TEE solutions with Yocto:
  + Current Yocto community support
- Outro and sources

---

# What is Trusted Execution Environment?

.center[ <img src="/img/TEE_cpu_visual.svg" height="250px"> ]

_A secure area of a main processor that guarantees that the code and data loaded
inside are protected with respect to confidentiality and integrity._

???

- This is more of an overview to visualize the basic gist as implementations
vary from architecture to architecture each having it's own caveats
- According to Confidential Computing Consortium TEE provides a level of
assurance of
    - Data integrity
        - preventing unauthorized entities from altering data when data is being
        processed
    - Data confidentiality
        - unauthorized entities cannot view data while it is in use within the
        TEE
    - Code integrity
        - the code in the TEE cannot be replaced or modified by unauthorized
        entities
- Also called Confidential Computing
    - TODO elaborate, there's a difference
- TEE provides a level of protection against software attacks generated from the
normal execution environment
    - Also assists in protecting against hardware attacks.
        - TODO elaborate

---

# Normal vs Secure Worlds - Arm Cortex-A

.center[ <img src="/img/TEE_ARM_Cortex-a.svg" height="250px"> ]

???

- Arm TrustZone
- High-level overview
    - Trusted Applications are also protected from each other

---

# Normal vs Secure Worlds - Arm Cortex-M

.center[ <img src="/img/TEE_ARM_Cortex-m.svg" height="250px"> ]

---

# Normal vs Secure Worlds - x86

???

- TODO (briefly)

---

# Normal vs Secure Worlds - RISC-V

???

- TODO (briefly)

---

# Secure Storage vs fTPM

### TPM

<img src="/img/tpm_ftpm_tee_driver1.svg" height="79px">

### fTPM

<img src="/img/tpm_ftpm_tee_driver3.svg" height="130px" style="margin-top:-25px">

### fTPM as TA

<img src="/img/tpm_ftpm_tee_driver3.svg" height="130px" style="margin-top:-25px">

---
