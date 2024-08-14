class: center, middle, intro

# Enabling coreboot on Talos II

### Open Source Firmware Conference 2024

## Krystian Hebel

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
  src="/remark-templates/3mdeb-presentation-template/images/your_name.png"
  width="150px" style="marking-top:-50px">
]

.center[Your Name]
.center[_Your Job Title_]
.right-column50[
- X years in 3mdeb
- Work experience
- interested in:
  - interest 1
  - interest 2
  - interest 3
]
.left-column50[
- <a href="https://twitter.com/YOUR_TWITTER">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @YOUR_TWITTER_
   </a>
- <a href="mailto:YOUR.NAME@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    YOUR.NAME@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/YOUR_LINKEDIN">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    linkedin.com/in/YOUR_LINKEDIN
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

* coreboot licensed service providers since 2016 and leadership participants
* UEFI Adopters since 2018
* Yocto Participants and Embedded Linux experts since 2019
* Official consultants for Linux Foundation fwupd/LVFS project since 2020
* IBM OpenPOWER Foundation members since 2020

---

# Agenda

* Why?
* Reset vector and thereabouts
* Debugging tools
* PPC64 ABI, decisions and assumptions
* Hardware
* Implementation
* Current state & TODOs
* Q&A

???

- why: coreboot is simpler than hostboot
- reset vector: SBE, SEEPROM, PNOR, initial state
- Debugging: BMC => pdbg, QEMU => monitor
- decisions & assumptions: BE
- hardware: how many cores in SoC
- implementation: easy and hard part
- current state: what works, what doesn't

---

# Why?

.left-column50[
### Hostboot

- C++, C, Python, Perl, XML
- **TBD** KLOC
- partially machine-generated
- PPC64 only
- OS:
  - user mode
  - virtual memory
  - dynamically loaded libraries
  - on-demand paging
- slow 🐢
]

.right-column50[
### coreboot

- mostly C
- **TBD** KLOC
- written by humans for humans
- x68, ARM, RISC-V, PPC64
- program:
  - supervisor mode
  - physical memory
  - static code<br>&nbsp;
  - everything fits in cache
- fast <img style="height:1em" src="/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png" />
]

---

# Why?

**TBD**: examples of initfiles

---

# Reset vector and thereabouts

**TBD**
- IPL diagram from https://wiki.raptorcs.com/w/images/b/bd/IPL-Flow-POWER9.pdf
- SBE, SEEPROM
  - SEEPROM I2C from BMC?
  - ECC
- PNOR with partition list
  - marked HB
  - ECC
- initial state, HRMOR, cache validity

---

# Debugging tools

**TBD**
- QEMU monitor
- BMC pdbg
- differences between QEMU and HW
- first attempts at bootblock

---

# PPC64 ABI, decisions and assumptions

**TBD**
- function descriptors
  - why sizes in `build/cbfs/fallback/*.map` are useless for PPC64
- BE:
  - why?
  - CBFS, FMAP, CBMEM
- reuse HB partitions
- little RAS - workstation
- skiboot in CBFS
- FDT
- Heads in PNOR (?)
- bonus: `eieio`, `darn`, `miso`

---

# Hardware

**TBD**
- Talos II vs Talos II Lite
  - SATA controller - not open
- https://en.wikipedia.org/wiki/POWER9#Chip_types
- Figure 23-3 from https://wiki.raptorcs.com/w/images/c/ce/POWER9_um_OpenPOWER_v21_10OCT2019_pub.pdf
  - OCC
  - no I/O PPE on Sforza
- Figure 2 from https://wiki.raptorcs.com/w/images/c/c7/POWER9_Registers_vol2_version1.2_pub.pdf
  - SCOM

---

# Implementation

**TBD**
- RAM init
  - https://github.com/3mdeb/openpower-coreboot-docs/tree/main/devnotes/isteps
  - don't buy JEDEC specs unless you need it
- SMP, HOMER, OCC
- RNG timeout - coreboot too fast
- non-technical issues:
  - lost XIVE documentation
  - https://lists.ozlabs.org/pipermail/openpower-firmware/2021-January/000611.html,
    https://lists.ozlabs.org/pipermail/openpower-firmware/2021-February/000628.html
  - platform moved to lab - full-speed CPU fan unnoticed because of that (Heads)

---

# Current state & TODOs

**TBD**

---

<br>
<br>
<br>

## .center[Q&A]
