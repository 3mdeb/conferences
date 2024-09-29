---
layout: cover
background: /intro.png
class: text-center
routeAlias: implementing-uefi

---

## Implementing UEFI Secure Boot in Qubes OS

### Challenges and Future Steps

<br>

## Piotr Król
<!--

This talk addresses both the technical and procedural aspects and aims to
provide a comprehensive roadmap for achieving UEFI Secure Boot support in Qubes
OS, ultimately paving the way for a more secure and resilient operating system.

-->

---

# Kudos

* Kamil Aronowski
* Marek Marczykowski-Górecki
* Andrew Cooper

---

# Goals
* Briefly explain what is UEFI Secure Boot and what led to OSS dislike of it.
* Justify that only valid way of use of UEFI Secure Boot was defined by Trammel Hudson
in [safeboot project](https://safeboot.dev/).
  - Anything else are just excuses, which waste resources.

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_09.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_08.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_07.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_06.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_05.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_04.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_03.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_02.png"/>

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_01.png"/>

<!--

Chain of Trust between DXE and BDS, BDS is just specialized DXE module, is
something to consider, because despite whole infrastructure for enforcing image
authentication exist at this point.

First there is no image verification if UEFI Secure Boot is not set, that is
obvious.

It seem to not be used in reference implementation. It is little bit different
for each image, but we will look on the policy right after next slide.

-->

---
transition: fade

---

<img src="/2024/QubesOSsummit/uefi_rot_and_cot/ds08msa_uefi_rot_and_cot_00.png"/>

<!-- 

A bootloader is an option. In reality, it is a UEFI Image (PE file) called by
UEFI Specification OS Loader. Recently popularity gain boot chain without
Bootloader/OS Loader, or rather built-in OS kernel. Both are visible to UEFI as
PE file and treated as UEFI Image.

-->

---

```c {*}{maxHeight:'100px'}
  switch (GetImageType (File)) {
    case IMAGE_FROM_FV:
      Policy = ALWAYS_EXECUTE;
      break;

    case IMAGE_FROM_OPTION_ROM:
      Policy = PcdGet32 (PcdOptionRomImageVerificationPolicy);
      break;

    case IMAGE_FROM_REMOVABLE_MEDIA:
      Policy = PcdGet32 (PcdRemovableMediaImageVerificationPolicy);
      break;

    case IMAGE_FROM_FIXED_MEDIA:
      Policy = PcdGet32 (PcdFixedMediaImageVerificationPolicy);
      break;

    default:
      Policy = DENY_EXECUTE_ON_SECURITY_VIOLATION;
      break;
  }
```

Policies:
`ALWAYS_EXECUTE`,`NEVER_EXECUTE`,`ALLOW_EXECUTE_ON_SECURITY_VIOLATION`,`DEFER_EXECUTE_ON_SECURITY_VIOLATION`,`DENY_EXECUTE_ON_SECURITY_VIOLATION`,
`QUERY_USER_EXECUTE_ON_SECURITY_VIOLATION`.

<!--

OptionROM policy is important because malicious VM with passed-through GPU
could do the OptionROM update, which without signature verification can
undermine security of whole platform.

-->

---

# UEFI Secure Boot

UEFI Secure Boot has emerged as a critical feature to protect systems against
persistent firmware attacks and unauthorized code execution. While Qubes OS is
renowned for its security-centric approach, the official support for UEFI
Secure Boot remains a significant milestone yet to be fully realized.

UEFI Secure Boot is really Chain of Trust technology, which covers very
specific part of x86 UEFI compliant boot process.

By default it covers only transition between UEFI BIOS and OS Loader/OS Kernel.
Verification of components coming from Firmware Volume, OptionROMs, drivers
from external media or internally connected are verified only if correct policy
is set by UEFI BIOS vendor.

<!--

Correctly configured UEFI Secure Boot is not enough to protectli platform,
there have to be root of trust behind, but is another can of worms.

-->

---

<center><img src="/2024/QubesOSsummit/pk_kek_role.png" width="450"/></center>

<!--

UEFI Secure Boot keys and db role

-->

---

# UEFI Secure Boot and Linux

* Microsoft became a holder of of keys for UEFI CA
  - nobody else had infrastructure (Microsoft already signed OS drivers),
  - nobody else had/wanted to put resources in the process,
* Microsoft to provide certification mandates among OEM inclusion of one their
certificates in KEK database and two in DB (MSFT PCA, UEFI CA).
* UEFI CA is the certificate which signs non-Microsoft software.

<!--

- Current Limitations and User Impact: Understanding why Secure Boot is not
currently supported and the implications for users, particularly those needing
dual-boot environments.

-->

---

# UEFI Secure Boot has bad press

* [PKfail (CVE-2024-8105)](https://www.cve.org/CVERecord?id=CVE-2024-8105)
  - Use of insecure PK generated by AMI for reference implmentation needs
* [UEFI Shell considered harmful (CVE-2024-7756)](https://www.cve.org/CVERecord?id=CVE-2024-7756)
  - If UEFI BIOS has UEFI Shell and attacker would be able to trigger it, then it can be leveraged for UEFI Secure Boot bypass thanks to `mm` tool (CWE-489: Active Debug Code).
* [BootHole](https://eclypsium.com/blog/theres-a-hole-in-the-boot/)
  - Multiple vulnerabilities in GRUB2 allowing to bypass UEFI Secure Boot.
  - Lack of revocation in shim lead to escalation of revocation to certificate
    from Microsoft to prevent shims that allow running vulnerable GRUB2.
* [Black Lotus](https://github.com/Wack0/CVE-2022-21894)
  - Bootkit using CVE-2022-21894 ("Baton Drop") to bypass UEFI Secure Boot.
  - > Windows Boot Applications allow the `truncatememory` setting to remove blocks of memory containing "persistent" ranges of serialised data from the memory map, leading to Secure Boot bypass.

<!--

Cryptographic verification of UEFI images was not broken, but those vulnerabilities.

-->

---

# The cure happen to be worse than the disease

* Microsoft effort for maintaining security properties of UEFI Secure Boot on
  certified hardware lead to requirements, which leads to many issues in OSS
  ecosystem. If it all was not bad design from the beginning.
  - [SBAT](https://github.com/rhboot/shim/blob/main/SBAT.md) (_Secure Boot
    Advanced Targeting_) was created to create revocation mechanism in shim,
  - All processes around signing are very bureaucratic.
  - shim community put together dedicated [review repo](https://github.com/rhboot/shim-review) and guidelines to simplify process of OSS community.
* Need for complex and non-standarized integration with HSMs.
* But we can see almost no one attack UEFI Secure Boot mechanism, not even
  implementation, but rather configuration or already authorized code.
  - Maybe we will get there.

<!--

* It looks like brave fighting with self-created problems.
  - even more, fighting using the same methods which caused problems upfront
* When we will realized something is wrong with the way we fighting?
- revocation doesn't make sense, DBX is evergrowing, on many systems space for
DBX was probably exhausted or will be exhausted soon,
- maintaining revocation list is also hard thing, you have to rely on UEFI
distributions or on your vendor, and we know there are various vendors with
various level of caring about security
- this is at least one reason to have only allow list, which consist only
current system owner signature
  - how stupid this is, we can manage passwords to our banks and creating systems
to simplify things in that space, but traction for UEFI SB management
simplification is non-existent
  - we can imagine system in which keys would be managed by TPM and protected by
user password

-->

---

# UEFI Secure Boot and Qubes OS

* Those are requirements for being signed by Microsoft, not for UEFI Secure
Boot a la'safeboot.
* First production-related
  [question](https://groups.google.com/g/qubes-users/c/vrzdJmPNzrE/m/MC4l9QTJBAAJ)
  coming from Wim Vervoorn (Eltan), Aug 2017.
* Effort started to be tracked in
  [#4371](https://github.com/QubesOS/qubes-issues/issues/4371) since Oct 2018.
* Trammell reported booting Qubes OS 4.1 with secure boot enable leveraginging
  unified `xen.efi` in Aug, 2020.
  - initial concerns: xen.efi reliability while loading other boot files,
    complexity of boot parameters modification
* Effort for signing boot images was requested by Marek in May 2023 in
  [#8206](https://github.com/QubesOS/qubes-issues/issues/8206).
* Qubes OS Summit 2023 we discussed inclusion of Qubes OS CA in Dasharo firmware.
* Frederic works on improving Qubes Builder v2 to include `pesign` for signing
  needs [PR #77](https://github.com/QubesOS/qubes-builderv2/pull/77).
* There is no easy way to use current installer (R4.2.3) and modify it for UEFI
  Secure Boot enabled booting.
* Current approach is to build unified `xen.efi` and sign it. Pre-built
    `xen.efi` binaries will be provided in R4.3.


<!--

Initial email thread gathered a lot of emotions, FUD, ideology etc.

Trammel effort led to:
- patches for supporting UEFI Secure Boot in Xen started landing upstream,
- safeboot project support was developed,

-->

---

# UEFI Secure Boot and Xen

* There is a lot in this can of worms.
* From discussion with Andrew:
  - Xen needs support for SBAT, which is not present yet.
  - NX_COMPAT is required for SBAT support.
  - kexec have to leverage SHA256 for checking integrity of executed images.
  - kexec purgatory code should be built-in Xen.
  - Livepatching have to check patches singatures.
  - Command line have to be correctly handled (some options may be not safe).
  - New hypercalls ABI for checking all passed pointers.
  - Some debug options should have ability to be disabled at compilations time: GDB stub.
* In summary "unsigned code can't make any unaudited reads/writes".
* Not everything affect Qubes OS.
  -  But ensuring Linux kernel lockdown mode is forced will belong to this tasks.

<!--

* xen.efi changes:
** Require SBAT support to be signed
** In turn, requires NX_COMPAT
* Kexec needs to sig-check purgatory and the target executable
** Easiest approach is to build purgatory into Xen
* Livepatching needs to sig-check the patch
* Command line handling
** Most options are probably safe, some are definitely not

TODO: Why Qubes OS is different?  What are the Xen challanges?
- NX bit
- relocation, tklangley `.reloc`?

- Andy: XenServer Host UEFI Secure Boot update
  - Microsoft mandates use of SBAT for signing Xen code.
  - Live patches require signatures, while Kxec is more complicated due to
user-space code.
  0 Purgatory runs in VM context, fully privileged, to ensure Xen’s signature.
  0 Integrity check on regions before loading to avoid rogue DMA corruption.
- XenServer Host UEFI Secure Boot update
  - Expected changes needed in Xen to support Secure Boot:
    - xen.efi metadata changes
      - Add SBAT support.  Contents to be provided by vendor
      - Support IMAGE_DLLCHARACTERISTICS_NX_COMPAT
    - Kexec
      - Embed purgatory in Xen (can’t be passed from tools)
        - Includes SHA256 for checking the integrity of the target image
      - Check signature on new kernel+initrd
    - Livepatches
      - Check signature on livepatches
    - Hypercalls
      - New ABI to check all pointers  (Discussed previously)

Notes from Andrew Cooper, mentioned by Trammel
[here](https://github.com/QubesOS/qubes-issues/issues/4371#issuecomment-682614795):

> Things like LIVEPATCH and KEXEC need compiling out, until they can be taught
> to verify signatures.
> Beyond that, things like the GDB serial stub probably need a way of being
> able to be compiled out, and then being compiled out. (This is definitely not
> an exhaustive list.) Xen's secureboot requirements also extend to the dom0
> kernel, due to the responsibility-sharing which currently exists. For a Linux
> dom0, Xen must ensure that lockdown mode is forced on (/dev/mem in dom0 still
> has a lot of system level power). At a minimum, this involves extending
> lockdown mode to prohibit the use of /{dev/proc}/xen/privcmd, which is still
> a trivial privilege escalation hole in PV Linux that noone seems to want to
> admit to and fix. I think it is great that work is being started in this
> direction, but there is a huge quantity of work to do before a downstream
> could plausibly put together a Xen system which honours the intent of
> SecureBoot. I know Safeboot has different goals/rules here, but whatever we
> put together called "Secure Boot support" will have to be compatible with
> Microsoft's model for it to be useful in the general case.

There is classical problem here which involve premise that either we doing
everything or nothing. So for examples there are issues with locking down Xen
and Dom0, but that seem to block having UEFI Secure Boot enabled to the point
of the lockdown.

Other issue is PE file format vs Xen requirements for memory layout.

This talk will explore the challenges and potential solutions for implementing
UEFI Secure Boot in Qubes OS.


> just signing bootloader and/or Xen isn't enough, and would result in
> something trivial to bypass (for example using kernel parameters).
- _marmarek_

> relying on Xen.efi is very unreliable depending on (...) UEFI implementation
> the requires File System Protocol Interface may be missing or unable to
> access those files (including limitation like ESP support, which on ISO9660
> is only 32MB)

> boot parameters modification is problematic, so in case boot failure
> troubleshooting/recovery may be very problematics
- this dev feature, regular user should never need that, we know thing work
differently, so maybe there should be better recovery mechanisms

- Technical Roadblocks: This section highlights technical challenges such as
signing GRUB and Xen binaries, managing key enrollments, and ensuring
compatibility across different hardware setups.

Let's say we have booted system, what is next?

-->

---

# What we can do right now?

* Choose hardware which has better UEFI Secure Boot Support
  - HP and some ACER BIOS implement ability to trust given file for execution,
  - not ideal but could be improved, especially by Dasharo Team, of course if
    there is consensus about security of such solution with Qubes OS Team,
* Wait for R4.3.
* Compile unified kernel yourself and try safeboot-like approach - this is what
  we will try.
* Disable UEFI Secure Boot

---

# It would not be end

* What are the capabilities which my system support?
- UEFI specificaition not defines what is supported,
- every implementation may do things little bit different,
- how to test that?
  - try
  - trust spec version compliance, which say something but not everything,


---

# Hackathon Challange

* Build unified xen.efi using qubes-builderv2
  - fix documentation?
* Test in OVMF

<!--

Short approach:
choose RSA-2048+SHA512

Generate bunch of various DER-encoded x.509 certificates and check which are
accepted by UEFI Secure Boot menu.

Hey! 8192 doesn't make sense it is too computationally expensive:
- who cares I'm doing that very rarely
- ECC is not supported

PK enrolling test results on edk2-202408 OVMF
- RSA < 2048 would not work.
- RSA 2048 SHA256/384/512 PASS (112 bits of symmetric key security)
- RSA 4096 SHA256/384/512 PASS (140 bits)
- RSA 8192 SHA256/384/512 PASS (192 bits)

Let's try to run:
- RSA8192 SHA512 signed HelloWorld.efi PASS

Experiment:
- copy content of Qubes OS R4.2.3-rc1 EFI partition to disk and see if it boots
without SB, and not boot with SB
- if yes, sign it with 8k-SHA512 key and check it if it boots

Above works very well, but, when trying to test media and install I get:

```shell
error: shim_lock protocol not found.
error: you need to load the kernel first.
error: you need to load the kernel first.

Press any key to continue...
```
-->

---
layout: cover
background: /intro.png
class: text-center

---

# Q&A

---
layout: cover
background: /intro.png
class: text-center

---

# Backup

---

# What could be done differently?

* Improve reference UEFI BIOS implementation to make dealing with UEFI Secure
  Boot manageable by mare mortals.
* Provide system level tooling as part of OS installation process.
  - Many distro doing that since those cannot afford fullfilling requirements for review process.
