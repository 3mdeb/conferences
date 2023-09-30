class: center, middle, intro

# Status fwupd/LVFS support
# for Qubes OS

### Qubes OS and 3mdeb minisummit 2020

## Norbert Kamiński

<img src="remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Agenda

* fwupd/LVFS - overall information
* Qubes OS support challenges and architecture solutions
* What is done
* Downloading firmware
* Updating firmware
* To Do's
* Q&A

---

# $ whoami

.center[<img src="images/nk-conference.png" width="175px" style="margin-top:-50px">]
.center[Norbert Kamiński]
.center[_Junior Embedded Systems Engineer_]

.left-column50[

- open-source contributor:
  - meta-pcengines
  - meta-virtualization
- scope of interests:
  - embedded Linux
  - virtualization
  - bootloaders

]

.right-column50[

- <a href="mailto:norbert.kaminski@3mdeb.com"><img src="remark-templates/3mdeb-presentation-template/images/email.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> norbert.kaminski@3mdeb.com </a>

- <a href="https://www.linkedin.com/in/norbert-kami%C5%84ski/"><img src="remark-templates/3mdeb-presentation-template/images/linkedin.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> linkedin.com/in/norbert-kami%C5%84ski/ </a>

- <a href="https://www.facebook.com/nkaminski3"><img src="remark-templates/3mdeb-presentation-template/images/facebook.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> facebook.com/nkaminski3 </a>

- <a href="https://twitter.com/asiderr"><img src="remark-templates/3mdeb-presentation-template/images/twitter.png" width="24px" style="margin-bottom:-5px; margin-left:-15px"/> @asiderr </a>

]

---

# Standard fwupd/LVFS architecture

.center[ .image-80[![architecture-plan](images/architecture-plan.png)]]
.footnote[Image source: https://lvfs.readthedocs.io/en/latest/intro.html]

---

# Linux Vendor Firmware Service (LVFS)

* The LVFS is a secure web service that can be used by hardware vendors to upload
firmware archives

* Customers can securely download metadata about the available updates.

* Firmware update files are stored in cabinet archives files, that contain
firmware, metadata and detached signature

![architecture-plan-internet](images/architecture-plan-internet.png)

---

# fwupdmgr and fwupd

* The `fwupdmgr` is a CLI client tool, that allows user to preform the update
process manually

* It takes the role of connector between LVFS database and the
fwupd

* The `fwupd` is a system activated daemon with a D-Bus interface, that can be
used to perform wide upgrades and downgrades according to security policy

.center[ .image-60[![architecture-plan-system](images/architecture-plan-system.png)]]

---

# Qubes OS support challenges

* Virtual machines ( AdminVM (dom0), sys-usb) which handle devices to be flashed have no
internet connection

* UpdateVM must check metadata and provide a update archive for a device

* Update files must be verified at all steps of the download process

* `fwupd` must support the firmware update process divided into three VMs
(UpdateVM, AdminVM , sys-usb)

---

# What is done

* Architecture plan of the fwupd/LVFS support for Qubes OS

* Frame of the update process

* Building the `fwupd` from the source at the AdminVM.

.center[ .image-70[![architecture-plan-qubes](images/work-in-progress.png)]]

---

# Architecture Plan

.center[ .image-65[![architecture-plan-qubes](images/QubesFwupd.png)]]

---

# Downloading firmware

* dom0 and sys-usb are isolated from the network

* Download process is initiated via `qubes-dom0-update`

* `qubes-dom0-update` creates download directory in the UpdateVM

* Then it runs `fwupd-download-updates` in the UpdateVM

.center[ .image-65[![architecture-plan-qubes](images/QubesFwupd2.png)]]

---

# Downloading firmware

* `fwupd-download-updates` downloads metadata and firmware from the LVFS

* Script performs the first step of the validation

* If it is running with `check-only`, it sends only meta data

* Otherwise it download the `.cab` archive and it starts `qubes.ReciveUpdates`

.center[ .image-65[![architecture-plan-qubes](images/QubesFwupd2.png)]]

---

# Downloading firmware

* `qubes.ReciveUpdates` is a symbolic link to the python script </br>
`qubes-receive-updates`

* The script t is responsible for receiving the update files from the UpdateVM

* `qubes-receive-updates` creates the update cache directory for fwupd,
it copies the files and it performs the second step of the validation
.center[ .image-65[![architecture-plan-qubes](images/QubesFwupd2.png)]]

---

# Updating firmware

* We need two `fwupd` daemons to provide the updates to every type of device

* The first daemon is installed to AdminVM and It provides updates to non-USB
devices

* The second daemon is placed on the sys-usb. It allows us to update the
hardware connected via USB
.center[ .image-65[![architecture-plan-qubes](images/QubesFwupd3.png)]]

---

# Updating firmware

* The update process is managed by `qubes-fwupdmgr`

* The `fwupdmgr` takes the hardware information from the daemon and pass
it to `qubes-fwupdmgr`

* If the update is available `qubes-fwupdmgr` uses proper `fwupdmgr` to perform
the firmware update process

.center[ .image-65[![architecture-plan-qubes](images/QubesFwupd3.png)]]
---

# To Do's


* Custom fwupd plugin that will use information from all VMs

* `qubes-fwupdmgr` script that will connect the downloading and
updating firmware

* `.cab` archives validation that will ensure us about the safety of the files

.center[ .image-70[![architecture-plan-qubes](images/work-in-progress.png)]]

---

## .center[Q&A]

