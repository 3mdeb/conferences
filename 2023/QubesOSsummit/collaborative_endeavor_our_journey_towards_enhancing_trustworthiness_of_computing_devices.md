class: center, middle, intro

<!-- markdownlint-disable-next-line MD013 -->

# A Collaborative Endeavor: Our Journey Towards Enhancing Trustworthiness of Computing Devices

## Qubes OS Summit 2023

### Piotr Król

.center[<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
width="150px" style="margin-left:-20px">]

---

# `whoami`

.center[<img
src="/remark-templates/3mdeb-presentation-template/images/piotr_krol.jpg"
width="150px">]

.center[Piotr Król] .center[_3mdeb Founder_]

.left-column55[

- Conference speaker and organizer
- Open-source firmware evangelist
- Dasharo vision and mission gatekeeper
- OpenSecurityTraining2 Instructor ]

.left-column45[

- 15yrs+ in business
- Qubes OS user since 2016
- Interested in theology, philosophy and psychology.
- Chess and bridge player. ]

.center[@pietrushnic@fosstodon.org]

---

# Agenda

- Building partnership and shared vision
- Fobnail Project
- TwPM
- Dasharo HCL
- Dasharo Openness Score
- Dasharo Tools Suite
- Lesson learned

---

# Building partnership and shared vision

- We all care directly about privacy and security
  + indirectly we care about open development, trustworthiness, platform
    security, and maybe even right to repair
  + we differ in strategies and tactics we use but we pursue the same goal
- 3mdeb created two partnership programs which aim to help enable more Qubes OS
  Certified Hardware
  + Inspired by Qubes OS
- Goal of the programs is to share revenue in open-source value chain
- Challenge: how big is the market really?
  + Hence Qubes OS statistics (it took 10 years to get to 30k and another 3
    years to reach 50k)
  + realistically how many users may use reasonably secure operating system

---

# Building partnership and shared vision

### .center[Dasharo Revenue Sharing Partners]

.center[.image-50[![](/img/nitrokey_logo.png)]
.image-15[![](/img/novacustom_logo.png)]]

### .center[Dasharo Supporting Partners]

.center[.image-50[![](/img/insurgo_logo.png)]]

---

# Building partnership and shared vision

.center[.image-80[![](/img/segments.svg)]]

- It is not only about those market segments, but also about supporting those
  who create and deliver value on those market segments
  + developers, DevOps and IT of our famous VPN provider
  + high value IP creators: hardware, IP blocks developers, chips designers etc.

???

- vertical integration on various levels to give tools for digital sovereignty
  + we should think about that in context of computing devices market segments
  + mobile - Graphene OS
  + network appliance - secure my network and my window to external world,
    OPNsense and OpenWRT world
  + desktop/laptop/workstation - here we have Qubes OS world
  + server - Qubes Air, RHEL, SLES?
  + For those users we have to provide value added vertically integrated
    features

---

# Building partnership and shared vision

.center[<img src="/img/dsr_value_prop.png" width="800px"
style="margin-left:-20px">]

---

# Building partnership and shared vision

.center[<img src="/img/dsp_value_prop.png" width="800px"
style="margin-left:-20px">]

---

# Fobnail Project

.center[.image-70[![](/img/fobnail-devkit.png)]]

.center[https://fobnail.3mdeb.com]

- Fobnail Project provide resources to create axiomatically trustworthy device
  and simple user interface to attest platform state.

---

# Fobnail Project

- Example of vertical integration idea. Execution still in progress.
- We implemented proof of concept.
- We parner with Nitrokey to kickoff next stage of the project with goal of
  productized version sold as feature of Nitrokey tokens.
- You can buy dev kit in our shop (https://shop.3mdeb.com/shop).
- Example application: disk encryption
  + Data theft - accessing secret information contained on disk
  + Installment of unauthorized data - files on disk are overwritten or new
    files are created
- Key protection
  + Disk encryption key is off platform, it is on Fobnail Token
  + Remote attestation to Fobnail is need to obtain encryption key
- Platform integrity
  + Fobnail cryptographically bound to TPM

---

# TwPM

.center[.image-60[![](/img/twpm_lpc.png)]]

.center[https://twpm.dasharo.com]

- Trustworthy Platform Module project aims to increase the trustworthiness of
  the traditional TPM module (hence the TwPM), by providing the open-source
  firmware implementation for the TPM device, compliant to the TCG PC Client
  Specification.

---

# TwPM

.center[.image-70[![](/img/regs_module.svg)]]

- Example of enabling new family of product lines based on principles of open
  development and trustworthiness.
- Goals was to use Microsoft reference TPM implementation on STM32 MCU with SPI
  interface and FPGA for handling signal conversion from LPC to SPI
- Conclusion: maturity of open-source toolchains for FPGA is far from usable in
  practical applications

---

# Dasharo Tools Suite

.center.image-99[![](/img/dts-logo.jpg)]

- Set of tools and scripts running in minimal Linux environment
  + https://docs.dasharo.com/dasharo-tools-suite/overview
- **Vision**
  + **_Versatility_**: Swiss army knife for Dasharo users and the open-source
    firmware community, providing a broad range of tools and scripts that
    simplify firmware operations.
  + **_Simplified Deployment_**: Efficient firmware deployment, updates and
    recovery to improve open-source firmware adaptability.
  + **_User-friendly Interface_**: Shiny, beautiful, and most importantly,
    user-friendly interface for sensitive operations related to firmware.
  + **_Diagnostics and System Verification_**: Accessible trustworthiness
    verification, assisting in platform security features provisioning and
    attestation.

---

# Dasharo HCL

.center[.image-70[![](/img/dasharo_hcl.png)]]

- Example of compliance verification tool.
- We need better collaboration and integration with:
  + OpenBenchmarking.org
  + linux-hardware.org
  + bsd-hardware.info
- Dasharo HCL is part of Dasharo Tools Suite:
  https://docs.dasharo.com/dasharo-tools-suite/documentation/#hcl-report

---

# Dasharo Openness Score

- Example of giving users tools to compare various distributions of firmware.
- Dasharo Openness Score is a tool designed to quantify the openness of firmware
  images, providing insights into the ratio of open-source to closed-source
  components.
- Python, MIT licensed, https://github.com/Dasharo/Openness-Score
- **Vision**
  + **_Universal Standard_**: Establish Dasharo Openness Score as the benchmark
    for firmware openness.
  + **_Visual Clarity_**: Provide visually appealing and easily understandable
    results.
  + **_Integration and Engagement_**: Embed within CI/CD processes and regularly
    update in community platforms.
  + **_Certification Component_**: Make it a pivotal element of the Dasharo
    Certification Program.
  + **_Transparency in Open-Source_**: Create a clear measure of openness in the
    open-source firmware community.

---

# Lesson learned

- We have to meet as often as possible with creative and maker goals in mind
  + we are challenged by deadlines and continues lack of time excuses
  + there is no lack of time just bad time management
- We have to listen more of our customers to shape vision of projects and
  products
- We have to challenge ourselves by roadmaps otherwise we will always have
  excuses for adding more to the release
  + those are not my words, those are words of Richard Stallman: roadmaps and
    execution
- We have to talk more often with business stakeholders
  + consider what they saying and try to solve their bigger painpoints
- Delivering engineering PoC is too far from moving the ecosystem forward.
  + We need rapid compliance verification.
- We can't solve all problems for free
  + without fuel we will not go too far
- There is definitely more to do but we have to grow privacy-respecting and
  security-concious ecosystem to make Qubes OS thrive.

---

class: center, middle, intro

# Q&A
