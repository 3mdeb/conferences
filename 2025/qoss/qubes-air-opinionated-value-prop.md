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
- [x] outline opinionated vision of Qubes Air vertical integration
- [x] address the needs of security-conscious technical professionals
  - [x] define those professionals
- [ ] How Qubes Air aligns with the threat models and workflows of
  security-sensitive users including comparison with non-Qubes Air workflow.
  - [x] what workflows we talking about
  - [ ] shim-review as dataset for problems mining, this is just shim and we
    have so many needs
    - mention some requirements for HSM, key material maintenance, signing
      process, CI/CD relation
  - [x] need for user-controlled root of trust and chain of trust
    - Intel Boot Guard or Arm-based key fusing as example
    - sealing/forward sealing
- [x] give clear reference to Kicksecure/Whonix and PUP
- [ ] what will be used to solve those problems?
  - [ ] obviously Dasharo and Qubes OS (in this case Qubes Air), but is there
    an alternative?
- [ ] qrexec-based RemoteVM advancements
  - [ ] brief explanation of qrexec (most likely some older content can be
    used)
  - [ ] Qubes Air and RemoteVM novum that coming to Qubes OS R4.3
  - [ ] PoC demo it works in at least tested in some limited capacity
- [ ] explain what workloads those components can satisfy
  - [ ] enumerate workloads and workflows based on threat model that can be
    satisfied using components connected in our system Dasharo+Qubes Air on
    server and Dasharo+Qubes OS on thin client
  - [x] how those are executed now,
    - nobody want to talk about ugly reality of today
  - [ ] how those would be used in future
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
layout: cover
background: /intro.png
class: text-center
---

## Problem Statement (aka Frictions)

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
  - internal or external
- Auditor
  - governments, certification/compliance org, insurer

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

<center>
  <div style="display: flex; flex-direction: column; align-items: center;">
    <img src="/@fs/repo/public/2025/QubesOSsummit/power-up-privacy-logo-light.png" width="220px" style="margin-bottom: 40px; margin-top: -30px;">
    <div style="display: flex; justify-content: center;">
      <img src="/@fs/repo/public/2025/QubesOSsummit/Kicksecure-logo-text.svg" width="300px" style="margin-right:20px">
      <img src="/@fs/repo/public/2025/QubesOSsummit/Whonix-logo-text.svg" width="300px">
    </div>
  </div>
</center>

<br>

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
clicks: 4
---

<center>
    <img src="/@fs/repo/img/qoss2025/friction_1.excalidraw.png" width="500px">
</center>

<!--

[click]
* Key management is world class issue, or at least issue of those who are
  responsible for security.

[click]
* Most of recent security issues are coming from key managment or rather
  mismanagement. Intel Boot Guard key leaks from OEMS or provisioning systems
  with sample Test key (famous PKFail).

[click]
* What we have today:
  - key tree sprawls across laptops, USB sticks, and ad-hoc scripts;
  - every new platform or release branch spawns another class of keys,
  - Many orgs reliably prove when a key is allowed to be used or that the machine
    holding it is in a known-good state, especially if we consider various levels
    of key tree.
  - Our secpacks growing and it is just matter of time, when it will cause
    problems, not mentioning about workforce rotation which requires to certify and
    revoke keys regularly across the systems
  - HSMs help but add cost, workflow integration overhead, and despite there is
    place and need for those, they have to be integrated in infrastructure if
    expected value is on positive side.

[click]
* Those are serious issues and we will not solve all of them.
  There are definitely solutions that fit ideally in solution chain, but I want
  to discuss potential Qubes Air architecture may have in improving that part
  slightly, so we can leverage ecosystem that we know and love.

-->

---
clicks: 4
---

<center>
    <img src="/@fs/repo/img/qoss2025/friction_2.excalidraw.png" width="500px">
</center>

<!--

[click]
* This is not what developers want to hear, but IMHO we should not build
  software on our thin clients end points.
  - there are workstations and servers for that and to those machines we should
    delegate hard job

[click]
* In configuration with hypervisor we tend to destroy our storage, wearleveling
  yada yada.

[click]
* But that is not the only problem with local builds:
  - reproducibility or even distributed reproducibility is another issues
  - Toolchains drift between developers and runners; base images and host kernels
    change under us; timestamps, locale, file ordering, and network fetches leak
    nondeterminism;
  - we can save VMs or containers, and this is how most of us solve that problem
* Building locally is bad for business.
* We have to build architecture designed for reproducibility with fine grained
  policies and who knows

[click]
* By no means Qubes Air is dedicated tool for such problem, but may be unified
  interface and policy management improve overall operation.
* This is not just building, that would be simple, let's consider building with
  special souse.

Some other use cases/workloads:
- trasncoding, video/audio processing, streaming
- search and indexing
- CI/CD - we should not build on our thin clients

-->

---

<center>
    <img src="/@fs/repo/img/qoss2025/friction_1_plus_2.excalidraw.png" width="900px">
</center>

<br>

Of course, that equation works only under specific (_opinionated_) computation
systems. In this case, I mean systems where trustworthiness for computing is
not an option; it is a requirement. If that happens, controlling the Root of
Trust and Chain of Trust is paramount.

---
clicks: 4
---

<center>
    <img src="/@fs/repo/img/qoss2025/friction_3.excalidraw.png" width="600px">
</center>

<!--

[click]
* Provisioning RoT/CoT is still a maze.
* Every platform and release family comes with a different recipe for key
generation, fusing or Boot Guard policy, Secure Boot PK/KEK/DB updates, PCR
policies, and update-signing semantics.
* The tools live in different silos—ROM tools, board vendor flashers, OEM
scripts, CI steps, field jigs—and none of them agree on formats, identities, or
evidence.

[click]
* Each run turns into a bespoke ceremony: re-confirm the docs, re-approve the
scripts, re-enroll the keys, hope the jig version matches, discover late that
the ‘right key signs the wrong thing’ or that revocation lists drifted. 

[click]
* Auditors then ask who signed what, on which machine, and in what measured
state—and we can’t reconstruct it without heroics.
* The result is schedule slip, expensive appliances, creeping delegation
lock-in, and a persistent doubt about whether the provisioned chain will
actually verify in the field.

-->
---

<center>
    <img src="/@fs/repo/img/qoss2025/friction_4_and_5.excalidraw.png" width="900px">
</center>

<!--

You are probably bored, but before we jump into Qubes Air two last cases.

I know I should have just 3 frictions, but I could not resist adding last two
which are very closely related to todays trends and giving pitch  is
essentially impossible without mentioning those two areas.

I promise this is almost last time and we will focus on frictions #1-#3.

Running LLMs on real project data keeps tripping the same alarms: I can’t prove
the model is stateless, I can’t bound where prompts and embeddings travel, and
I can’t enforce who gets compute or which model weights are even allowed for a
given task. Caches, plugins, and silent telemetry create memory I never
authorized. Model versions drift under me, so two runs on the ‘same’ input
disagree, and I have no clean way to freeze context for review. Egress controls
are porous—the model can synthesize or summarize its way around filters—and
nothing ties a response to an attested environment. The net effect is legal
exposure, accidental leakage, and irreproducible results that I can’t defend in
a post-mortem or an audit.

When something goes wrong, I cannot reconstruct who did what, on which machine,
in what measured state. Logs live in runners, artifact stores, package
registries, and ticketing systems that don’t agree on identities or time.
Provenance breaks at the seams: the binary doesn’t cleanly map to the commit,
the container SBOM disagrees with the base image SBOM, and the update-signing
step sits in a different trust silo. Ephemeral infrastructure erases context,
timestamps are squishy, and vendors gate the few tools that might help behind
expensive appliances and lock-in. The result is slow, inconclusive root-cause
analysis, weak evidence for compliance, and a lingering doubt about whether the
thing we shipped is the thing we meant to ship.

-->

---
layout: cover
background: /intro.png
class: text-center
---

# Qubes Air

<!--

We quickly get through some frictions experts may experience today. Now its
time to recap Qubes Air from 2018.

-->

---
clicks: 4
---

<figure>
  <img src="/@fs/repo/img/qoss2025/qubes-cloud-hybrid.png" width="500px">
  <figcaption>
    Qubes Air: Generalizing the Qubes Architecture, http://qubes-os.org/news/2018/01/22/qubes-air/
  </figcaption>
</figure>

<!--

[click]
* Joanna writing is probably one of most influential among FOSS crowd when we
touch space of privacy and security.
* We keep recalling her work related to x86 considered harmful or stateless
laptop, but today I would like to talk about post published on 22 January 2018
about Qubes Air, which generalize Qubes Architecture.

[click]
To make things clear. Following are out of scope out of scope:
- old hardware - there is reason for that, EOL, lack of patches for uArch bugs,
  penny scrapping on hardware, unless we talking about high value ancient
  artifacts, with all due respect not every one can and should become Indiana
  Jones of computers, we respect everyone who is doing that, but that's not the
  topic here
  - so we talking about modern and reasonably expensive hardware, it would be
    clearer when I will explain our persona
- Qubes Air in public cloud - only in some limited capacity for very narrowly
  defined use cases, but with focus and foundation on self-hosted private
  cloud.
- Situation where Platform Owner (individual or organization) do not put
  emphasis on reasonable control their Root of Trust and Chain of Trust.

[click]
What were reasons for Qubes Air:
- Deployment cost understand as problem with finding compatible hardware
  - it is not that hard to find hardware which is Qubes OS Certified and works
    our of the box
  - our need for controlling hardware as well as requirements for domain specific
    computing extend, that why we can redefine it
  - Qubes Air still help satisfy that reason by offloading to cloud
- Hypervisor or modern and powerful (cutting corners "x86") computer
  architecture is the issue and source of bugs.
  - it is still value although Xen has probably most solid security process among
    open-source hypervisors
  - Xen is also considered one of the most stable and minimal in context of
    features it support
  - pending MISRA  compliance and adoption in automotive prove that
  - microarchitecture bugs are definitely issue predicted or marketed by Joanna,
    but there are other processor architectures that coming (Arm, RISC-V) and x86
    have to keep up to stay competitive, there is also a lot of side project which
    try to address that: CHERI, memory tagging, control flow integrity

Notes about Joanna approach to security of Qubes:
- it is about minimizing and controlling interfaces between components
- more isolated components with well defined interfaces are better than unified
  bloated solution


[click]
- There are some things on this picture which still remain a dream, but we
slowly leaning toward those: Qubes GUI VM, Qubes GUI protocol, or fully
featured Admin VM with dom0less or minimal dom0 architecture.
- We are far from exhausting Joanna vision, here we talking only hybrid
architecture, but there are also Qubes on air-gapped devices as well as Qubes
Zones. We don't have time to dive into those here. Maybe at different occasion.

-->
---

<figure>
  <img src="/@fs/repo/img/qoss2025/qubes-zones.png" width="425px">
  <figcaption>
    Qubes Air: Generalizing the Qubes Architecture, http://qubes-os.org/news/2018/01/22/qubes-air/
  </figcaption>
</figure>

<!--

Qubes Zones is another concept build on top of Qubes Air, which could bring
very interesting topic of distributed reproducibility as proof of correctness,
as well as multiple signed reproduction proofs in order to satisfy the criteria
of reasonably secure supply chain strategy.

Closely resembles Friction #2.

-->

---

<center>
    <img src="/@fs/repo/img/qoss2025/qubes_air_motivation_today.excalidraw.png" width="800px">
</center>

<!--

So today motivation for Qubes Air is:
- distributed reproducibility (stagex)
- self-hosted user-controlled Root of Trust and Chain of Trust management systems (Zarhus Provisioning Box/VM)
- MAC LLM inferencing (arthurrasmusson/bsd3-mac-llm-ui)
- Compliance evidence gathering (CISO Assistant?)

There can be more, but as I said this is opinionated.

-->

---

<center>
    <img src="/@fs/repo/img/qoss2025/state_of_qubes_air.excalidraw.png" width="900px">
</center>

---

<!--

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

<!--

Friction #1 solution

How Qubes Air could help?

In Qubes Air the issuer is me. We keep a simple three-tier hierarchy: L1
ephemeral local keys for everyday work, L2 release-family keys available only
after attestation, and L3 product or organizational masters touched rarely
under N-of-M. Measured boot binds unseal to TPM PCRs so secrets open only on
attested state. Remote signing runs in attested service VMs via qrexec policy;
an HSM or KMS can provide custody without owning the workflow. The outcome is
fewer standing keys on endpoints, policy-gated use, and auditable, reversible
actions when something goes wrong.

-->

---

<!--

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

