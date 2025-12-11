---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## The Future of Platform Security Measurement in Linux

Linux Plumbers Conference 2025

---

# $ whoami

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="/slides/img/macpijan.png" style="width: 100px; border-radius: 50%;"
    alt="Profile Picture">
  <div>
    <b style="font-size: 1.5em;">Maciej Pijanowski</b><br>
    <i style="font-size: 1.2em;">Engineering Manager</i>
  </div>
</div>

<div style="display: flex; justify-content: space-between; align-items: center;
 font-size: 1.2em;">
  <div>
    🔑 <code>A766 C895 6989 5C0B 86D5  98D0 9963 C36A AC3B 2B46</code><br>
    ✉️ <a href="mailto:maciej.pijanowski@3mdeb.com">maciej.pijanowski@3mdeb.com</a><br>
    🐦 <a href="https://x.com/macpijan">@macpijan</a><br>
    🔗 <a href="https://www.linkedin.com/in/maciej-pijanowski-9868ab120">LinkedIn</a><br>
    🌐 <a href="https://www.3mdeb.com">3mdeb.com</a><br>
    💻 <a href="https://github.com/macpijan">GitHub</a><br>
  </div>
</div>

::: footer

<div style="color: black; font-size: 0.8em; text-align: center; margin-top: 20px;">
  Reach out for collaborations or inquiries!
</div>
:::

---

# Agenda

* Why should we care?
* Overview across ecosystem
* fwupd / HSI
* Problems and possible improvements

<!--
-->

---

# Why platform security measurement matters

* Firmware is the new attack surface
  - Runs before OS, OS security relies on it (e.g. UEFI Secure Boot)
* Complex security landscape
  - Dozens of complex security features, must be configured correctly
* User awareness gap
  - Users don't know how secure are their platforms
* Enterprise compliance
  - IT policies mandate specific security configurations

**There is a need for OS-enforced firmware quality assessment presenting simple
metrics to end user.**

<!--

**1. Firmware is the new attack surface**

* Runs before OS with highest privileges
* OS security relies on it (e.g. UEFI Secure Boot)
* Persistent across OS reinstalls

**2. Complex security landscape**

* Modern platforms: dozens of complex security features
* Intel Boot Guard, TPM 2.0, IOMMU, Memory Encryption, SPI Protections, ...
* Each must be configured correctly
* One misconfiguration = security gap

**3. User awareness gap**

* Users don't know these features exist and/or how they work
* No **easy** way to verify OEM enabled them
* "Is my platform actually secure?" ❓
* Users deserve transparency

**4. Enterprise compliance**

* IT policies mandate specific security configurations
* Manual verification doesn't scale
* There is a need for compliance tooling

The Solution: Automated, standardized platform security measurement This is why
HSI and similar tools are critical - they provide visibility and verification
that was previously impossible / difficult for end users.

-->

---

# Windows

<figure>
  <img src="/slides/img/windows_device_security.avif" width="550px">
</figure>

<!--

TBD: get up-to-date graphic from NovaCustom MTL release, update description below

Windows Security App → Device Security

Security Features Displayed:
- Security processor (TPM)
  + Status: enabled/disabled
- Secure boot
  + Status: on/off
- Core isolation (Memory Integrity)
  + Virtualization-based security
  + Toggle on/off with explanation
- Data encryption (BitLocker)
  + Status and management
- Hardware security capability

User Experience:
- Simple status indicators
- "Your device meets the requirements for standard hardware security"
- Click-through for details and settings

Windows focuses on clear pass/fail status with minimal technical details.
Emphasis on whether the device meets Microsoft's security baseline.

-->

---

# QubesOS

<figure>
  <img src="/slides/img/qos_sec_report.png" width="450px">
</figure>

<!--

TBD: get up-to-date graphic from NovaCustom MTL release

-->

---

# Linux (GNOME)

<figure>
  <img src="/slides/img/gnome_device_security_hsi.png" width="600px">
</figure>

<!--

TBD: get up-to-date graphic from NovaCustom MTL release

Screenshot shows: GNOME Settings Device Security panel with HSI security attributes

GNOME's approach provides detailed, technical information but makes it
accessible through clear visual indicators and actionable suggestions.

User Interface:
- HSI score: 0 (critically insecure) to 4 (very secure)
- Colorful large icons for immediate awareness
- List of security attributes with status
  + Green check: feature enabled/secure
  + Red cross: feature disabled/insecure
- Translated summary and description for each issue
- Suggested actions for fixing problems

Key Features:
- Integrated into GNOME Settings (gnome-control-center)
- Timeline showing when configuration changes occurred

Sources for screenshots:
- https://blogs.gnome.org/hughsie/files/2022/08/Screenshot-from-2022-08-24-12-08-47.png
- https://developers.redhat.com/sites/default/files/screenshot_from_2023-06-06_14-24-21_0.png

-->

---

# Linux (KDE)

<figure>
  <img src="/slides/img/firmware-security.png" width="700px">
</figure>

<!--

TBD: get up-to-date graphic from NovaCustom MTL release

-->

---

# What is fwupd?

* A tool for applying firmware updates from the Linux Vendor Firmware Service (LVFS)
* Beyond updates: evaluates system security through HSI scoring
* Presents users with automated security reports
* Users generate reports: `fwupdmgr security` or `fwupdtool security`

<figure style="display: flex; gap: 1px;">
  <img src="/slides/img/fwupd_logo.svg" width="250">
  <img src="/slides/img/lvfs_avatar.png" width="250">
</figure>

<!--
fwupd has become a critical tool in the Linux ecosystem, not just for firmware
updates but also for security assessment. It's widely adopted across major
distributions.
-->

---

# Host Security ID (HSI)

* A proposal of standardized metric to quantify platform security
* Developed by:
  - Richard Hughes (Red Hat)
  - Mario Limonciello (AMD)
  - Alex Bazhaniuk (Eclypsium)
  - Alex Matrosov (Binarly)
* **Important:** Specification is under active development
  - Incomplete, subject to change, may have errors
* https://fwupd.github.io/libfwupdplugin/hsi.html

<!--
-->

---

# HSI overview

Hierarchical framework with multiple levels

* **HSI-0:** HSI-1 requirements not met
* **HSI-1:** Least restrictive - non-permanent features
  - BIOS update capability, TPM presence, SPI write protection, UEFI Secure Boot
* **HSI-2:** Hardware-based firmware verification
  - "Fusing" - irreversible hardware changes enforcing firmware authorization
* **HSI-3:** Advanced protections
  - CPU control-flow integrity, DMA protection, low-power state requirements
* **HSI-4:** Memory protection
  - Supervisor Mode Access Prevention (SMAP), memory encryption
* **HSI-5:** Out-of-band attestation (planned, not yet implemented)

<!--
Notice the progression from basic to advanced security features. Each level
adds more sophisticated protections.
-->

---

# Inputs for HSI

fwupd uses several different interfaces to have an overview of platform's security

<style>
th {
  font-size: 1.1em !important;
  font-weight: bold !important;
}
td {
  font-size: 0.8em !important;
}
</style>

| Method | Interface | Tool/Path | Example Checks |
|--------|-----------|-----------|----------------|
| **sysfs (kernel)** 🟢 | sysfs | `/sys/class/`, `/sys/kernel/security/` | IOMMU, lockdown, TPM |
| **CPUID** 🟢 | instruction | Direct CPU instruction, `/proc/cpuinfo` | CET, TME support |
| **procfs** 🟢 | procfs | `/proc/sys/`, `/proc/cmdline`, `/proc/swaps` | Kernel tainted, swap |
| **ACPI Tables** 🟢 | sysfs | `/sys/firmware/acpi/tables/` | DMAR (DMA protection) |
| **EFI Variables** 🟢 | sysfs | `/sys/firmware/efi/efivars/` | SecureBoot, PK |
| **MSR** 🟡 | devfs | `/dev/cpu/0/msr` | Platform debugging (DCI), TME |
| **MTD** 🟡 | devfs | `/dev/mtd0` | Flash descriptor |
| **PCI Config Space** 🔴 | sysfs | `/sys/bus/pci/devices/.../config` | ME HFSTS (BootGuard), BCR (SPI) |

<!--

This table shows the diversity of hardware access methods fwupd uses for HSI
checks.

In this excericse we are trying to assign some colors indicating how well
certain interfaces are suitable right now for a userspace application.

We have interfaces like: ...

We will go through them in more details, focusing on the potential problems and
improvements.

🟢 **GREEN - Already good**:
🟡 **YELLOW - Works but could be improved**
🔴 **RED - Could use kernel API**

-->

---

# Proper user-space interfaces 🟢

* Sysfs
  - Read `/sys/class/tpm/tpm0/tpm_version_major` for TPM version
  - Read `/sys/power/mem_sleep` for available suspend modes
* ACPI tables
  - Read `/sys/firmware/acpi/tables/DMAR` and check DMA protection flag
* UEFI variables
  - Read `SecureBoot` EFI variable

---

# MSR 🟡

* Current flow
  - Open `/dev/cpu/0/msr`
  - Read buffer at register's offset (e.g. `IA32_DEBUG_INTERFACE`,
  `IA32_TME_ACTIVATION`)
  - Parse bit fields to inspect configuration (e.g. debug interface and memory
    encryption)
* Problems
  - Requires root permissions and `msr` kernel module
  - Low-level hardware knowledge in userspace (bit parsing)
* Possible improvements
  - Expose as sysfs entries for Intel CPUs as well
  - AMD exposes some security properties, e.g.:
    + `/sys/bus/pci/devices/<BDF>/debug_lock_on`
    + `/sys/bus/pci/devices/<BDF>/tsme_status`
    + [AMD PSP patchset](https://lore.kernel.org/lkml/20220329164117.1449-1-mario.limonciello@amd.com/)

---

# Parsing Intel Flash Descriptor (IFD) 🟡

* Current flow
  - Open `/dev/mtd0`
  - Parse IFD structure
  - Check if descriptor region is write-protected by parsing bit fields
* Problems
  - Requires root permissions
  - Parsing of low-level IFD structures
  - Multiple IFD layout versions have to be supported by the tool
  - Low-level hardware knowledge in userspace (bit parsing)
* Possible improvements
  - Parsing done once by kernel
  - Expose parsed IFD and access permissions as sysfs entries

---

# Parsing PCI config space (BCR) 🔴

* Current flow
  - Find Intel PCH device
  - Open `/sys/bus/pci/devices/<BDF>/config`
  - Read at offset `0xDC` (`BIOS_CNTL - BIOS Control Register`)
  - Parse bits
    + `Write Protect Disable`, `BIOS Lock Enable`, `SMM BIOS Write Protect`
* Problems
  - Low-level hardware knowledge in userspace (bit parsing)
* Possible improvements
  - Parsing done once by kernel
  - Expose flash security flags as sysfs entries

---

# Parsing PCI config space (ME) 🔴

* Current flow
  - Open `/sys/bus/pci/devices/0000:00:16.0/config`
  - Read 6 HFSTS registers at different offsets:
    + HFSTS1 at `0x40` - Manufacturing mode, operation mode
    + HFSTS2 at `0x48` - System state, error codes
    + HFSTS3 at `0x60` - Firmware SKU
    + HFSTS4 at `0x64` - Flash operation status
    + HFSTS5 at `0x68` - ACM (Authenticated Code Module) status
    + HFSTS6 at `0x6C` - BootGuard config, OTP fuse

---

# Parsing PCI config space (ME) 🔴 #2

* Problems
  - 6x 32-bit registers
  - Version-dependent layouts (CSME 11-17 vs 18+)
  - **Breaks when ME disabled** (false negatives - Intel Boot Guard still works)
* Possible improvements
  - Parsing done once by kernel
  - Expose ME and Intel Boot Guard configuration status in sysfs
  - AMD: `/sys/bus/pci/devices/<BDF>/fused_part`
    + reports whether the CPU has been fused to prevent tampering

---

# Going further: firmware security interface?

* Centralized security posture API
* Reusable across tools (not just fwupd)
* No need for root privileges to check security status
* Simplified implementation for userspace tools (vendor abstraction)
* A "similar" pattern already exists: `/sys/devices/system/cpu/vulnerabilities/`
  - translates low-level details into user-readable `PASS / FAIL` information
  - https://docs.kernel.org/admin-guide/hw-vuln/

<br>

```bash
cat /sys/devices/system/cpu/vulnerabilities/meltdown
Not affected
```

---

# Going further: firmware security interface?

```txt
/sys/firmware/security/
├── flash/
│   └── descriptor
│       ├── locked              # "0" or "1" - descriptor region write-locked
│       └── version             # "1", "2", or "3" - IFD version
├── srtm/                       # Vendor-agnostic HW RoT interface
│   ├── technology              # "bootguard", "psb", "trustzone", "secureboot"
│   ├── verified_boot/
│   │   ├── enabled             # 0 or 1
│   │   └── key_hash            # SHA256 of root public key
│   ├── vendor_specific/        # Vendor extensions
│   │   ├── intel_bootguard/
│   │   │   ├── acm_protected   # 0 or 1
│   │   │   └── btg_profile     # "production", "debug"
│   │   ├── amd_psb/
│   │   └── arm_xyz/
│   └── status                  # "active", "disabled", "not_provisioned"
├── drtm/                       # Vendor-agnostic HW RoT interface
```

Move (some of) the checks done by `fwupd HSI` into kernel?

<!--

Better Approach:
Kernel provides semantic interface:
  /sys/firmware/security/root_of_trust/verified_boot → "1"

Userspace doesn't need to know about HFSTS5, PSP registers, or TrustZone.
Just reads a boolean value with clear meaning.

This vendor-agnostic Hardware Root of Trust interface provides semantic meaning
instead of raw register bits.

Benefits:

- Safety
- Abstraction
- Caching
- Privilege separation
- Cross-platform consistency

Similar to Existing Patterns:
- /sys/devices/system/cpu/vulnerabilities/ - CPU security status
- /sys/firmware/efi/ - UEFI runtime info
- /sys/firmware/dmi/ - SMBIOS data
- /sys/class/tpm/tpm0/ - TPM interface
-->

---

# Going further: firmware security interface?

**Use Case**: Verify platform is using your Intel Boot Guard key

**Intel Boot Guard**:

```text
# Kernel reads Key Manifest from FIT
cat /sys/firmware/security/srtm/verified_boot/key_hash
a7f3d2c1b8e9... (your provisioned key hash)
```

**AMD Platform Secure Boot**:

```text
# Kernel queries PSP root key from fuses
cat /sys/firmware/security/srtm/verified_boot/key_hash
3c8d9f2e1a7b... (your provisioned key hash)
```

* Attestation: prove platform uses specific key
* Supply chain security: verify OEM provisioned correct key

<!--
Key Hash Exposure: Critical for Modern Security

Current Problem:
- Boot Guard Key Manifest is in SPI flash, complex to parse
- AMD PSP root key hash is in fuses (?), no standard interface
- ARM implementations vary wildly
- No way to (easily) verify which key is fused

-->

---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

# Q&A

---

# Parsing PCI config space (ME) 🔴 #3

<br>

**Example: Reading Intel Boot Guard OTP Fuse Status**

```c
const guint hfs_cfg_addrs[] = {0x0, 0x40, 0x48, 0x60, 0x64, 0x68, 0x6c}
```

```rust
struct FuMeiCsme18Hfsts6 {
    _reserved0: u21,                // bits 0-20: reserved/unused
    _manufacturing_lock: u1,        // bit 21
    _reserved1: u8,                 // bits 22-29: reserved
    fpf_soc_configuration_lock: u1, // bit 30: ⭐ OTP fuse lock status
    _sx_resume_type: u1,            // bit 31
}
```

```c
if (!fu_mei_csme18_hfsts6_get_fpf_soc_configuration_lock(hfsts6)) {
    // OTP fuse check FAILS -  user sees ❌ in HSI report
		fwupd_security_attr_set_result(attr, FWUPD_SECURITY_ATTR_RESULT_NOT_VALID);
		fwupd_security_attr_add_flag(attr, FWUPD_SECURITY_ATTR_FLAG_ACTION_CONTACT_OEM);
}
```

<!--

The current architecture has fwupd directly accessing hardware from userspace.
While this works, it has several limitations that a kernel-mediated approach
could solve.

**Problems**:
- Requires root privileges for raw hardware access
- Platform-specific knowledge scattered in userspace
- Breaks when vendors changes register layout (happens every few ME versions)
- Complex bit-level manipulation for every check
- No vendor abstraction - Intel/AMD/ARM all different

1. Userspace needs intimate hardware knowledge
2. Duplicated vendor knowledge
3. Maintenance burden
4. AMD is completely different
5. ARM is even more fragmented

-->

---

# Intel Boot Guard

* Hardware-based boot integrity protection
* Prevents the machine from running firmware images not released (signed) by
  the system vendor
* It forms a Root of Trust for Verification (RTV) and Static Root of Trust
  for Measurement (S-RTM) by fusing cryptographic keys into hardware

<!--

TBD: Extend  or drop?

https://edc.intel.com/content/www/us/en/design/ipla/software-development-platforms/client/platforms/alder-lake-desktop/12th-generation-intel-core-processors-datasheet-volume-1-of-2/010/boot-guard-technology/

-->

---
layout: two-cols-header
class: text-center
---

# Intel Boot Guard and Management Engine

::left::

<figure>
  <img src="/slides/img/hsi_me_enabled.png" width="300">
  <figcaption>ME enabled</figcaption>
</figure>

::right::

<figure>
  <img src="/slides/img/hsi_me_disabled.png" width="420">
  <figcaption>ME disabled</figcaption>
</figure>

<!--

Intel Boot Guard status reporting with disabled ME

* open-source firmware users typically prefers the ME to stay disabled
* If IBG is configured correctly, firmware is still verified on boot
* fwupd is lacking an interface to confirm this correct configuration

The HSI score is radically different.

In reality, the security posture is the same - or one could argue the one with
ME disabled is even better due to reduced attack surface.

References:
- https://github.com/Dasharo/dasharo-issues/issues/463
- https://github.com/fwupd/fwupd/issues/6011

-->

---

# Alternative ways of checking Intel Boot Guard configuration

ME HFSTS registers cached in SMBIOS

```text

Handle 0x0031, DMI type 219, 106 bytes
OEM-specific Type
	Header and Data:
		DB 6A 31 00 01 04 01 55 02 00 90 00 81 00 60 30
		00 00 00 00 00 00 00 03 1F D6 02 00 00 00 00 02
		00 00 00 80 00 00 00 00 00 00 00 00 00 00 00 00
		00 00 00 00 00 00 00 00 03 00 00 00 80 00 00 00
		00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
		00 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00
		00 00 00 00 00 00 00 00 00 00
	Strings:
		MEI1
		MEI2
		MEI3
		MEI4
```

See
[this issue](https://github.com/fwupd/fwupd/issues/6011#issuecomment-3631473485)
for details.

<!--

-->
