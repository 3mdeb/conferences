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

- What is TEE/Secure Storage and what for?
  + Root of trust
  + TEE and its structure
  + TEE possibilities and use cases
- Integrating TEE solutions with Yocto

---
