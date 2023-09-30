# Title: Secure firmware updates for Qubes - Status presentation

## Session Type

Speaker at location 30 minutes

## Abstract

The presentation will describe the current status of work on the fwupd [1] port
for Qubes OS. I will present the porting process, the obstacles we encountered
during development, and the work that needs to be done to complete the project.

[1] https://fwupd.org/

## Description (optional and publicly visible)

The security of the whole system is not determined only by the software it
runs, but also by the firmware. Firmware is a piece of software inseparable from
the hardware. It is responsible for proper hardware initialization as well as
its security features. That means that the safety of the machine strongly
depends on the mitigations of vulnerabilities provided by firmware (like
microcode updates, bug/exploit fixes). For these particular reasons,
the firmware should be kept up-to-date.

Nowadays, one of the most popular firmware update software is fwupd/LVFS.
fwupd is a Linux daemon that manages firmware updates of each of your hardware
components that have some kind of firmware. What is more fwupd is open source,
which makes it more trustworthy than proprietary applications delivered by
hardware vendors designed for (only) their devices. This presentation will
describe the process of providing a secure firmware update method for
the Qubes OS community.

## Notes (optional, not publicly visible, only for organizers)

None

## Duration

30 min
