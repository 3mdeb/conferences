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
  <img src="/@fs/repo/img/macpijan.png" style="width: 100px; border-radius: 50%;"
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

* TBD

<!--
-->

---

# Why platform security measurement matters

<br>

**1. Firmware is the new attack surface**

* Runs before OS with highest privileges
* OS security relies on it (e.g. UEFI Secure Boot)
* Persistent across OS reinstalls

**2. Complex security landscape**

* Modern platforms: dozens of complex security features
* Intel Boot Guard, TPM 2.0, IOMMU, Memory Encryption, SPI Protections, ...
* Each must be configured correctly
* One misconfiguration = security gap

---

# Why platform security measurement matters

<br>

**3. User awareness gap**

* Users don't know these features exist and/or how they work
* No **easy** way to verify OEM enabled them
* "Is my platform actually secure?" ❓
* Users deserve transparency

**4. Enterprise compliance**

* IT policies mandate specific security configurations
* Manual verification doesn't scale
* There is a need for compliance tooling

<!--

The Solution: Automated, standardized platform security measurement This is why
HSI and similar tools are critical - they provide visibility and verification
that was previously impossible / difficult for end users.

-->

---

# Windows

<figure>
  <img src="/@fs/repo/img/qos_sec_report.png" width="450px">
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
  <img src="/@fs/repo/img/qos_sec_report.png" width="450px">
</figure>

<!--

TBD: get up-to-date graphic from NovaCustom MTL release

-->

---

# Linux (GNOME)

<figure>
  <img src="/@fs/repo/img/gnome_device_security_hsi.png" width="500px">
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
  <img src="/@fs/repo/img/firmware-security.png" width="500px">
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
  <img src="/@fs/repo/img/fwupd_logo.svg" width="250">
  <img src="/@fs/repo/img/lvfs_avatar.png" width="250">
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
  + Richard Hughes (Red Hat)
  + Mario Limonciello (AMD)
  + Alex Bazhaniuk (Eclypsium)
  + Alex Matrosov (Binarly)
* **Important:** Specification is under active development
  + Incomplete, subject to change, may have errors
* https://fwupd.github.io/libfwupdplugin/hsi.html

<!--
-->

---

# HSI overview

* Hierarchical framework with multiple levels
* Each level builds upon previous ones
* Cannot achieve higher level without meeting all lower level requirements
* Evaluates various security attributes
  + Firmware update mechanisms and integrity
  + TPM functionality and PCR measurements
  + Intel Boot Guard and measured boot
  + IOMMU and DMA protection
  + UEFI Secure Boot configuration
  + Memory encryption support
  + Control-flow enforcement technology

<!--
-->

---

# HSI overview #2

* **HSI-0:** HSI-1 requirements not met
* **HSI-1:** Least restrictive - non-permanent features
  + BIOS update capability, TPM presence, SPI write protection, Secure Boot
* **HSI-2:** Hardware-based firmware verification
  + "Fusing" - irreversible hardware changes enforcing firmware authorization
* **HSI-3:** Advanced protections
  + CPU control-flow integrity, DMA protection, low-power state requirements
* **HSI-4:** Memory protection
  + Supervisor Mode Access Prevention (SMAP), memory encryption
* **HSI-5:** Out-of-band attestation (planned, not yet implemented)

<!--
Notice the progression from basic to advanced security features. Each level
adds more sophisticated protections.
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

Intel Boot Guard status reporting with disabled ME

* open-source firmware users typically prefers the ME to stay disabled
* If IBG is configured correctly, firmware is still verified on boot
* fwupd is lacking an interface to confirm this correct configuration

::left::

<figure>
  <img src="/@fs/repo/img/hsi_me_enabled.png" width="200">
  <figcaption>ME enabled</figcaption>
</figure>

::right::

<figure>
  <img src="/@fs/repo/img/hsi_me_disabled.png" width="200">
  <figcaption>ME disabled</figcaption>
</figure>

<!--

The HSI score is radically different.

In reality, the security posture is the same - or one could argue the one with
ME disabled is even better due to reduced attack surface.

References:
- https://github.com/Dasharo/dasharo-issues/issues/463
- https://github.com/fwupd/fwupd/issues/6011

-->

---

# Intel Boot Guard and Management Engine

There are more HSI checks reading from ME PCI space

| HSI check | ME >=11 | ME >= 18 |
| :-- | :-- | :-- |
| <span style="color: red;">ME not in manufacturing mode</span> | <span style="color: red;">HFSTS1</span> | <span style="color: red;">HFSTS1</span> |
| <span style="color: green;">ME Flash Descriptor Override</span> | <span style="color: green;">HFSTS1</span> | <span style="color: green;">HFSTS1</span> |
| <span style="color: green;">Intel BootGuard: Enabled</span> | <span style="color: green;">HFSTS6</span> | <span style="color: green;">HFSTS5</span> |
| <span style="color: green;">Intel BootGuard: Verified</span> | <span style="color: green;">HFSTS6</span> | <span style="color: green;">N/A</span> |
| <span style="color: green;">Intel BootGuard: ACM</span> | <span style="color: green;">HFSTS6</span> | <span style="color: green;">HFSTS5</span> |
| <span style="color: green;">Intel BootGuard: Policy</span> | <span style="color: green;">HFSTS6</span> | <span style="color: green;">N/A</span> |
| <span style="color: red;">Intel BootGuard: OTP fuse</span> | <span style="color: red;">HFSTS6</span> | <span style="color: red;">HFSTS6</span> |

---

<!--

TBD: Only two of them are failing with ME disabled? Why? Can we really read out
some of the registers, but not all of them, even when ME is disabled?

-->

# Intel Boot Guard and Management Engine

Alternative ways of checking the failing checks

**ME not in manufacturing mode**
* check IFD is locked ?
  + cannot be done with kernel lockdown (UEFI Secure Boot) - opporunity for
  an in-kernel implementation?
* more ???

**Intel BootGuard: OTP fuse**
* ???

<!--

In our tests:
https://github.com/Dasharo/open-source-firmware-validation/blob/develop/dasharo-security/cbnt.robot#L179
we parse cbmem logs.

The logs are also filed in beased on the ME PCI HFSTS registers - the same (or
almost the same) as in fwupd checks:
https://github.com/Dasharo/coreboot/blob/dasharo/src/soc/intel/common/block/cse/cse_spec.c#L60

TBD: What is the state of these checks in our logs with ME disabled?

If we would propose to use cbmem, there are following challenges:
- relevant to coreboot-only devices (not a generic solution)
- cbmem access via /dev/mem is not ideal - it maye be usually restricted
- cbmem access via sysfs is somehow tied to Google devices and usually not
  available in distros?:
  https://github.com/torvalds/linux/blob/master/drivers/firmware/google/Kconfig

-->

---

# HSI complexity

Uses several different low-level interfaces to have an overview of platform's security

| Method | Interface | Tool/Path | Example Checks |
|--------|-----------|-----------|----------------|
| **PCI Config Space** | sysfs | `/sys/bus/pci/devices/.../config` | ME HFSTS (BootGuard), BCR (SPI) |
| **MSR** | devfs | `/dev/cpu/0/msr` | Platform debugging (DCI), TME, SMAP |
| **CPUID** | instruction | Direct CPU instruction | CET, SMAP, TME support |
| **sysfs (kernel)** | sysfs | `/sys/class/`, `/sys/kernel/security/` | IOMMU, lockdown, TPM |
| **procfs** | procfs | `/proc/sys/`, `/proc/cmdline`, `/proc/swaps` | Kernel tainted, swap |
| **ACPI Tables** | sysfs | `/sys/firmware/acpi/tables/` | DMAR (DMA protection) |
| **EFI Variables** | sysfs | `/sys/firmware/efi/efivars/` | SecureBoot, PK |
| **TPM sysfs** | sysfs | `/sys/kernel/security/tpm0/` | PCR values, eventlog |
| **PSP sysfs** (AMD) | sysfs | PSP device path | TSME, debug_lock_on |
| **MTD** | devfs | `/dev/mtd0` | Flash descriptor |

---

# HSI complexity

Requires registers / bit manipulation in userspace

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

# Firmware security interface?

**Generalized `/sys/firmware/security/` interface**

```txt
/sys/firmware/security/
├── srtm/                       # Vendor-agnostic HW RoT interface
│   ├── technology              # "bootguard", "psb", "trustzone", "secureboot"
│   ├── verified_boot/
│   │   ├── enabled             # 0 or 1
│   │   ├── enforced            # 0 or 1 (fail vs warn)
│   │   └── key_hash            # SHA256 of root public key
│   ├── vendor_specific/        # Vendor extensions
│   │   ├── intel_bootguard/
│   │   │   ├── acm_protected   # 0 or 1
│   │   │   └── btg_profile     # "production", "debug"
│   │   ├── amd_psb/
│   │   └── arm_xyz/
│   └── status                  # "active", "disabled", "not_provisioned"
├── drtm/                       # Vendor-agnostic HRoT interface
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

# Firmware security interface?

**Use Case**: Verify platform is using your Boot Guard key

**Intel Boot Guard**:
```bash
# Kernel reads Key Manifest from FIT, computes SHA256
cat /sys/firmware/security/srtm/verified_boot/key_hash
a7f3d2c1b8e9... (your provisioned key hash)
```

**AMD Platform Secure Boot**:
```bash
# Kernel queries PSP root key from fuses
cat /sys/firmware/security/srtm/verified_boot/key_hash
3c8d9f2e1a7b... (your PSP key hash)
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

# Going further: in-kernel HSI?

* Centralized security posture API
* Reusable across tools (not just fwupd)
* No need for root privileges to check security status
* Simplified implementation for userspace tools (vendor abstraction)
* A "similar" pattern already exists: `/sys/devices/system/cpu/vulnerabilities/`
  + translates low-level details into user-readable `PASS / FAIL` information
  + https://docs.kernel.org/admin-guide/hw-vuln/

<br>

```bash
cat /sys/devices/system/cpu/vulnerabilities/meltdown
Not affected
```

---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

# Q&A
