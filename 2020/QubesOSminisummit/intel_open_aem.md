class: center, middle, intro

# Anti Evil Maid for Intel<br>coreboot-based platform

### Qubes OS and 3mdeb minisummit 2020

## Michał Żygowski

<img src="remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Agenda

* Introduction
* Anti Evil Maid
* AEM on Intel processors
* Qubes OS Anti-Evil-Maid
* Qubes OS Anti-Evil-Maid installation
* Qubes OS Anti-Evil-Maid troubleshooting
* Intel TXT status in coreboot
* Enabling Intel TXT on older hardware
* Q&A

---

# Introduction

.center[<img src="images/miczyg.png" width="220px" style="margin-top:-50px">]
.center[Michał Żygowski]
.center[_Firmware Engineer_]
.right-column50[
- Braswell SoC, PC Engines and Protectli maintainer in coreboot
- interested in:
  - advanced hardware and firmware features
  - coreboot
  - security solutions
]
.left-column50[
- <a href="https://twitter.com/_miczyg_"><img src="remark-templates/3mdeb-presentation-template/images/twitter.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @_miczyg_</a>

- <a href="mailto:michal.zygowski@3mdeb.com"><img src="remark-templates/3mdeb-presentation-template/images/email.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> michal.zygowski@3mdeb.com</a>

- <a href="https://www.linkedin.com/in/miczyg"><img src="remark-templates/3mdeb-presentation-template/images/linkedin.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> linkedin.com/in/miczyg</a>

- <a href="https://www.facebook.com/miczyg1395"><img src="remark-templates/3mdeb-presentation-template/images/facebook.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> facebook.com/miczyg1395</a>
]

---

# Anti Evil Maid

Protection by ensuring the state of the platform.

If we can trust the hardware and software we use, can we feel safe?

How to determine if the state of the platform is trusted and
hardware/firmware/software has not been tampered?

**Trusted Execution / Trusted Computing**:

- TPM module by TCG
- Intel TXT
- AMD Secure Launch with SKINIT

---

# AEM on Intel processors

**Intel TXT**:

- TPM required
- BIOS ACM and SINIT ACM required
- implementation: tboot, TrenchBoot
- BIOS needs to enable VT-x, VT-d, load BIOS ACM
- many GETSEC sub-instructions called leaf functions

---

# Qubes OS Anti-Evil-Maid

`sudo qubes-dom0-update anti-evil-maid`

Additional protection:

- multi-factor with AEM USB boot device and TOTP
- using 2 AEM USB sticks in case one could be stolen
- using non-default SRK password
- using additional secret key file for LUKS on AEM USB

Attack still not prevented:

- attacker can sniff passwords, keystrokes and access AEM USB stick
- fake motherboard injection with radio link
- successful measurement bypass by buggy CRTM implementations in BIOS
- buggy BIOS updates leading to BIOS compromise
- SMM attacks leading to Intel TXT compromise (can be prevented by STM)

.footnote[
https://www.qubes-os.org/doc/anti-evil-maid/

https://github.com/QubesOS/qubes-antievilmaid/blob/master/anti-evil-maid/README
]

---

# Qubes OS Anti-Evil-Maid installation

Reference hardware for this presentation:

- Dell OptiPlex 9010 SFF
- firmware: coreboot
- TPM 1.2
- Intel TXT supported
- CPU: Intel Core i7-3770 (Ivybridge)
- Chipset: Intel Q77 Express (PantherPoint)

---

# Qubes OS Anti-Evil-Maid installation

Following the procedure in [Anti-Evil-Maid README](https://github.com/QubesOS/qubes-antievilmaid/blob/master/README):

1. Enable TPM in BIOS. Also enable TXT if there is an option for it.
2. Install and Verify TPM support under your OS/Dom0:

  - Install anti-evil-maid packages (in Dom0 on Qubes). It will install all the
    required dependencies and tools: _**qubes-dom0-update anti-evil-maid**_
  - Verify kernel support for TPM: _**cat /sys/class/tpm/tpm0/pcrs**_
  - Initialize the TPM for use with AEM: _**anti-evil-maid-tpm-setup**_

3. Setup Anti Evil Maid:

  - Obtain SINIT module appropriate for your platform
  - Create an Anti Evil Maid device with _**anti-evil-maid-install**_

---

# Qubes OS Anti-Evil-Maid installation

&#52;. Reboot the system and test with AEM entry in GRUB:

  - Enter your SRK password if prompted
  - See your secret text or TOTP code (if set) displayed **before** you enter
    your LUKS disk encryption or key file passphrase

---

# Qubes OS Anti-Evil-Maid troubleshooting

First I have tried to enable AEM on original BIOS...

Problems:

- Had to juggle TPM BIOS options to get it cleared properly
- When QubesOS was launched with TBoot, TPM was not detected (broken memory
  map)
- my previous QubesOS setup was installed on NVMe SSD, but original BIOS does
  not support NVMe booting, so I had to reinstall Qubes OS for testing purposes

Solutions:

- **Implement open-source firmware support!** to workaround buggy BIOS
  implementations

---

# Intel TXT status in coreboot

Some time ago someone managed to implement Intel TXT support in coreboot...

9elements from Germany implemented Intel TXT support for Facebook:

- [https://review.coreboot.org/c/coreboot/+/37016](https://review.coreboot.org/c/coreboot/+/37016)
- ACM and silicon verification
- ramstage driver for TXT and ACM loading
- supports Haswell and newer machines (up to Kaby Lake)
- unfortunately no support for Ivybridge and older but a lot of code that could
  be reused

---

# Enabling Intel TXT on older hardware

Missing parts:

- No FIT table to load ACM before CPU reset so need other mechanism
- No pre-RAM support to load ACM to perform SCLEAN for memory controller unlock
- No SCHECK support for S3 resume
- Need to implement special SIPI vector in ROM for APs
- How to handle hyperthreaded CPUs?

---

# Enabling Intel TXT on older hardware

Where we are?

- Need to implement special SIPI vector in ROM for APs - **DONE**
- No pre-RAM support to load ACM to perform SCLEAN for memory controller unlock - **VERIFICATION**
- No SCHECK support for S3 resume - **WORK IN PROGRESS**
- How to handle hyperthreaded CPUs? - **???**

Currently we struggle with launching secondary processors to perform TXT
initialization, the machine hangs...

---

# Enabling Intel TXT on older hardware

Few logs:

```
TXT: ACM Version comparison mask: ffffffff
TXT: ACM Version numbers supported: 00000000
TXT: Max size of authenticated code execution area: 00010000
TXT: External memory types supported during AC mode: 00000303
TXT: Selective SENTER functionality control: ffc88900
TXT: TXT Feature Extensions Flags: 00000040
TXT:    S-CRTM Capability rooted in: BIOS
TXT:    Machine Check Register: preserved
TEE-TXT: Initializing TEE...
TXT-STS: ACM verification successful
TXT-STS: IBB not measured
TXT-STS: TXT is not disabled
TXT-STS: BIOS is not trusted
TEE-TXT: State of ACM and ucode update:
TEE-TXT: Chipset Key Hash 0x82d8c45fef2b9c992d4aef4104243773d1cb65033330d95d1d3d53f6fa1ffdb
TEE-TXT: DIDVID 0xb0018086
TEE-TXT: production fused chipset: false
```

---

# Enabling Intel TXT on older hardware

```
TEE-TXT: Validate TEE...
TEE-TXT: CPU supports SMX: true
TEE-TXT: CPU supports VMX: true
TEE-TXT: IA32_FEATURE_CONTROL
 VMXON in SMX enable: true
 VMXON outside SMX enable: true
 register is locked: true
 GETSEC (all instructions) is enabled: true
TEE-TXT: GETSEC[CAPABILITIES] returned:
 TXT capabable chipset present: true
 ENTERACCS available: true
 EXITAC available: true
 SENTER available: true
 SEXIT available: true
 PARAMETERS available: true
TEE-TXT: Machine Check Register: preserved
TEE-TXT: Hyperthreading capable CPU detected
TEE-TXT: Preparing 7 APs for TXT init
Setting up local APIC...
 apic_id: 0x00 done.
TEE-TXT: Asserting INIT
TEE-TXT: Sending first SIPI
(boot process hangs here...)
```

---

# Enabling Intel TXT on older hardware

Next steps:

1. Resolve INIT-SIPI-SIPI sequence issue for secondary cores initialization.
2. Secure the S3 resume path with SCHECK.
3. Get to know how to handle hyperthreading capable CPUs.
4. Last resort: reverse engineering.
5. **UPSTREAM CHANGES!**

---
class: center, middle, intro

# .center[Q&A]

---
class: center, middle, intro

# Thank you
