class: center, middle, intro

# D-RTM for Qubes OS VMs

### Qubes OS and 3mdeb mini-summit 2020

## Piotr Król

<img src="remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Agenda

* Intro and goals
* Terminology
* Flicker
* Platform relaunch
* Virtual Machine Inspection and D-RTM
* vTPM and D-RTM
* Network booted vDLME
* Visual trust level indicator for VMs
* Future ideas
* Discussion

---

# `whoami`

.center[<img src="remark-templates/3mdeb-presentation-template/images/piotr_krol.jpg" width="200px">]

.center[Piotr Król]
.center[_Founder & Embedded Systems Consultant_]

.right-column50[
<img src="remark-templates/3mdeb-presentation-template/images/twitter.png" width="24px"/> @pietrushnic<br>
<img src="remark-templates/3mdeb-presentation-template/images/email.png" width="24px"/> piotr.krol@3mdeb.com<br>
<img src="remark-templates/3mdeb-presentation-template/images/linkedin.png" width="24px"/> [linkedin.com/in/krolpiotr](https://www.linkedin.com/in/krolpiotr)<br>
<img src="remark-templates/3mdeb-presentation-template/images/facebook.png" width="24px"/> [facebook.com/piotr.krol.756859](https://www.facebook.com/piotr.krol.756859)
]

.left-column50[
- open-source firmware
- platform security
- trusted computing
]

---

# Presentation goal

### .center[To discuss value and usage models of D-RTM implementation in Qubes OS]

<br>
<br>
<br>
<br>
<br>
<br>
#### Kudos for support

* Marek Marczykowski-Górecki (Qubes OS)
* Daniel Smith (TrenchBoot)
* Andrew Cooper (Xen)

---

# Root of Trust family

.center[.image-75[![](images/drtm_in_rot.svg)]]

* 2 most well known implementations use special CPU instruction to trigger
  D-RTM (aka Dynamic Launch Event): Intel `SENTER` and AMD `SKINIT`
* D-RTM is very different from S-RTM in way it establish RTM

---

# Terminology

.center[.image-99[![](images/d-rtm_timeline.png)]]

* DRTM start when Dynamic Launch event call executes
* DL Event controls PCRs 17-22, those are initialized with value -1
* DL Event change PCRs value to 0 and immediately extends with DCE hash
* Any attempt to reset TPM will set PCR[17] to -1 (TPM reset attack immunity)

.footnote[
TCG D-RTM Architecture v1.0.0
]

---

# Boot process for Qubes OS

.center[.image-99[![](images/boot_process_overview.svg)]]

* This is just general overview of boot process to build background for further
  slides
* It applies to many other projects using virtualization technology

---

# Early Launch scenario

.center[.image-99[![](images/early_launch.svg)]]

* **Early Launch** happens once each boot
* What is the value?
  - in STM-enabled configurations we can remove UEFI/coreboot from TCB
  - we can avoid complexity of S-RTM (NDAs, convoluted specs and manufacturing process)
  - we can leverage PCRs 17-22 for secret unsealing or attestation

.footnote[STM - _SMI Transfer Monitor_]

---

# Late Launch scenario

.center[.image-99[![](images/late_launch.svg)]]

* **Late Launch** may happen multiple times during runtime
* Way more complex case, but give lot of flexibility
* What is the value?
  - depends on DCE (D-RTM Configuration Environment) Payload
  - D-RTM provides on-demand secure execution environment
  - we will discuss further in the presentation

---

# Flicker

.center[.image-70[![](images/flicker.png)]]
* In 2008 Jonathan M. McCune, Bryan Parno, Adrian Perrig published v0.1 version
  of Flicker, a technique for executing application code as DCE Payload
* Their papers provide couple interesting use cases:
  - remote rootkit detector (hash of: kernel text segment, system call table and loaded modules)
  - attested results for distributed applications
  - ssh password protection against malicious server
  - private key secure storage

.footnote[https://web.archive.org/web/20160323022110/https://sparrow.ece.cmu.edu/group/flicker.html]

---

# Platform relaunch

.center[.image-90[![](images/platform_relaunch.svg)]]

* Since Xen can control `VMEXIT_{SKINIT,SENTER}` we have to reestablish trust
  in hypervisor before performing any further system integrity checks
* Otherwise Xen could trap our call or fake its results

---

# VMI

* Virtual Machine Introspection (VMI) is a technique of runtime state, what can
  be helpful in debugging or forensics analysis
* Use VMI for VM process table (or other running system properties)
  attestation:
  - critical system component periodic audits/relaunch (e.g. vault, gpg, sys-vtpm)
  - rootkit and malware detection
  - checks before performing administrative tasks
* VMI when connected with secure execution environment provided by D-RTM can
  bring additional use cases, which will be described later

---

# vTPM

.center[.image-40[![](images/vtpm_and_drtm.svg)]]

* Any attestation of sealed secrets when using D-RTM would require TPM support
  for VMs
* In some cases also DL Event instruction emulation would make sense to avoid
  delay which real SKINIT/SENTER may cause

---

# Network booted vDLME

.center[.image-70[![](images/netboot_vdlme.svg)]]

* SKINIT (or any other DL Event) instruction is emulated by hypervisor but from
  VM perspective it looks like Late Launch

.footnote[https://blog.3mdeb.com/2020/2020-06-01-ipxe_lz_support/]

---

# Visual trust level indicator for VMs

* Apply VM colors according to trust level established based on VM process
  table attestation
* various policies possible depending on threat model
  - if all processes are known and measured then give black
  - gradually go down to red
* early launch - color assigned at boot, also S-RTM can be used
* late launch - color change while system is running

---

# Future ideas

* Trusted system backups and migration
  - run critical system actions only in vDLME/DLME
* Trusted firmware update
  - running critical piece of fwupd as DCE Payload or in trusted VM
* Dynamic RPC policy
  - let give ability to run some workloads only in VM that meet required trust level
  - pools of VMs meeting certain policy may change over time
  - most probably would involve developing Qubes RPC extension
* Secure storage
  - it is possible to seal secret in TPM and make it available only to certain
    DCE Payload
  - this may help in implementing per-VM password manager, most probably simpler
    and faster solution then vault VM

---

# Discussion

* It looks like even basic Late Launch implementation to be secure requires a
  lot of work
* How to solve attestation problem in Qubes OS? We don't want rely on network
  connectivity.

---

# 

## .center[Q&A]

