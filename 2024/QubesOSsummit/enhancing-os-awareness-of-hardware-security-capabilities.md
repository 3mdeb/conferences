---
layout: cover
background: /intro.png
class: text-center
routeAlias: assessment

---

## Enhancing OS Awareness of Hardware Security Capabilities in Qubes OS

### Piotr Król

---

<center><img src="/2024/LPC/qos_sec_report.png" width="270"/></center>

* Lack of OS awareness about hardware security capabilities leads to the
inability to evaluate and improve system security posture.
* Over the last two years, we have seen number of various communities
approaching this topic.
  - GNOME introduced the Device Security Settings page (based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html)).
  - KDE Plasma added Firmware Security page (based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html)).
  - Qubes OS Security Report (based on Qubes HCL).
  - FSF RYF Certification (unclear rules).

<!-- markdownlint-disable MD022 MD003 -->
---
clicks: 4
---
<!-- markdownlint-enable MD022 MD003 -->

## Assessment

* Some interfaces for CPU assessment already exist. We have tools like:
  - `lscpu`, which shows `/sys/devices/system/cpu/vulnerabilities`.
  - `/proc/cpuinfo` bugs.
* We could only secure our ecosystem if we knew what security mechanisms are
available on a given piece of hardware.
* Shipping hardware with Linux would be more challenging without exposing the
interface, which will help assess security configuration and help protect
against misconfiguration of security features.
* Achieving results requires broader cooperation between communities and vendors.
* Followed presentations and communities discussed this topic:
  - [Embedded Recipes: LVFS: The next 50 million firmware updates](https://embedded-recipes.org/2022/wp-content/uploads/2022/06/LVFS-ER-avec-compression.pdf).
  - [TrenchBoot Summit: LVFS Host Security ID (HSI) and Silicon-Based Core Security](https://www.youtube.com/live/xZoCtNV8Qs0).
  - Arm SystemArchAC Security Sub-team.

<!--

[click] many tools focus x86 UEFI ecosystem and compliance with silicon vendor
recommendations (hence OF != UEFI),

[click] How would we know that correct version of SBAT was applied and correct
revocation data included?

[click] How we would realize we booting Your-Favourite-IBV BIOS, U-Boot with
UEFI payload support or coreboot with UEFI Payload, or maybe different
combination? Or maybe we should admit we don't care about about niche use
cases.

[click] LVFS HSI brings some assumptions
  - arbitrary ranking, not actively maintained, limited number of security
capabilities enumeration,
  - limited support for hypervisor-based OSes (Qubes OS, xcp-ng, Proxmox),
of the system.

-->

<!-- markdownlint-disable MD022 MD003 -->
---
layout: cover
background: /intro.png
class: text-center
---
<!-- markdownlint-enable MD022 MD003 -->

# Discussion
