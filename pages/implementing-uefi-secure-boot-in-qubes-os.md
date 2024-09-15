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

# UEFI Secure Boot

<!--

TODO: very brief intro to UEFI Secure Boot

UEFI Secure
Boot has emerged as a critical feature to protect systems against persistent
firmware attacks and unauthorized code execution. While Qubes OS is renowned
for its security-centric approach, the official support for UEFI Secure Boot
remains a significant milestone yet to be fully realized.

UEFI Secure Boot is really Chain of Trust technology, which covers very
specific part of x86 UEFI compliant boot process.

It covers only transition between UEFI BIOS and OS Loader/OS Kernel.

It also can cover DXE images (typically drivers) authentication although
reference implementation does not enable that. Despite providing all necessary
libraries to achieve the goal.

-->

---

# UEFI Secure Boot and Linux

<!--

- Current Limitations and User Impact: Understanding why Secure Boot is not
currently supported and the implications for users, particularly those needing
dual-boot environments.

-->

---

# UEFI Secure Boot and Xen
<!--

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

TODO: where to put various BIOSes approach: Dasharo, HP BIOS, QEMU
- ACER seem to have option "UEFI file trusted for execution" or sth like that

-->

---

# UEFI SB in Qubes OS

<!--

It all seem to start from Wim Vervoorn (Eltan)
[email](https://groups.google.com/g/qubes-users/c/vrzdJmPNzrE/m/MC4l9QTJBAAJ)
about building chain of trust in system using Qubes OS.
- thread gathered a lot of emotions, FUD, ideology etc.

-->

---

# Challenges

<!--

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

# Why we should care?

<!--

The ever-evolving landscape of cybersecurity demands robust mechanisms to
ensure the integrity and trustworthiness of computing environments.

- Security Enhancements and Benefits: Evaluate how Secure Boot can enhance
Qubes OS's overall security posture and protect against specific attack
vectors.

TODO: mention biggest SNAFU caused by UEFI Secure Boot and explain true reason
behind that.

-->

---

# What we can do?

<!--

TODO: explain possible paths for integration of UEFI Secure Boot
- how various distributions deal with the problem
- draw diagrams which show all those boot flows and provisioning procedures

- Proposed Solutions: This section discusses the steps proposed in issue #4371
to sign boot images with dedicated keys, build unified Xen boot images, and
make necessary GRUB configuration changes.

-->

---

# Tools

<!--

TODO: what tools we have to deal with
- sbsigntool family
- efitools family

-->

---

# Processes

<!--

Leveraging insights from ongoing discussions and issues like QubesOS Issue
#4371, we will explore the necessary system changes, from signing boot images
to configuring the system to accommodate Secure Boot's complexities.

-->

---

# Plans

<!--

- Roadmap and Community Involvement: Outlining the future steps towards full
Secure Boot support and how the community can participate in the ongoing
testing, feedback, and development efforts.

Marek's requirements June, 2018:
1. Binaries signed in a split-gpg compatible way
  - signing key shouldn't be exposed to build environment
2. Make sure kernel and initramfs also gets verified
  - how to do that when initramfs is dynamically generated?
  - what would be role of shim in this scheme?
3. xen and kernel command line are also verified

Reading this: https://ruderich.org/simon/notes/secure-boot-with-grub-and-signed-linux-and-initrd
- why initial loader (GRUB2) cannot be signed and then continue using GPG?

-->

---

# Extreme approach

* Trust only keys I personally control

<!--

What are the capabilities which my system support?
- UEFI specificaition clearly defines what is supported,
- every implementation may do things little bit different,
- how to test that?
  - practical test
  - trust spec version compliance

Why?
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

TODO: introduce UEFI revocation

Trammel already achieved this approach in 2020 with Qubes 4.1 under safeboot
project.

-->

---

# Evaluation

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
