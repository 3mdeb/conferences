class: center, middle, intro

# Automating Low-Level Firmware Validation with Robot Framework

### FOSDEM 2025

### Testing and Continuous Delivery

## Maciej Pijanowski

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
src="/remark-templates/3mdeb-presentation-template/images/maciej_pijanowski.png"
width="220px" style="margin-top:-50px"> ]

.center[Maciej Pijanowski] .center[_Engineering Manager_] .right-column50[

- Over 8 years in 3mdeb
- Open-source contributor
- Interested in:
  + build systems (e.g., Yocto)
  + embedded, OSS, OSF
  + firmware/OS security

]

.left-column50[

- <a href="https://twitter.com/macpijan">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/x.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @macpijan
    </a>
- <a href="mailto:maciej.pijanowski@3mdeb.com">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/email.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      maciej.pijanowski@3mdeb.com
    </a>
- <a href="https://www.linkedin.com/in/maciej-pijanowski-9868ab120">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/maciej-pijanowski-9868ab120
  </a>

]

---

# Who we are ?

.center[
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)]
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)]
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/lvfs.png)]
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)]
]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

- coreboot licensed service providers since 2016 and leadership participants
- UEFI Adopters since 2018
- Yocto Participants and Embedded Linux experts since 2019
- Official consultants for Linux Foundation fwupd/LVFS project since 2020
- IBM OpenPOWER Foundation members since 2020

---

# Agenda

- History
- Dasharo OSFV and RF
- Hardware support
- Interfacing with hardware
- Example scenarios
- Q&A

---

# History

.center.image-99[![](/img/osfv.png)]

- We've been using OSFV at least since 2018
  + when validating PC Engines coreboot releases on a monthly basis
  + executed over **50k** tests
  + publicly releasing **150+** binaries of open-source firmware
- Initially, it was an internal project

---

# Dasharo OSVF

.center[https://github.com/Dasharo/open-source-firmware-validation]

- Published as open-source project Sep 2023 (small part of it earlier)
- Use cases of Dasharo OSFV
  + validation of (open-source) firmware
    * can be used for any firmware, really
  + testing Dasharo firmware releases
  + test-driven bug fixing (and adding new features)
  + regression testing
    * after introducing new features
    * after major changes (update base from upstream project)
  + mainly Dasharo with UEFI payload right now
- Scripts written in:
  + mostly Robot Framework (keywords, test suites)
  + some Python (sometimes more suitable than RF)
  + shell scripts (mostly some wrappers for test execution)

???

- Main purpose
- Using Robot Framework as a base

- Use cases
  + validation of Dasharo-related tools (Dasharo Tools Suite, Dasharo
    Configuration Utility)
    * where possible, in QEMU

- Key Features of OSFV:
  + **Hardware Compatibility Testing**: audio, cpu, fan, network, docking
    stations, displays, network, thunderbolt, USB and more
  + **Performance and Stability Testing**: boot time, cpu frequency and
    temperature, power cycle testing
  + **Dashro Security Features Testing**: UEFI Secure Boot, measured boot, TPM,
    verified boot, TCG OPAL, ME, DMA protection and more
- To maximize use of Dasharo OSFV you need dedicated infrastructure

---

# Robot Framework

- Robot Framework is a generic open source automation framework
- It can be used for test automation and Robotic Process Automation (RPA)
- Used widely for web apps testing (with Selenium), and many more
- Used by OpenBMC (firmware, embedded Linux) for test automation
  + https://github.com/openbmc/openbmc-test-automation
- Active community, quality documentation
  + https://robotframework.org/#community
  + https://docs.robotframework.org/docs
- Robot Framework Conference
  + https://robocon.io/

.center.image-20[![](/img/Robot-framework-logo.png)]

---

# Supported Platforms

.center[
  .image-30[![](/img/VP4600.png)]
  .image-30[![](/img/NovaCustom-V54-Series-1.png)]
]
.center[
  .image-30[![](/img/apu4d4.png)]
  .image-40[![](/img/qubes_modern_desktop/msi_pro_z690a.png)]
]

???

Let's see what kind of hardware we are interfacing with the most

---

# OSFV Lab

.center.image-70[![](/img/osfv_arch.png)]

???

We have two more options, not displayed here:
- PiKVM + RTE + Sonoff
- PiKVM + Sonoff

---

# Power control

.left-column50[
.center.image-50[![](/img/osfv_sonoff_r26.png)]

- WiFi plug with custom firmware
- https://tasmota.github.io/docs/devices/Sonoff-S26-Smart-Socket/
]

.right-column50[
.center.image-60[![](/img/rte.jpg)]

- DC relay
- OSHW control board
- HTTP API to control gpio/power
- https://github.com/3mdeb/rte-schematics
- https://github.com/3mdeb/RteCtrl
]

---

# Test execution interface

- Output
  + gather logs via serial port
  + SSH
- Input
  + serial port
  + USB keyboard emulation (via PiKVM)
  + SSH

.center.image-50[![](/img/rf_test_control.png)]

---

# GPIO control

- Power / reset button
- Power LED status
- Custom GPIOs

.center.image-80[![](/img/msi_z690_lab_SPI_RTE.jpg)]

---

# Firmware flashing

.center.image-40[![](/img/pomona_clip_connected_to_flash_chip.jpg)]

---

# osfv_cli - developer usage scenario

https://github.com/Dasharo/osfv-scripts/tree/main/osfv_cli

.code-13px[```bash

# Reserve platform

osfv_cli snipeit check_out --rte_ip $RTE_IP

# Read backup firmware

osfv_cli rte --rte_ip $RTE_IP flash read --rom backup.rom

# Flash new firmware

osfv_cli rte --rte_ip $RTE_IP flash read --rom backup.rom

# Enable power supply

osfv_cli rte --rte_ip $RTE_IP pwr psu on

# Get logs from serial

osfv_cli rte --rte_ip $RTE_IP serial

# Reset platform

osfv_cli rte --rte_ip $RTE_IP pwr reset
```]

???

We expose these hardwaare interfaces via CLI tool allowing developers to
control the state of the devices in the lab

---

# osfv_cli integration

* Integrate low-level hardware operations into Python libraries
* Reuse the same libraries by test framework and CLI tool

.center.image-80[![](/img/osfv_cli_after.png)]

---

# Example test scenario

.center.image-80[![](/img/dasharo_press_key.png)]

---

# Example test scenario

.center.image-80[![](/img/dasharo_main_page.jpeg)]

---

# Example test scenario

.center.image-80[![](/img/dasharo_features.jpeg)]

---

# Example test scenario

.center.image-80[![](/img/dasharo_sec_opts.jpeg)]

---

# Example test scenario

* Code

.code-13px[```python
SMM001.001 SMM BIOS write protection enabling (Ubuntu)
    Power On
    ${setup_menu}=    Enter Setup Menu Tianocore And Return Construction
    ${dasharo_menu}=    Enter Dasharo System Features    ${setup_menu}
    ${network_menu}=    Enter Dasharo Submenu    ${dasharo_menu}    Dasharo Security Options
    Set Option State    ${network_menu}    Enable SMM BIOS write    ${TRUE}
    Save Changes And Reset
    Boot System Or From Connected Disk    ubuntu
    Login To Linux
    Switch To Root User
    ${out_flashrom}=    Execute Command In Terminal    flashrom -p internal
    Should Contain    ${out_flashrom}    SMM protection is enabled
```
]

- Run command

.code-13px[```bash
CONFIG=msi-pro-z690-a-ddr5 \
RTE_IP=AAA.BBB.CCC.DDD \
DEVICE_IP=EEE.FFF.GGG.HHH \
FW_FILE=msi_ms7d25_v1.1.4_ddr5.rom \
./scripts/run.sh dasharo-security/smm-bios-write-protection.robot
```]

---

# Running in QEMU

- Spin up QEMU with Dasharo firmware
  + `./scripts/ci/qemu-run.sh graphic firmware`
- Run test
- Observe the robot execution in console
- Observe how the machine is being controlled in the QEMU window

.center.image-90[![](/img/osfv_qemu_run.png)]

---

# Community

* Standard GH issues and PR flow for contributors
  - https://github.com/Dasharo/open-source-firmware-validation
* Join Dasharo Matrix Space
  - https://matrix.to/#/#dasharo:matrix.org
* Join Dasharo OSFV Matrix room
  - https://matrix.to/#/#osfv:matrix.3mdeb.com

---

# Contact us

We are open to cooperate and discuss

- <a href="mailto:contact@3mdeb.com">
    <img src="/remark-templates/3mdeb-presentation-template/images/email.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      contact@3mdeb.com
  </a>

- <a href="https://www.facebook.com/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/facebook.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      facebook.com/3mdeb
  </a>

- <a href="https://x.com/3mdeb_com">
    <img src="/remark-templates/3mdeb-presentation-template/images/x.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @3mdeb_com
  </a>

- <a href="https://www.linkedin.com/company/3mdeb">
    <img src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/company/3mdeb
    </a>

- <a href="https://3mdeb.com">https://3mdeb.com</a>

- <a href="https://cloud.3mdeb.com/index.php/apps/calendar/appointment/yiqxCTTdioPN">
    Book a call
  </a>

- <a href="https://newsletter.3mdeb.com/subscription/PW6XnCeK6">
    Sign up for the newsletter
  </a>

Feel free to contact us if you believe we can help you in any way. We are
always open to cooperate and discuss.

---

<br>
<br>
<br>

## .center[Q&A]

---

# Extras

---

# Getting started with OSFV

- What do I need to learn first?
- How do I run existing test?
- How do I write a new test?
- How do I add support for a new platform?

---

# What do I need to learn first?

- Some basic RF knowledge
  + go through basics in
      [User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html):
  + go through basic
      [RF libraries](https://robotframework.org/robotframework/):
    * `BuildIn`, `Collections`, `Strings`, `Telnet`
    * add them to your bookmarks, you will need them often
  + check out [SSHLibrary](http://robotframework.org/SSHLibrary/SSHLibrary.html)
- Some basic Python knowlednge
  + there are plenty of learning materials, pick your favourite one

???

https://3mdeb.gitlab.io/human-resources/processes/teams/test-automation-team/TAT_newcomer_cheatsheet/

---

# How do I run existing test?

- Consult README for:
  + [supported platforms](https://github.com/Dasharo/open-source-firmware-validation/#supported-platforms)
  + [getting started](https://github.com/Dasharo/open-source-firmware-validation/#getting-started)
  + [running single tests](https://github.com/Dasharo/open-source-firmware-validation/#running-tests)
- Look through existing tests in:
  + `dasharo-compatibility`
  + `dasharo-security`
  + `dasharo-performance`
  + `dasharo-stability`

---

# How do I run existing test?

- Start with QEMU to learn how it works
- Spin up QEMU with Dasharo firmware
  + `./scripts/ci/qemu-run.sh graphic firmware`
- Run test
- Observe the robot execution in console
- Observe how the machine is being controlled in the QEMU window

---

# How do I run existing test?

- Check if selected test is supported by the given platform
- In `platform-configs/qemu.robot`:

.code-11px[```markdown
${CUSTOM_BOOT_MENU_KEY_SUPPORT}=    ${TRUE}
```]

* `In dasharo-compatibility/custom-boot-menu-key.robot`

.code-11px[```markdown
Skip If    not ${CUSTOM_BOOT_MENU_KEY_SUPPORT}    CBK001.001 not supported
```]

* Example on hardware:

.code-11px[```text
$ robot  -L TRACE -v config:protectli-vp4630 -v rte_ip:192.168.10.244 dasharo-compatibility/custom-boot-menu-key.robot

==============================================================================
Custom-Boot-Menu-Key
==============================================================================
CBK001.001 Custom boot menu key :: Check whether the DUT is config... | PASS |
------------------------------------------------------------------------------
CBK002.001 Custom setup menu key :: Check whether the DUT is confi... | PASS |
------------------------------------------------------------------------------
Custom-Boot-Menu-Key                                                  | PASS |
2 tests, 2 passed, 0 failed
==============================================================================
Output:  /home/macpijan/projects/github/dasharo/open-source-firmware-validation/output.xml
Log:     /home/macpijan/projects/github/dasharo/open-source-firmware-validation/log.html
Report:  /home/macpijan/projects/github/dasharo/open-source-firmware-validation/report.html
```]

---

# How do I write a new test?

* Refer to the existing tests
  - `self-tests` are good examples
  - other commonly used tests
      - `dasharo-security/bios-lock.robot`
      - `dasharo-security/me-neuter.robot`
      - `dasharo-security/smm-bios-write-protection.robot`
      - `dasharo-compatibility/network-boot.robot`
      - `dasharo-compatibility/network-boot-utilities.robot`
  - some tests may currently not work or be of a lower quality

???

https://3mdeb.gitlab.io/human-resources/processes/teams/test-automation-team/coding-guideline/#documentation

---

# How do I add support for a new platform?

* Pick a similar board from `platform-config` and adjust it
  - config documentation: `docs/adding-new-platforms.md`
* Power control
  - [RTE](https://3mdeb.com/open-source-hardware/),
    [Sonoff WiFi Smart Plug](https://sonoff.tech/product/smart-plugs/s26/),
    or both (or something else, which is not supported yet)
* Flashing
  - preferably external flashing is supported - like SOIC clip connected to RTE
    all the time
* Serial connection
  - [ser2net service](https://github.com/cminyard/ser2net) to expose serial
    via telnet
* Hardware setup may be complex
  - https://docs.dasharo.com/variants/asus_kgpe_d16/setup/
