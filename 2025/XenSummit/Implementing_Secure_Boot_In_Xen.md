# Kudos

* Michał Iwanicki

---

# Agenda

<!--

This talk will explore challenges and proposed strategies for implementing UEFI
Secure Boot within Xen and downstream distributions like XCP-ng or Qubes OS,
focusing on how these changes can enhance security and contribute to a more
unified framework for future development.

We will begin by examining why UEFI Secure Boot is essential in continuing the
transitive chain established by the modern static root of trust, and its
synergy with TrenchBoot and DRTM technology. We will delve into the
implications of the UEFI Secure Boot process, showing why simply signing
bootloaders and hypervisor binaries is insufficient; a comprehensive
implementation must address the entire boot chain.

Throughout the presentation, we will navigate the technical complexities of
effectively integrating UEFI Secure Boot in Xen. Some obstacles include:

- Support for SBAT: We will discuss the mandated adoption of SBAT for signing
Xen code and the prerequisite implementation of NX_COMPAT, which is critical
for UEFI Secure Boot compatibility.

- Kexec and Livepatching: the necessity for integrity checks using SHA256
during kexec operations and the requirement for signature verification for live
patches.

- Command Line Handling: how command-line parameters can introduce
vulnerabilities unless carefully managed, which must be resolved for an
implementation that can maintain a chain of trust.

- Memory Layout Compatibility: challenges presented by PE file formats and
their interactions with Xen's memory layout demands.

Community input is critical to ensure that the proposed changes align with
practical use cases and user requirements.  We will articulate a potential
roadmap for progressing toward full UEFI Secure Boot support in Xen, with
collaborative development and user requirements guiding change. By elucidating
the roadmap, we aim to motivate stakeholders to engage in dialogue prioritizing
secure launch technologies as essential components of a modern virtualization
strategy.

-->

---

# Previous work

<!--

* Secure Boot in Xen 2019
  * https://archive.fosdem.org/2019/schedule/event/vai_implementing_uefi_variable_services_in_qemu/attachments/slides/2972/export/events/attachments/vai_implementing_uefi_variable_services_in_qemu/slides/2972/fosdem.pdf
   * https://www.youtube.com/watch?v=jiR8khaECEk
* Vates UEFI SB in Xen Guests
  * https://www.youtube.com/watch?v=A_IhKjK7EgA

-->

---

# Start with why

<!--

* I should not need to lower my hardware and firmware security posture to
install Qubes OS, xcp-ng or any other Xen derivative.
* If you are susceptible to attacks that can compromise UEFI Secure Boot or any
other component in chain of trust your problem is bigger, that's why maybe it
doesn't make sense to take care of chain of trust protection if you don't have
correct countermeasure of physical attacks.
* What about bootkits? Maybe correctly set chain of trust at least can help
protecting against bootkits.
  - how bootkits are deployed? - through update, through vulnerabilities in
  "value-added" BIOS components, vulnerabilities in BIOS services and drivers?
* Maybe one of the problems is that Xen is deployed in "someone-else"
datacenters on bare metal?
* Why nobody care in Xen Community care about UEFI SB?

-->

---

# Current state

<center><img src="/2025/XenSummit/xenserver_sb_not_suppported.png"></center>


<!--

* XCP-ng:
  - https://github.com/xcp-ng/xcp/issues/294
* Qubes OS:
  - https://github.com/QubesOS/qubes-issues/issues/8206
  - https://github.com/QubesOS/qubes-issues/issues/4371
* There are some other commercial versions of Xen

-->

---

# What is Chain of Trust?

---

# Chain of Trust

* Modern computers Chain of Trust

<!--

* UEFI Secure Boot is as good as its own mechanisms and transitive trust on which
  it relies on.
* There is a lot of turtles all the way down. We will not be able to deal with
  all of those.
* Claims:
  - depending on your threat model you can be better on handling all keys
    yourself instead of relying on ecosystem
  - major obstacle for that is tooling

* UEFI Secure Boot tooling like sbctl does not work with Xen, but should

-->

---

# UEFI Secure Boot

<center><img src="/img/ds08msa_uefi_rot_and_cot_00.png"></center>

<!--
Basic overview of UEFI Secure Boot
Maybe add basic Secure Boot workflow when using bootloader e.g. GRUB, notes
about signature verifier protocols and security consideration in bootloader e.g.
GRUB module signing (or disallowing insmod), locking GRUB console when SB is
enabled to disallow changing boot commands

This view is definitely too simplified, we have to consider Xen distributions
and target market for it. Let's tackle it one by one and verify what are the
most common boot paths for those market segments:

### Server

Question is what datacenters use, how big deployments Xen have,
based on fact that Amazon use Xen deployment base can be really bit.

This space is extensive from OCP servers to SOHO setup with 1-2U. It is
possible to find representative examples of how those devices boot, but finding
most popular in rankings and maybe map that to standards (OCP) or simply read
manuals which can give a hint.

It seem that very popular solutions are:
- RoT in BMC and then BMC control hand over to CPU
  - then we can have Intel PFR here
  - there is AMD PSB here, but it has bad reputation
  - RoT in BMC make sense since AST2600, because earlier versions didn't have OTP memory
  - then going further there can be DC-SCM (Datacenter Secure Control Module) based on OCP specification: 
    - there could be lecture just about that one, but it seem to be most advanced
    and polished design, modular and mature in concept, what is most important it
    is open
      - but the point of this presentation is not exploration of all possible RoT and
      how platform can be boot, but presenting plethora of approaches showing strong
      sides and explaining that delegating security to vendor could be cost-saving
      but ignorant approach, which may lead to not comprehensively covered boot chain
      security

### Client? - this seem to be only Qubes OS, where laptops dominating market,
with small share of workstations

### Embedded - there is extensive space here, on one side it can be SOHO and
homelabs, on the other side there is huge automotive market

-->

---

# Threats

<!--

What threats are we subject to?
- here we should briefly analyze what we can be afraid of
- boothole - manipulation of config file leading to overflow, which breaks
chain of trust giving attacker control over it leading to compromise of further
components in chain of trust
- probably bigger headache are speculative attacks, rowhammer and similar,
because those can be performed remotely
- bootkitty
- black lotus - which is really boothole but for windows based solutions
- CVE-2024-7344 - this vulnerability prove that many vendors include
value-added utilities which are insufficiently validated
- Those are threats against UEFI Secure Boot, but there are also threats
against other components in the system like: ME, BMC and potentially more.
- Other issue is that MSFT and UEFI Forum are centralized authorities to deal
with vulnerabilities, relying always on those players may be insufficient in
some cases


Future ideas:
- discuss PI 1.9 and signed FV

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
https://youtu.be/cJyX6FLK4iU?feature=shared&t=813

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

https://xenbits.xen.org/docs/unstable/misc/kexec_and_kdump.txt

- integrity check
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

From June 2024 community call:
- purgatory can't be past userspace becase it violates security boundary of host
SB
- Linux - implemented purgatory themselves

-->

---

# Livepatching

<!--
Describe why it is needed, how the support is going, what will need to be
done.

>     Check signature on livepatches
> Live patches require signatures, while Kxec is more complicated due to user-space code.

https://www.redhat.com/en/topics/linux/what-is-linux-kernel-live-patching
https://docs.kernel.org/livepatch/livepatch.html
https://xenbits.xen.org/docs/unstable/misc/livepatch.html
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

From Community call:
- Requirement from Microsoft - no pointer can be used unchecked
- that translates to deleting priv(?) command
- a lot of work needed
-->

---

# Other

<!-- Anything else? If so then add -->

---

# Roadmap

<!-- Create roadmap for implementing Secure Boot support in Xen -->

---

# Official Microsoft process

<!--

* Revise Qubes OS Summit 2024 materials and get through shim review documentation
as well as current state for Qubes OS.
* Explain what is really involved.
* Is there any hypervisor signed already?

-->

---

# Sales pitch

<!--

What we can propose to accelerate resolution of described problems?
- we don't have enough resources to do big ecosystem changes,
- that's why we mostly focus on education and fixed price consultation,
- to provide something for community we work with OST2 to provide free of
charge, open access training materials related to coreboot, UEFI and low level
security, it is not only about us because there are lot of world-class experts
teaching those things at that platform
- if you looking for introducing UEFI SB in your organizations

-->
