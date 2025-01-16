---
layout: cover
background: /intro.png
class: text-center
routeAlias: implementing-uefi

---

## Implementing UEFI Secure Boot in Xen and Qubes OS

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

<center><img src="/img/ds08msa_uefi_rot_and_cot_00.png" style="height: 400px; padding: 10px;"></center>

<!--
Basic overview of UEFI Secure Boot
Maybe add basic Secure Boot workflow when using bootloader e.g. GRUB, notes
about signature verifier protocols and security consideration in bootloader e.g.
GRUB module signing (or disallowing insmod), locking GRUB console when SB is
enabled to disallow changing boot commands
-->
---

# UEFI Secure Boot in Xen

<!--
What's different when using Xen, why can't Secure Boot be enabled by default
Check:
Community Call Oct 2019:
> Host Secureboot: no-one has followed on it - not clear on what exactly the problem is
Community Call: 13 June 2024:
> Andy: XenServer Host UEFI Secure Boot update
-->

---

# UKI

Building Unified Kernel Image allows image to be verified by UEFI verification
protocol which lowers needed security considerations

<!--
With UKI bootloader part could be skipped.
Built-in initrd, no need for separate verifier protocol in e.g. GRUB
(UEFI verifier works for EFI files (any others?))
-->

---

# Static Root of Trust

<!-- Describe basics of SRTM -->

---

# Dynamic Root of Trust

<!-- Describe basics of DRTM -->

---

# SRTM, DRTM & TrenchBoot

<!--
Describe synergy between SRTM, DRTM and TrenchBoot.
Can anything be taken from: https://trenchboot.org/dev-docs/Late_Launch_Overview/?
-->

---

# TrenchBoot & Xen

<!--
https://trenchboot.org/blueprints/Xen_Late_Launch/
-->

---

# Current state

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-7h26{color:#00E;text-align:left;text-decoration:underline;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-amwm" colspan="2">Xen-Version</th>
    <th class="tg-7h26"><a href="https://xenbits.xen.org/docs/unstable/SUPPORT.html">4.20-unstable</a></th>
    <th class="tg-7h26"><a href="https://xenbits.xen.org/docs/4.19-testing/SUPPORT.html">4.19</a></th>
    <th class="tg-7h26"><a href="https://xenbits.xen.org/docs/4.18-testing/SUPPORT.html">4.18</a></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-amwm" colspan="2">Initial-Release</td>
    <td class="tg-0lax">n/a</td>
    <td class="tg-0lax">2024-07-29</td>
    <td class="tg-0lax">2023-11-16</td>
  </tr>
  <tr>
    <td class="tg-amwm" rowspan="2">Host EFI Secure Boot</td>
    <td class="tg-amwm">x86</td>
    <td class="tg-0lax">Experimental</td>
    <td class="tg-0lax">Experimental</td>
    <td class="tg-0lax">Experimental</td>
  </tr>
  <tr>
    <td class="tg-amwm">Arm64</td>
    <td class="tg-0lax">Experimental</td>
    <td class="tg-0lax">Experimental</td>
    <td class="tg-0lax">Experimental</td>
  </tr>
</tbody></table>

<!--
Taken from https://xenbits.xen.org/docs/unstable/support-matrix.html
Describe experimental support, why it is/isn't enough
-->

---

# What needs to be done

- Xen needs support for SBAT, which is not present yet.
- NX_COMPAT is required for SBAT support.
- kexec have to leverage SHA256 for checking integrity of executed images.
- kexec purgatory code should be built-in Xen.
- Livepatching have to check patches signatures.
- Command line have to be correctly handled (some options may be not safe).
- New hypercalls ABI for checking all passed pointers.
- Some debug options should have ability to be disabled at compilations time:
GDB stub.

<!--
Taken from previous presentation, check if it's done already.
Check if there is anything new in https://github.com/QubesOS/qubes-issues/issues/8206
https://github.com/QubesOS/qubes-issues/issues/4371
-->

---

# SBAT

* TL;DR: better DBX but for shims, bootloaders and kernels
* SBAT (Secure Boot Advanced Targeting) introduces a structured metadata
  section in EFI binaries (like bootloaders and shims) that provides versioning
  information related to the binary.
* Metadata is added to the binary as part of a new section in the PE (Portable
  Executable) file called `.sbat`.
  * **Component Name** : Identifies what part of the boot chain the binary belongs to.
  * **Provider Name** : The organization or company that maintains the binary (e.g.,
    "shim").
  * **Component Generation** : Establishes the "generation" or version of the
    component to determine if it’s old or new.
  * **Vendor Name** : Identifies the vendor responsible for the binary (e.g.,
    "Red Hat").
  * **Version Information** : The specific version of the entity.
  * **Vendor URL** : A URL for further information (often related to security, vulnerabilities, or versioning).

---

# SBAT support

<!--
Describe why it is needed, how the support is going, what will need to be
done

From community call agenda:

> Add SBAT support.  Contents to be provided by vendor
> Microsoft mandates use of SBAT for signing Xen code.

Is it needed if using custom keys?
-->

---

# NX_COMPAT

<!--
Describe why it is needed, how the support is going, what will need to be
done
https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_optional_header32#IMAGE_DLLCHARACTERISTICS_NX_COMPAT
-->

---

# kexec SHA256 leverage

<!--
Describe why it is needed, how the support is going, what will need to be
done. Is it disabled? If yes then why?
-->

---

# kexec purgatory should be built-in

<!--
Describe why it is needed, how the support is going, what will need to be
done.
What's the current state?
https://github.com/torvalds/linux/blob/master/arch/x86/purgatory/purgatory.c#L44
needed only to verify sha256 checksum?

>     Embed purgatory in Xen (can’t be passed from tools)
        Includes SHA256 for checking the integrity of the target image
    Check signature on new kernel+initrd
> Purgatory runs in VM context, fully privileged, to ensure Xen’s signature.
-->

---

# Livepatching

<!--
Describe why it is needed, how the support is going, what will need to be
done.

>     Check signature on livepatches
> Live patches require signatures, while Kxec is more complicated due to user-space code.
-->

---

# Command line handling

<!--
Describe why it is needed, how the support is going, what will need to be
done.
Command line should be locked to disallow disabling security features e.g.
(check if it's relevant to Xen/QubesOS):

ima_appraise - disabling integrity measurements
lockdown - kernel lockdown feature
spec-ctrl - Controls for speculative execution sidechannel mitigations
-->

---

# New hypercalls ABI

<!--
Describe why it is needed, how the support is going, what will need to be
done.
-->

---

# Other

<!-- Anything else? If so then add -->

---

# Roadmap

<!-- Create roadmap for implementing Secure Boot support in Xen -->
