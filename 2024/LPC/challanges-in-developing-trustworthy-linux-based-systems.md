## Goal

The presentation highlights five challenging areas and activities related to
Linux-based system booting and security from system creator and end user
perspective.

The focus is on:
* Highlighting the problem
* Letting you know where those topics are discussed
* Making connection with further presentations

<!--

Those challenges are probably known to most of you.

-->

---

## Assessment

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/2024/LPC/device-security-screenshot.png" width="220"/>
  <img src="/2024/LPC/firmware-security.png" width="220" style="margin-left: 50px"/>
</div>

* Lack of OS awareness about hardware security capabilities leads to the
inability to evaluate and improve system security posture.
* Over last two years we have inflation of various communities approaching this
topic.
* All that seem to mimic Microsoft Windows
  * GNOME introduced Device Security Settings page
  * KDE Plasma added Firmware Security page
  * both are based on [LVFS HSI](https://fwupd.github.io/libfwupdplugin/hsi.html)

---

## Assessment

* LVFS HSI brings some assumptions
  - focus x86 UEFI ecosystem and compliance with silicon vendor recommendations
  (hence OF != UEFI),
  - no support for hypervisor-based OSes,
* Arm also working on Security Assessment mechanism, which could be levered by
end users (and not only) and give meaningful information about security posture
of the system.
* Topic was discussed on various conferences:
  - OSFC
  - Qubes OS Summit
  - Dasharo User Group
  - Arm SystemArchAC Security Sub-team
* Without exposing interface which will protect against misconfiguration of
security features shipping hardware with Linux would be harder or impossible
for some buyers.

---

# SMM (TEE?) as Chain of Trust Gap

* Platform security and the challenges of closing System Management Mode
(SMM)-created gap in an open-source way.
* Solutions:
  - SMI Transfer Monitor - Linux driver [out of tree](https://github.com/EugeneDMyers/stm_linux_module), probably very far from making it first class citizen
  - Project Mu - has STM integrated

---

# All your hardware belong to us

- The growth of hardware and firmware components like AMD SMM Supervisor, Intel
PPAM, or MS Pluton and how effectively those block building trustworthy systems
in parallel, creating an ecosystem in which we cannot leverage the full
potential of hardware and firmware in our machines.

---

# Root of Trust

- Plans for defeating the lack of consistent assessment, implementation, and
provisioning of Root of Trust on very different hardware configurations through
Caliptra, DICE, SPDM, and more, and what impact it may have on the OS.

---

# What we can do better with DRTM for AMD

- Lessons learned from making DRTM for Intel CPUs a first-class citizen in
Linux kernel impact on support for AMD.

