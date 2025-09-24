---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

### Qubes Air: Opinionated Value Proposition for Security-Conscious Technical Professionals

<br>

#### Piotr Król

<!--

Building on "Qubes Air: Hardware, Firmware, and Architectural Foundations":
- [ ] outline opinionated vision of Qubes Air vertical integration
- [ ] address the needs of security-conscious technical professionals
  - [ ] define those professionals
- [ ] How Qubes Air aligns with the threat models and workflows of
  security-sensitive users including comparison with non-Qubes Air workflow.
  - [ ] what workflows we talking about
  - [ ] shim-review as dataset for problems mining, this is just shim and we
    have so many needs
    - mention some requirements for HSM, key material maintenance, signing
      process, CI/CD relation
  - [ ] need for user-controlled root of trust and chain of trust
    - Intel Boot Guard or Arm-based key fusing as example
    - sealing/forward sealing
- [ ] give clear reference to Kicksecure/Whonix and PUP
- [ ] what will be used to solve those problems?
  - [ ] obviously Dasharo and Qubes OS (in this case Qubes Air), but is there
    an alternative?
- [ ] qrexec-based RemoteVM advancements
  - [ ] brief explanation of qrexec (most likely some older content can be
    used)
  - [ ] Qubes Air and RemoteVM novum that coming to Qubes OS R4.3
  - [ ] PoC demo it works in at least tested in some limited capacity
- [ ] explain what workloads those components can satisfy
  - [ ] enumerate workfloads and workflows based on threat model that can be
    satisfied using compoents connected in our system Dasharo+Qubes Air on
    server and Dasharo+Qubes OS on thin client
  - [ ] how those are executed now, how those would be used in future
    - nobody want to talk about ugly reality of today
- [ ] relation to attestation based authentication
  - [ ] TrenchBoot role
    - this is not AEM case, although AEM could be used at thin client
      connecting to the system
    - Implementation strategies for attestation using the TrenchBoot ecosystem,
      contributing to verifiable platform integrity.
  - this could resolve problems of account management, but could be hard to
    implement
  - auditability and compliance, so providing evidence stack is running in
    knwon good state - there is a lot of to consider if that would have to be
    made in scale
  - Mendatory Access Control based access to resources e.g. LLM compute,
    models, etc.
  - can given infomation be kept only in vm
- [ ] business value of vertically integrating mentioned components
- [ ] CTA for investors and customers

TBD:
- should we talk about fully-featured solution and its lifecycle right now?
- or maybe just draw vision of it and focus on pieces?
- aiming for holistical design is always tempting, but pracrtice and experience
  show this is usually bad direction, so we have to focus on delivering small
  steps that really improve situation, so let's focus on max 3 tasks that will
  change, or could be implemented better thanks to Dasharo-based dservers with
  Qubes Air

Painpoint backstory:

- We dealing with growing number of private keys, every platform and every
  release family for given platform adds to the key tree structure

-->

---

# `whoami`

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="/piotr_krol.jpg" style="width: 100px; border-radius: 50%;" alt="Profile Picture">
  <div>
    <b style="font-size: 1.5em;">Piotr Król</b><br>
    <i style="font-size: 1.2em;">3mdeb Founder</i>
  </div>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; font-size: 1.2em;">
  <div>
    🔑 <code>869E 9AE8 AFDB 5FAE 6068  338B 99BD 2EEE E2D0 CE31</code><br>
    ✉️ <a href="mailto:piotr.krol@3mdeb.com">piotr.krol@3mdeb.com</a><br>
    🐦 <a href="https://x.com/pietrushnic">@pietrushnic</a><br>
    🔗 <a href="https://www.linkedin.com/in/krolpiotr/">LinkedIn</a><br>
    🌐 <a href="https://www.3mdeb.com">3mdeb.com</a><br>
    💻 <a href="https://github.com/pietrushnic">GitHub</a><br>
  </div>
</div>

::: footer

<div style="color: black; font-size: 0.8em; text-align: center; margin-top: 20px;">
  🌟 Reach out for collaborations or inquiries!
</div>
:::

---

<center>
  <div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/3mdeb-logo.png" width="220px" style="margin-bottom: -40px; margin-top: -30px;">
    <div style="display: flex; justify-content: center;">
      <img src="/@fs/repo/img/pet_logo.png" width="180px">
      <img src="/@fs/repo/img/dasharo-sygnet.svg" width="230px">
      <img src="/@fs/repo/img/zarhus_logo.png" width="160px">
    </div>
  </div>
</center>

Our mission is to enhance platform security using the expertise we gained in
Root of Trust, Chain of Trust, Trusted Computing, TPM, coreboot, UEFI/EDK II,
Yocto, U-Boot, and Linux. Pace Enterprise Training (PET), Dasharo and Zarhus,
are products designed to enhance the trustworthiness of every computing device
through open development principles. We prioritize transparency, digital
sovereignty, and the right to repair in creating resilient embedded firmware
solutions, ensuring secure systems for the community and our clients.

<!--

About 3mdeb.

-->

---
clicks: 2
---

<center>
    <img src="/@fs/repo/img/qoss2025/actors.excalidraw.png" width="450px">
</center>

- Expert
  - maintainers of security related software
  - incident response teams
- Adversary
  - intrenal or external
- Auditor
  - governament, certification/compilance org, insurer

<!--

Let me set the stage with some actors for my story. We have Experts,
Adversaries, and Auditors.

[click]
- Other examples of experienced professionals I'm thinking about, are
  - quality assurance of mission critical software
  - people dealing with Confidential or Top Secret documents
  - researchers
  - huge and important group that falls in this bucket are people who would
    like to leverage self-hosted GPU compute for LLM-related in isolated
    environment, which can deliver quarantees on non-leaking, so almost
    everyone delivering value right now
- This presentation is targeted at Experts, but feedback from Adversaries and
Auditors is welcome.

[click]
Why them?
  - they have need and can typically resources to afford solutions that makes
  their life easier, or improve quality of life by better defending workflows
  and workloads
  - Need to protect high value cryptographic keys (e.g. master keys, release
    signing keys).
  - Need to ensure software reproducibility.
  - Overhead with incoherent trust boundaries, maintenance of multiple tools and
    difficulty of achieving verifiable/attestable state.
  - Knowledge to define appropriate policy for those operations.
  - Need for custom services (backup, router, NAS, air-gapped operations)
- Assuming we are experts only by creating solutions that work for us we can
  really create solutions for others


-->

---

Documentation of
[Threat Model Persona](https://github.com/3mdeb/verified-boot/blob/master/threat-model-persona.md)
of **Expert** and
[Threat Model](https://github.com/3mdeb/verified-boot/blob/master/threat-model.md),
that can be exercised by some **Adversaries** was funded by PowerUpPrivacy and
reviewed by Whonix/Kicksecure Maintainers.

<!--

Some credits.

-->

---

# Friction #1

<center>
    <img src="/@fs/repo/img/qoss2025/qoss2025_friction_1.excalidraw.svg" width="500px">
</center>

<!--

Some other use cases/workloads:
- trasncoding, video/audio processing, streaming
- search and indexing
- CI/CD - we should not build on our thin clients

Assumptions:

It is trivial to say that Virtualization Based Security is future of Security,
but so far it is adapted either by:
1. Hyperscalers.
2. Hosting/cloud ecosystem.
3. Corporate Enterprise OSes.
4. Niche group of enthusiasts.

There is massive market with potential benefits from Virutalization Based
Security especially in era of uncertainty, not-always-reasonable compliance
requirements and return of PC/Destkop/Workstation era on the LLM hype wave.

Visualization:
- three racks: homelab, company lab/dev, company production
- buying professional all-in-one rack -> expensive, economically infeasible,
  also vendor lock-in
- putting it together:
  - this is what some of us doing as daily job, occasional system building or
    professionally
  - again we can choose ready to use building blocks, or try to glue something
    our own

In most cases it is not only about security, privacy or trustworthiness, it is
also for cases, when incident will happen we really have ability to:
- detect - quickly inspect, analyze and isolate to improve our detection
- protect - also improve our protection
- recover - get back to operation ASAP

Why now?
- rise of need for security because global power shift
- first most likely is the cause of hard push for compliance, compliance means
  auditability

TBD:
- KPI for proving problem is solved.
-->

---

# Friction #2

---

# Friction #3

---

# Friction #4 and #5

<!--

I know I should have just 3 frictions, but I could not resist adding last two
which are very closely related to todays trends and giving pirch  is
essentially impossible without mentioning those two areas.

I promise this is almost last time and we will focus on frictions #1-#3.

-->

---

<!--

Joanna writing is probably one of most influential among FOSS crowd when we
touch space of privacy and security. We keep recalling here work related to x86
considered harmful or stateless laptop, but today I would like to talk about
post published on 22 January 2018 about Qubes Air, which according to here is
generalization of Qubes Architecture.

What were reasons for Qubes Air:

- Deployment cost - to some extent still valid today, but OTOH we get great
  powerful and memory rich laptops which seem to be sufficient for casual use
  of and even for some daily drivers. So not so much issue today unless you are
  compute (or certain type of compute) hungry professional.
- Hypervisor or modern and powerful (cutting corners "x86") computer
  architecture is the issue and source of bugs.

What I don't want to talk about?

- old hardware - there is reason for that, EOL, lack of patches for uArch bugs,
  penny scrapping on hardware, unless we talking about high value ancient
  artifacts, with all due respect not every one can and should become Indiana
  Jones of computers, we respect everyone who is doing that, but that's not the
  topic here
  - so we talking about modern and reasonably expensive hardware, it would be
    clearer when I will explain our persona
- Qubes Air in public cloud, unless in some limited capacity for very narrowly
  defined use cases, but with focus and foundation on self-hosted private
  cloud.
- Situation where Platform Owner (individual or organization) do not put
  emphasis on reasonable control their Root of Trust and Chain of Trust.

Idea for picture: schematic drawing of Qubes Air schemes and big red X on those
which we discourage.

What are other reasons?
- distributed reproducibility
- need for heavy but privacy respecting and secure computing

Notes about Joanna approach to security of Qubes:
- it is about minimizing and controlling interfaces between components
- more isolated components with well defined interfaces are better than unified
  bloated solution

Qubes Air security considerations:
- Is local laptops computing worse than remote server? Why?
- Is travelling with USB token that keeps your private key better than keeping
  it under the physical security control guard in a vault?
- The problem is sending things over intrenet?
  - What if we sending only through intranet?
- Some may say this is coming back to mainframe security model.
  - Classic mainframe/MLS concentrates the TCB on the host. Terminals are I/O
    only and outside the TCB; they do not enforce policy. Any controller or
    link encryptor on the path enters the TCB only if the system relies on it
    for security properties. This sets the baseline for our contrast with Qubes
    Air, where we keep the TCB central but add a minimal, attested
    display/input slice on the thin client.

-->

---
