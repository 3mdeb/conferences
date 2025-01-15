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

<!-- Basic overview of UEFI Secure Boot -->

---
# UEFI Secure Boot in Xen

<!--
What's different when using Xen, why can't Secure Boot be enabled by default
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

<!-- Taken from https://xenbits.xen.org/docs/unstable/support-matrix.html -->
---

<!-- Describe experimental support, why it is/isn't enough -->

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
# SBAT support

<!--
Describe why it is needed, how the support is going, what will need to be
done
-->

---
# NX_COMPAT

<!--
Describe why it is needed, how the support is going, what will need to be
done
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
-->

---
# Livepatching

<!--
Describe why it is needed, how the support is going, what will need to be
done.
-->

---
# Command line handling

<!--
Describe why it is needed, how the support is going, what will need to be
done.
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
