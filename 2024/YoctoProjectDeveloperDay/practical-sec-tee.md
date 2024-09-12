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

## Tymek

- What is TEE (2-4 slides)?
  + concept description
  + overview on different architectures
  + we focus on ARM Cortex-A
  + we mentiond briefly Intel, RISC-V. Intel
  + secure world vs non-secure world
- TEE API specififactions (1-2 slides)
  + focus Global Platform API
    - show that something liek this exist,s try to explain the purpose
- OPTEE - about + history
  + https://www.iwavesystems.com/product/op-tee-for-android-and-linux/
  + architecture, tee-supplicant
- optee - features overview (1 slide)
- fTPM - autopromotion + example of trusted service  (1 slide)
- optee secure storage (1 slide)
  + https://optee.readthedocs.io/en/latest/architecture/secure_storage.html

extras:
- What is Trusted Execution Environment?
  + Normal World vs Secure World
    - Different architecture overview
  + Root of trust
  + TEE use cases
    - Secure storage

## Daniil

- meme star wars
- optee support in Yocto (3 slides)
  + meta-arm - compilation from sources
  + problems with binaries provied by vendors
  + optee format (bin vs elf)
  + how other vendors provide/support optee (perhaps support matrix?)

- optee secure storage userland integration
  + https://optee.readthedocs.io/en/latest/building/userland_integration.html

- practical integration on RK3566 (3-4 slides)
  + adding optee to image
  + adding userspace components
- Zarhus integration
  + source code references
- bonus:
  + optee test suite integrtation

- Outro and sources

???

---

# What is Trusted Execution Environment?

.center[ <img src="/img/TEE_cpu_visual.svg" height="250px"> ]

<br>

_"Trusted Execution Environment (TEE) is a secure area in a device that ensures
sensitive data is stored, processed and protected in an isolated and trusted
environment."_

???

- Used to be "secure area of the main processor" but the definition has
broadened
    - Can even be a separate device, some "External Security SoC"
- A device can have multiple TEEs
- Mostly dependant on CPU architecture

---

# Different architectures - different approaches

- Guarantees the authenticity of the executed code.

- The confidentiality of its code, data and runtime states stored on a
persistent memory.

- Shall be able to provide remote attestation that proves its
trustworthiness for third-parties.

- Not hardware-dependant

---

# Coprocessor-based TEE

.left-column50[
.center[ 
<img src="/img/TEE_CPU_based.svg" height="200px" style="margin-left:-10px">
]
]

.right-column50[
.center[ 
<img src="/img/TEE_CoCPU_based.svg" height="200px" style="margin-right:-10px"> 
]
]

.center[ <img src="/img/TEE_SepCPU_based.svg" height="250px" style="margin-top:-10px"> ]

---


# Secure Storage

_Storage where confidentiality, integrity and freshness of stored data are
guaranteed, and where only authorized entities can access the data._

---

# Normal vs Secure Worlds - Arm

.left-column50[
<br>

### Arm Cortex-A

]

.right-column50[
<img src="/img/TEE_ARM_Cortex-a.svg" height="180px" style="margin-left:-120px; margin-top:-10px">
]

.left-column50[
<br>
<br>
<br>
<br>
<br>

### Arm Cortex-M

]

.right-column50[
<img src="/img/TEE_ARM_Cortex-m.svg" height="180px" style="margin-left:-17px">
]

???

- Arm TrustZone
- High-level overview
  + Trusted Applications are also protected from each other

---

# Normal vs Secure Worlds - Others

.center[ <img src="/img/TEE_ARM_Cortex-m.svg" height="250px"> ]

---

# Secure Storage vs fTPM

### TPM

<img src="/img/tpm_ftpm_tee_driver1.svg" height="55px">

### fTPM

<img src="/img/tpm_ftpm_tee_driver2.svg" height="55px">

### fTPM as TA

<img src="/img/tpm_ftpm_tee_driver3.svg" height="90px" style="margin-top:-25px">

???

- If you've heard of fTPM you might be wondering how does it differ
  + Without going into much detail fTPM can be thought as a software implementation of a TPM module
  + Normally it's implemented only in the firmware so the OS calls TPM and firmware is responsive for handling requests and security
  + Can be implemented in TEE thus offering better security and extended functionality
---

# Secure Storage vs fTPM - Shameless Plug

.center[

### For those interested more about fTPM's

[<img src="/img/FOSDEM_ftpm_ta_tee_blured.png" height="350px">
](https://fosdem.org/2024/schedule/event/fosdem-2024-3097-securing-embedded-systems-with-ftpm-implemented-as-trusted-application-in-tee/)
]

---

# Trusted Execution Environment (Secure OS) options

.pure-table[
| Company              | Product         | Hardware Used          | API Standard                  | Is Open-Source?       | Supported by Yocto? |
|----------------------|-----------------|------------------------|-------------------------------|-----------------------|---------------------|
| Alibaba              | Cloud Link TEE  | ?                      | GlobalPlatform                | ❌                    | ❌                  |
| Apple                | Secure Enclave  | Separate processor     | Proprietary                   | ❌                    | ❌                  |
| BeanPod              | ISEE            | ARM TrustZone          | GlobalPlatform                | ❌                    | ❌                  |
| Huawei               | iTrustee        | ARM TrustZone          | GlobalPlatform                | ❌                    | ❌                  |
| Google               | Trusty          | ARM / Intel            | Proprietary                   | Partially Open-Source | ❌                  |
| Linaro               | OPTEE           | ARM TrustZone          | GlobalPlatform                | ✔️                     | ✔️                   |
| ProvenRun            | ProvenCore      | ARM TrustZone          | ?                             | ❌                    | ❌                  |
| Qualcomm             | QTEE            | ARM TrustZone          | GlobalPlatform + Proprietary  | ❌                    | ❌                  |
| Samsung              | TEEgris         | ARM TrustZone          | GlobalPlatform                | ❌                    | ❌                  |
| TrustKernel          | T6              | Arm / Intel            | GlobalPlatform                | ? *                   | ❌                  |
| Trustonic            | Kinibi          | ARM TrustZone          | GlobalPlatform                | ❌                    | ❌                  |
| Open-TEE             | Open-TEE        | Emulation only         | GlobalPlatform                | ✔️                     | -                   |
]

.footnote[

Sources:

[wikipedia.org/Trusted_execution_environment](https://en.wikipedia.org/wiki/Trusted_execution_environment)

]

???

- Wikipedia also specifies a formally-validated static partitioning über eXtensible
Micro-Hypervisor Framework.
  + Segway into Crosscon HV

---

# Resources

<!-- markdownlint-disable-next-line MD013 -->

- ##### Mohamed Sabt, Mohammed Achemlal, Abdelmadjid Bouabdallah. Trusted Execution Environment: What It is, and What It is Not. 14th IEEE International Conference on Trust, Security and Privacy in Computing and Communications, Aug 2015, Helsinki, Finland. 10.1109/Trustcom.2015.357. hal-01246364

<!-- markdownlint-disable-next-line MD013 -->

- ##### Han, Seung-Kyun, and Jinsoo Jang. "MyTEE: Own the Trusted Execution Environment on Embedded Devices." NDSS. 2023. 

- ##### [What is a Trusted Execution Environment (TEE)? Past, Present & Future](https://www.youtube.com/watch?v=JHbq6lSey_Q)

- ##### Building Secure Firmware, Armoring the Foundation of the Platform - Jiewen Yao, Vincent Zimmer
