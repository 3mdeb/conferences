class: center, middle, intro

# TrenchBoot boot protocol for Xen in UEFI boot mode

### Xen Project Summit 2024

## Michał Żygowski

<img src="../../remark-templates/3mdeb-presentation-template/images/logo.png"
     width="150px" style="margin-left:-20px">

---

# Legacy multiboot2 path

<br>
<br>
<br>

.center[.image-99[![](/img/xen_tb_uefi_legacy_mb2.png)]]

---

# EFI multiboot2 path without EBS

<br>
<br>
<br>

.center[.image-99[![](/img/xen_tb_efi_mb2.png)]]

---

# EFI multiboot2 path with SLRT

.center[.image-90[![](/img/xen_tb_efi_mb2_slrt.png)]]

.footnote[
More details about SLRT on [trenchboot.org](https://trenchboot.org/specifications/Secure_Launch/)
]

---

# EFI PE path with SLRT

.center[.image-90[![](/img/xen_tb_uefi_pe_slrt.png)]]

.footnote[
More details about SLRT on [trenchboot.org](https://trenchboot.org/specifications/Secure_Launch/)
]
