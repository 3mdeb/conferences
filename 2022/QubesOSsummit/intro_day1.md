class: center, middle, intro

# Welcome to Qubes OS Summit 2022

### Day 1

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Welcome

.center[.image-99[![](/img/qubes_os_summit.png)]]

### .center[Thank you for coming!]

---

# Why I care

.center[.image-99[![](/img/trust.png)]]

* Defend identity.
* We share vision.
   	- Tactics and strategy difference.
* Operating System and Firmware synergy.
* Sustainability.

???

* [ ] personally important thing, that I care about

Explain why you care about this event.

* I can't tell you why you should care, but I will try explain why I care
* **direct human-to-human** interaction is priceless, if 2-3 years ago
  we were not sure about that, now we value it way more
* without backstage discussion, networking and after-parties
* I can talk without wiretap with those whom I value for contribution
  to systems trustworthiness
* I believe that thriving community is crucial to build reasonably
  secure systems
* to build trustworthy solutions we have to trust each other
* creating sustainable environment for trustwoethy solutions is not easy
* we need tools to defend our identity
* wihout privacy we loosing our humanity, if you cannot be yourself and
  have to pretend all the time (panopticon), sooner or later you will change loosing
  part of your self and factors outised you start to form your identity
* we are also dependent on solutions we do not control
* because everything we do is used to manipulate us
  (advertisment,entertaiment) we need tools that help us decide if we
  want such change - trustworthy solutions are the tools
* if systems we use are not trustworthy, by accident or by by purpose,
  we can assume that vulnerability will be abused
* we can fill space left by lack of direct human-to-human backstage
  discussion, networking and after-parties over last 2 years.
* direct h2h interaction helps build trust, and we need confidence if we want
  to develop reasonably secure and trustworthy systems
* we are at qubes os summit, which means we are investing in a shared vision,
* of course, we can prefer different tactics and strategies, but overall we are
  here, which means we are committed to improving Qubes OS. and the surrounding
  ecosystem

* There is not enough synergy between firmware and operating systems world
* promote use of isolation mechanisms like (nested-)virtualization or cgroups in
  regular user daily workflow is minimal, but there is no simpler way to
  improve state of security
* build awareness about opportunities that open collaboration can
  bring to enterprise and community
* improve leveraging of modern platform security features
* convince silicon vendors and their OEM/ODM, that putting more effort in
  contribution to open source projects has not only ethical implications, but
  brings better economical results through wider and faster adoption of new
  hardware
* To gain practical, valuable first-hand knowledge and meet experts who are
  happy to answer intriguing questions and share their passion without creating
  any marketing pitch.

---

# History

.center[.image-99[![](/img/post.png)]]

---

# History

.center[.image-99[![](/img/qubes_os_summit.png)]]
.center[.image-50[![](/img/2021.png)]]
.center[.image-40[![](/img/2019.png) ![](/img/2020.jpeg)]]

???

* [ ] why we started Qubes OS summit?
   	- DRY - recommend Michał Żygowski blog post from Qubes News website
   	- Qubes OS has huge potential of improving awareness about state of
   security landscape and trustworthiness of computing systems
   	- Qubes OS users care about firmware securiyt, understand need for
   open-source firmware, every one want to be understood that why we
          feel great in this community
   	- Qubes OS users are fearless, one member was first to try our proucts
   	- facts say there is huge potential synergy between Qubes OS and
   Dasharo, as well as between Invisible Things Lab and 3mdeb
   	- because we had opprotunity, we didn't want to miss the chance
   	- TBD

* [ ] avoid slides

---

# Accomplishments - 2019-2022

* Initial fwupd/LVFS support for Qubes OS was developed.
* Qubes OS over last years gained 3 certified laptops (one from
  Insurgo, and 2 from NitroKey).
* Xen contributions: AMD Secure Startup via SKINIT
* TrenchBoot Project was established and AMD implementation was founded by NLNet
   	- Open-source D-RTM support
* Anti Evil Maid support for Qubes OS
   	- initial support for AMD platforms
   	- founded effort of replacing tboot with TrenchBoot
   	- support for legacy (Intel 3rd gen) platforms
* Fobanila Project was established and founded by NLNet
   	- Attestation in your pocket
* MSI Z690-A DDR4 and ASUS KGPE-D16 - Dasharo and Qubes OS support
* coreboot and Heads for Raptor Engineering Talos II (IBM POWER9)

???

* [ ] what was accomplished so far
   	- 4 events gathering Qubes OS community
   	- There is in progress project with goal of using TrenchBoot instead of tboot for Qubes AEM setup
   	- Heads project largely expanded its hardware support base
   	- Fobnail - attestation in your pocket

* We get through little bit more formal CfP
* We were able to get more talks from community members and Qubes OS Team
* Talks touch other areas then security, we will talk about Qubes OS future,
  UX, backups, cryptocurrency and many more

---

# Challanges and opportunities - 2019-2022

* Confidential VMs.
* New Golden Age of computing (aka firmware everywhere).
* UEFI BIOS for Arm and RISC-V.
* Reproducible toolchains.
* Hardware compatibility and trustworthiness.

???

* [ ] what problems we still have to face
   	- unfrotunately we getting more firmware and more blobs with every new platform
   	- RISC-V and Arm are not going in good direction (UEFI and all that
   mes(UEFI and all that mess that will not simplify firmware architecture)
   	- Reproducible toolchains were disucssed at multiple occasion,
   bootstrapable toolchain initiative popup, dependency on Docker
          started to be concern to many companies
   	- Xen development related to Hyperlaunch and Dom0less
   	- topic of confidential vms gained on attractiveness
   	- safeboot project was created to simplify leverage use of UEFI Secure
   Boot, measured boot and TPM by end users
   it can also attest DRTM PCRs, but state of the project is not good,
          there is some work to make it work in Qubes OS
   	- KGPE-D16 reupstreaming effort was founded with purpose of creating
   trustworthy workstation for blockchain developers
   	- we know Qubes OS works for us, but let's ask ourselves whether it is. Easy to
   use Qubes OS. How easy is it to get compatible hardware that is reasonably
   secure and trustworthy?
   	    + let's take a look in perspective at the last three years since 2019 was
       great, and a lot of important events happened back then; it was last year
       before all the mess started; after revisiting what happened, let's think about
       what may or should happen over next three years by 2025
   	    + slide with all important events
   	    + Qubes OS features progress
   	    + Qubes OS ecosystem achievements
   	- if we really think Qubes Os cannot reach the masses so maybe we should think
   about Qubes in similar fashion as we think about OpenBSD for reasonably
   secure and trustworthy solutions? Let Qubes OS be example and source of
   innovation in areas we care most about

---

# Vision and challanges - 2022-2025

* Provide solutions that will improve trustworthiness of every computing device.
   	- vertical integration of Qubes OS and Dasharo based-on Certified Hardware
* Extend hardware compatibility
* Provide incident protection, detection and recovery
* Support attestation based on TCG RIM and FIM standards
* Leverage hardware-asisted features
   	- Intel SMI Transfer Monitor and PPAM
   	- Use safeboot approach to improve UEFI Secure Boot integration
   	- Intel Boot Guard shim?
   	- Intel MKTME and AMD SEV guest encryption
* Innovation in operating systems and virtualization
   	- Unikernels as first class citizens
   	- Lightweight VMs
* Accelerate awareness buidling and influencing industry

???

* [ ] vision
   	- 3mdeb: to provide solution that will improve trustworthiness of every
   computing device
   	- 3mdeb: how world would look like with such solution?
      		+ we will have guarantee with physics and mathemtics what is
    going on with our computing, it would not be just laws
      		+ this will resolve many issues, one I personally care about is injustice among vulnerable
      		+ if we people will receive tools to act and make system more just
   	- Qubes OS: let's imagine the world in which everyone use Qubes OS
      		+ verifiable trustworthiness would be a every day experience not exception for choosen one
      		+ https://www.qubes-os.org/intro/#why-qubes-os-1
      		+ https://www.qubes-os.org/doc/security-design-goals/
      		+ let's say Qubes OS and Dasharo will succeed; what world will we have then?
      		+ we have tools that decrease injustice among the most vulnerable
      		+ with the tools we create, we can watch those who should provide us peaceful
    framework to grow (govs, NGOs, both national and international) and verify if
    they fulfill their promises
      		+ we can give back to the community their freedom, privacy, and liberty
      		+ those are long-term goals, but on the way, we need to build tools for
    ourselves gradually,

* [ ] where Qubes OS, 3mdeb and Dasharo would be in 2025
   	- we are far from competition
      		+ we barely leverage old hardware-assisted securit technologies: TPMs, DRTM
      		+ Trammel's safeboot and heads moved us in good direction
   	- lack of innovation in operating systems
* [ ] Joanna's paper overview/progress (state and x86 considered harmful)
   	- Qubes OS moved whole industry in good direction
   	- recent Xubuntu Core ask me about input that I'm pasting suggesting
   this may be potentially malicious input and this is default behavior
   	- I'm pretty sure there are more features like that discussed by
   various distribution mainteiners
   	- it is not enough to have reasonably secure OS - we need trustworthiness
* [ ] latest status in open-source firmware and OCP
   	- more firmware everywhere, firmware is more sophisticated and cannot
   get out of the way as Ron once said, we have to face this and think
   what we can do about it
   	- why it happens? relatively little innovation in operating systems
* [ ] be positive and inspiring, but technically accuarate
* [ ] what actions we should take to move world in positive direction

---

# So what you can expect this year

* This is 3 day event
    - September 9th 2022: conference day 1 and social event
    - September 10th 2022: conferene day 2
    - September 11th 2022: hackathon

---

# Day 1 agenda

* 10:00-10:25 - **_Welcome to Qubes OS Summit 2022 Day 1_**,Piotr (3mdeb)
* 10:30-11:30 - **_Qubes OS development status update_**, Marek (ITL)
* 11:10-11:50 - **_Building secure application with Qubes OS_**, Michael (FPF)
* 12:00-12:20 - **_Next generation of Qubes OS builder_**, Frédéric (ITL)
* 12:30-13:00 - **_Tailoring Qubes for Enterprises_**, Jan (NitroKey)
* 13:00-14:00 - Lunch break
* 14:00-14:30 - **_Qubes OS Policy: Adventures in UX/UI Design_**, Marta (ITL)
* 14:40-15:10 - **_GPU Virtual Machnie (GVM)_**, Arthur (Arc Compute)
* 15:20-15:50 - **_Isolating GUIs with the power of Wayland_**, Puck
* 16:00-16:30 - **_PipeWire and Qubes Video Companion_**, Demi (ITL)
* 16:40-17:40 - **_Design session: graphical subsystem (GPU, Wayland)_**, Marek (ITL)
* 17:50 - Day 1 closing notes
* 19:30 - Social event

---

# Social event

.center[.image-30[![](/img/sudblock2.png) ![](/img/sudblock3.png)]]
.center[.image-99[![](/img/sudblock.png)]]

---

# General Rules

* Respect Code of Conduct.
* Please follow Safety and Health protocols.
* Recording.
* Food and drinks.
* Matrix `#qubes-summit:matrix.org` will be used for communication during
  event.
* In case of any issues please contact with organizers.
* More information on https://qubesos.3mdeb.com

???

* [ ] logistics topics

---

# Organizers

.center[.image-40[![](/img/3mdeb.png) ![](/img/itl.png)]]

* It would not be possible without support and dedication of Invisible Things
  Lab and 3mdeb teams.
* Special thansl to Marek for help talks selection.

---

# Sponsors

.center[.image-60[![](/img/fpf.png)] .image-30[![](/img/nlnet.png)]]

.center[.image-40[![](/img/protectli.png)] &nbsp;&nbsp; .image-30[![](/img/arc-compute.png)]]
.center[.image-40[![](/img/nitrokey.png)]]
.center[.image-40[![](/img/novacustom.png)]]

???

---

class: center, middle, intro

# Q&A
