# `$ whoami`

<center><img src="/piotr_krol.jpg" width="150px">
  <b>Piotr Król</b><br>
  <i>3mdeb Founder</i>
</center>

* Developing platform security technologies since 2008.
* Integrating open-source firmware and Trusted Computing technologies since
  2014.
* Delivering training and consulting services for commercial organizations and
  the public sector since 2018.
* [OpenSecurityTraining2](https://ost2.fyi/) Boards of Directors Member and
  Instructor.
* [TrenchBoot Project](https://trenchboot.org/) Steering Committee Core Member.
* Conference speaker, privacy, liberty, and trustworthy solutions advocate

---

# Kudos

* Michał Iwanicki
* Marek Marczykowski-Górecki
* Demi Marie Obenour

---

# Goals

* Explore challenges for implementing UEFI Secure Boot within Xen.
* Report current status and activity in downstream distributions.
* Build awareness about UEFI Secure Boot among developers, testers and
researchers.
* Explain risk associated with choosing narrow and centralized path while
securing boot process.
* Show instructions and small demo what can be achieved now.

---

## From Root of Trust to authenticated UEFI image

<br>
<center><img src="/2025/XenSummit/cot_w_uefi_sb.excalidraw.png"></center>
<br>

* Platform security for commercial off-the-shelf hardware starts with Static Root of
Trust for Verification (SRTV). Which typically consist of some secure storage
and code managing its lifecycle.
* RoT properties are pass through boot chain using transitive trust and
establishing Chain of Trust.
* **UEFI Secure Boot** is part of that chain, which establish trust between Platform Owner and firmware as well as between firmware and hypervisor and/or operating system.
* **UEFI Secure Boot** is part of the UEFI Specification and serves as a
**load-time authentication mechanism** for UEFI images (like bootloaders, OS
kernels, drivers and hypervisors).
* It ensures only trusted UEFI binaries signed with a recognized key can be
executed during the boot process.

<!--

[click]
* I assume most of you know at least roughly how UEFI Secure Boot works, but
for clarity let's spent a minute on explaining what UEFI Secure Boot is in
simple words.

[click]
It is important to mention that UEFI Secure Boot to manage its databases and
keys use UEFI Runtime Services exposed through SMM.

[click]
Key questions are:
* What is or should be behind hypervisor yellow rectangle?
* How and if hypervisor continue chain of trust to Guest VM?
* This is something we will explore further in this presentation.

-->

---

# Xen EFI boot

<!--

* Add diagram showing how Xen typically boots under UEFI.
* Add diagram how Linux boots typically with UEFI Secure Boot.
  - there are multiple options here
  - which one is the best?
* How hypothetically Xen boot path could look like?

-->

---

# Challenges

* Microsoft-signed shim Path
  - this path make sense only if software would be directly used on a large
  number of machines from multiple hardware vendors
  - this path generate the most issues, but it doesn't mean issues we see on this
  path should not be fixed for other paths, to keep bar high,
* DIY Path - adding your keys to UEFI Secure Boot database
  - by administrator on each installation,
  - by hardware and or firmware/vendor,
* Tooling
  - shim-review present a lot of challenges with handling keys (HSM), correct set of patches, build environment etc.
  - how to audit code to make sure it fulfills all requirements and there is no regression during further development,

<!--

Let's discuss what options we have to support Xen with UEFI Secure Boot enabled.

-->

---

<center>
  <div style="display: flex; flex-direction: column; align-items: center;">
    <div style="display: flex; justify-content: center;">
      <img src="/2025/XenSummit/pkfail.png" style="height:150px;object-fit:contain; margin:10px;">
      <img src="/2025/XenSummit/bootkitty_logo.png" style="height:150px;object-fit:contain; margin:10px;">
    </div>
    <div style="display: flex; justify-content: center;">
      <img src="/2025/XenSummit/cve-2024-7344.png" style="height:200px;object-fit:contain; margin:10px;">
      <img src="/2025/XenSummit/black_lotus.webp" style="height:200px;object-fit:contain; margin:10px;">
      <img src="/2025/XenSummit/boothole.png" style="height:200px;object-fit:contain; margin:10px;">
    </div>
  </div>
</center>

<!--

## Why UEFI Secure Boot matters for Xen ecosystem?

Some UEFI Secure Boot related vulnerabilities which maybe saw in social media.

-->

---

## Why UEFI Secure Boot matters for Xen ecosystem?

* It provides additional protection and mitigation against malicious code.
* I guess nobody wants new vulnerability marketing logo being associated with
their product.
* It help ensure compliance with standards and regulations.
  - We have quite a lot coming in EU in next 2 years (CRA/NIS2).
- Because need for disabling security features to install security-focused Xen
derivative bring bad vibe.
  - Currently users are advised to disable UEFI Secure Boot before installation.
* It may be required to not loose competitive advantage.
  - Some competing hypervisor already solved that problem.

<!--

What are the biggest threats to UEFI Secure Boot and why. To explain that we
have to dive little bit in history of vulnerabilities against UEFI Secure Boot.

By no means I'm expert regarding those topics and I'm pretty sure in this room
there are people who know and understand much more about the problem,
especially those who had to deal with with the mess.

-->

---

# 2020: BootHole

!!! quote

    Eclypsium researchers, Mickey Shkatov and Jesse Michael, have
    discovered a vulnerability — dubbed “BootHole” — in the GRUB2 bootloader
    utilized by most Linux systems that can be used to gain arbitrary code
    execution during the boot process, even when Secure Boot is enabled.

!!! quote

    The vulnerability is a buffer overflow that occurs in GRUB2 when parsing
    the grub.cfg file. This configuration file is an external file commonly
    located in the EFI System Partition and can therefore be modified by an
    attacker with administrator privileges without altering the integrity of
    the signed vendor shim and GRUB2 bootloader executables.

<small>

Source: [Eclypsium: There's a hole in the boot](https://eclypsium.com/wp-content/uploads/Theres-a-Hole-in-the-Boot.pdf)

</small>

<!--

Eventually it happen it was not one vulnerability but whole family.

-->

---
clicks: 2
---

* GRUB2 uses flex and bison to generate a parsing engine for a domain-specific
language (DSL) from language description files and helper functions.

```c {all|6-7}
#define YY_DO_BEFORE_ACTION \
    yyg->yytext_ptr = yy_bp; \
    yyleng = (int) (yy_cp - yy_bp); \
    yyg->yy_hold_char = *yy_cp; \
    *yy_cp = ‘\0’; \
    if ( yyleng >= YYLMAX ) \
                   YY_FATAL_ERROR( “token too large, exceeds YYLMAX” ); \
    yy_flex_strncpy( yytext, yyg->yytext_
                    ptr, yyleng + 1 , yyscanner); \
    yyg->yy_c_buf_p = yy_cp;
```

* GRUB2 implementation of the macro `YY_FATAL_ERROR`:

```c
#define YY_FATAL_ERROR(msg)            \
  do {                                 \
    grub_printf (_(“fatal error: %s\n”),
      _(msg));                           \
  } while (0)
```

<small>

Source: [Eclypsium: There's a hole in the boot](https://eclypsium.com/wp-content/uploads/Theres-a-Hole-in-the-Boot.pdf)

</small>
<!--

[click]
In this macro, the generated code detects that it has encountered a
token that is too large to fit into flex’s internal parse buffer and calls
YY_FATAL_ERROR(), which is a helper function provided by the
software that is using the flex-generated parser

[click]
Rather than halting execution or exiting, it just prints an error to the
console and returns to the calling function. Unfortunately, the flex code has
been written with the expectation that any calls to YY_FATAL_ERROR() will never
return. This results in yy_flex_strncpy() being called and copying the source
string from the configuration file into a buffer that is too small to contain
it.

-->

---

# Black Lotus

* CVE-2022-21894 is very similar to Boot Hole in a sense that it enables bypass thanks to playing with boot configuation. 
* Boot Configuration Data (BCD) contain special setting called `truncatememory`, which allow removing blocks of memory containing "persistent" ranges of serialised data from the memory map.
  - researchers were able to figure out that it is possible to remove serialised Secure Boot policy from memory map before it was read by boot application
  - that led to allow dangerous setting be used by boot application, because Secure Boot Policy was not found
* Normally Secure Boot Policy is not allocated in ranges which allow use of `truncatememory`, but researchers found corner case that Secure Boot Policy gets reallocated if `osdevice` setting is BitLocker-encrypted partition where Volume Master Key was derived using TPM.
  - This also is not that easy, but researchers were able to fake that through setting bit 0 of the key flags after TPM unsealing.

---

!!! bug

    Complex boot flow and extensive configurability create a lot of opportunities for adversaries to attack and researchers to earn their CVE.

* Mitigation of issues like Boot Hole or Black Lotus is very hard.
  - Despite revoking over 2000 hashes in revocation lists published by UEFI Forum
researchers were able to find not revoked version of `bootmgfw` in the wild and 
bypass fixes introduced in code as fix to CVE-2022-21894.
  - The results was CVE-2023-24932.
* Policy Overcomplexification through Reactive Risk Management
  * Those outliers/force majeure lead to redesign of Microsoft process for assesing and signing open-source components.

<!--

We should give tools to organizations and  people, so they can manage their own
keys. If someone feel that keys will be managed better by someone else it
should be concious choice, so in case of another force majeore, decision could
be changed. At this point we keep adding to centralized ecosystem and will
probably have to call for help from bigger and bigger entities to hold that
shield.

We already have some researchers calling for more centralized approach to UEFI Secure Boot revocation list distribution.

-->

---

<!--

What was said so far?
1. who we are
2. who contributed
3. what are our goals for this presentation
4. how modern system look like from perspective of UEFI Secure Boot and what is scope of UEFI Secure Boot
5. how Xen EFI boots in comparison to Linux with UEFI Secure Boot enabled paths, and how Xen UEFI Secure Boot path could look like
6. what are the challanges area to achieve Xen working with UEFI Secure Boot 
7. why UEFi Secure Boot matters for Xen ecosystem
  - this should be considered to move after point 4
8. force majeore and its general principles

* TODO:
  - 9. list of Xen challanges
  - 10. list of selected challanges which are result of analysis of Microsoft signing requirements

11. Current state in Xen

* TODO:
  12. Proposed solution based on UKI
    - with and without GRUB

13. Current state in downstream Xen distro

* TODO:
  14. Qubes OS and UEFI Secure Boot
  15. XCP-ng and UEFI Secure Boot
  16. Roadmap

-->

---

# What needs to be done

* Following coming from discussion with Andrew:
  - Xen needs support for SBAT, which is not present yet.
  - NX_COMPAT is required for SBAT support.
  - kexec have to leverage SHA256 for checking integrity of executed images.
  - kexec purgatory code should be built-in Xen.
  - Livepatching have to check patches signatures.
  - Command line have to be correctly handled (some options may be not safe).
  - New hypercalls ABI for checking all passed pointers.
  - Some debug options should have ability to be disabled at compilations time:
GDB stub.
* There are also concerns mentioned by Demi:
  - `/dev/xen/privcmd` since it allow root to overwrite dom0 kernel memory,
  - address space isolation, nested virtualization PVH dom0 and PV IOMMU

<!--

I'm not Xen hacker, so my understanding of those is limited, but for what I
know some of this positions are concerning because of potential for similar
UEFI Secure Boot bypass as in case of Boot Hole and Black Lotus, so abuse of certain configuration and creating special cases for bypass.

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

<!--
How Versioning Works:

Each version of the component includes the generation number  (a numeric field)
which acts as a "version counter." When a vulnerability is detected in a
particular version, an admin can revoke binaries of that specific generation,
ensuring that only trusted, newer versions are able to pass Secure Boot
validation checks. For example, if a vulnerability affects any version below
generation 10 of a bootloader, the system will block the execution of all
versions with a generation number below 10.


SBAT Revocation List (sbat_var) and DBX:

Revoking specific component generations happens by updating the SBAT revocation
list , stored in NVRAM (non-volatile memory) and referred to as sbat_var.
Additionally, the standard UEFI DBX (Database of Revoked Signatures) can also
be used in conjunction to revoke binaries based on hash/keys. The SBAT info of
binaries is compared against the sbat_var to ensure no revoked versions are
loaded during the boot process.

-->

---

# SBAT support

* It doesn't seem to be big issue and it is required during
[shim-review](https://github.com/rhboot/shim-review) as well as Microsoft
process.
* If one does not use shim revocation mechanism it does not add much value.

<!--

Whole topic is not that complex, most likely simple sctipt could succesfully
add `.sbat` section to already created uki xen images as part of Qubes OS and
XCP-ng testing.

TODO: try to add that section and see if it works.

-->

---

# NX_COMPAT

<!--

Describe why it is needed, how the support is going, what will need to be
done
https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_optional_header32#IMAGE_DLLCHARACTERISTICS_NX_COMPAT

https://techcommunity.microsoft.com/blog/hardwaredevcenter/new-uefi-ca-memory-mitigation-requirements-for-signing/3608714

Why it is needed? Does Xen not comply to that requirements?
How does Xen UKI comply with this requirement?

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

# Active Debug Code

* [CWE-389: Active Debug Code](https://cwe.mitre.org/data/definitions/489.html)

<!--

There is special class of Common Weakness called Active Debug Code, that was
found many time to be used for UEFI Secure Boot bypass.
- http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-34301
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-34303

> By exploiting the identified vulnerabilities, which can be automated with
> startup scripts, attackers can use the built-in capabilities of the shells,
> such as mapping memory, reading and writing to memory and listing handles, to
> evade Secure Boot and execute malicious code.

Xen seem to have some ability to enable debug code, in UEFi Secure Boot enabled
Xen those functionalities should be disabled to not create opportunity for
attackers.

-->

---

# /dev/xen/privcmd

<!--

Key question is about this suggestion from Demi and other she pointed.
Is there enough time to discuss it?

-->

---

<!--

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

# Selected Microsoft signing requirements


<!--

Some Microsoft requirements may pose additional challanges on top of mentioned above.

* Revise Qubes OS Summit 2024 materials and get through shim review documentation
as well as current state for Qubes OS.
* Explain what is really involved.
* Is there any hypervisor signed already?

-->

---

!!! quote

    Submitter must design and implement a strong revocation mechanism for
    everything the shim loads, directly and subsequently.

* This rise question which components would have to be verified.
* There is no similar software reviewed on shim-review repository.
* Xen is probably comparable to special case, as it was for iPXE Anywhere from 2Pint for which Microsoft published [Security Assurance Review](https://techcommunity.microsoft.com/blog/hardwaredevcenter/ipxe-security-assurance-review/1062943).

---

# Key takeaways from iPXE security assurance review

---

<center><img src="/2025/XenSummit/msft_revoc_mechanism.excalidraw.png" style="height:350px"></center>

<!--

Looking like some other cases 

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

# How does decode?

* Functional completeness: No
  * Does it behave like a fully functional feature? Does it work on all expected platforms, or does it only work for a very specific sub-case? Does it have a sensible UI, or do you have to have a deep understanding of the internals to get it to work properly?
* Functional stability: Here be dragons
  * Pretty likely to still crash / fail to work. Not recommended unless you like life on the bleeding edge.
* Interface stability: Not stable
  * Interface is still in the early stages and still fairly likely to be broken in future updates.
* Security supported: No
  * If “no”, anyone who finds a security-related bug in the feature will be advised to post it publicly to the Xen Project mailing lists (or contact another security response team, if a relevant one exists).


---

# UKI

Building Unified Kernel Image allows image to be verified by UEFI verification
protocol which lowers needed security considerations

* Or rather Unified Xen and Linux Kernels, and dom0 initiramfs Signed Images

<!--
With UKI bootloader part could be skipped.
Built-in initrd, no need for separate verifier protocol in e.g. GRUB
(UEFI verifier works for EFI files (any others?))
-->

---

# Xen UKI boot flow

<!--
Basic overview of Xen UEFI Secure Boot with shim and GRUB.

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
https://youtu.be/cJyX6FLK4iU?feature=shared&t=813

-->

---

# SRTM, DRTM & TrenchBoot

<!--

Describe synergy between SRTM, DRTM and TrenchBoot.
Can anything be taken from: 
- https://trenchboot.org/dev-docs/Late_Launch_Overview/?
- https://trenchboot.org/blueprints/Xen_Late_Launch/

-->
---

# Current state

<center><img src="/2025/XenSummit/xenserver_sb_not_suppported.png"></center>

* XCP-ng:
  - https://github.com/xcp-ng/xcp/issues/294, issue created in 2019
* Qubes OS:
  - https://github.com/QubesOS/qubes-issues/issues/4371, 2018
  - https://github.com/QubesOS/qubes-issues/issues/8206, 2023
* There are some other commercial versions of Xen

<!--

Read one more time all those issues content to make sure you get all niuances.

Mention Trammel and tklengyel PoC and fact that what we presenting here is not
much new despite being closer to final implementation.

-->
---

## Qubes OS and UEFI Secure Boot

---

## XCP-ng and UEFI Secure Boot

---

# Roadmap

- Unfortunately most challenges on Xen side seem to boil down to waiting for
XenServer to develop solution.
  - Does it have to be that way?
* Qubes OS Team created CI/CD pipeline and tooling to produce Xen UKI
* Tooling
  - support for tools like sbctl to allow users manage signing themselves
  - tools for adding SBAT section

<!--

* Qubes OS use pesign

TODO: what is missing, how to proceed, with whome etc.
TODO: submit design session

-->

---

# Final notes

<!--

Strategic agitation.

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

What is our stake in enabling Xen in UEFI SB ecosystem?

-->

---

# Backlog

<!--

* What about bootkits? Maybe correctly set chain of trust at least can help
protecting against bootkits.
  - how bootkits are deployed? - through update, through vulnerabilities in
  "value-added" BIOS components, vulnerabilities in BIOS services and drivers?
* Maybe one of the problems is that Xen is deployed in "someone-else"
datacenters on bare metal?
* Why nobody care in Xen Community care about UEFI SB?

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

- Those are threats against UEFI Secure Boot, but there are also threats
against other components in the system like: ME, BMC and potentially more.
- Other issue is that MSFT and UEFI Forum are centralized authorities to deal
with vulnerabilities, relying always on those players may be insufficient in
some cases

Future ideas:
- discuss PI 1.9 and signed FV
-->

---

# References

* [Xen and dom0 with UEFI/SecureBoot + Intel TXT](https://github.com/tklengyel/xen-uefi), Tamas K Lengyel, last modification 2018
* [Securing Secure Boot on Xen](https://www.youtube.com/watch?v=jiR8khaECEk), Ross Lagerwall, FOSDEM 2019
  - Focused on UEFI Secure Boot for Guest VMs
* [Enabling UEFI Secure Boot on Xen](https://www.youtube.com/watch?v=A_IhKjK7EgA),Robert Eshleman, Xen Summit 2021
  - Also focused on Guest VMs
* [Xen Project Community Call](https://www.youtube.com/watch?v=cJyX6FLK4iU&t=813s), Andrew Cooper, June 2024
* [Implementing UEFI Secure Boot in Qubes OS: Challenges and Future Steps](https://youtu.be/ZcF_RN04oq8), Piotr Król, Qubes OS Summit 2024
* xen-devel activity

<!--

TODO: add activity found on mailing list.

-->
