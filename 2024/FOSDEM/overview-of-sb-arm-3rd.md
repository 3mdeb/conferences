# Title

Overview of Secure Boot state in the ARM-based SoCs: 3rd edition

# Abstract

In the ARM world, Secure Boot (aka Verified Boot) is typically a BootROM
feature, which allows for verification of the loaded binary (firmware,
bootloader, Linux kernel) before executing it. The main idea is to prevent
unauthorized code from running on our platform. The general approach is similar
across vendors, but this area has no standardization.

This is the 3rd edition [1][2] of such an overview. During the presentation, we
will check the status of the Secure Boot feature on ARM SoCs that were shown a
year ago, and then we will expand this by describing examples on Rockchip RK35xx
and RaspberryPi boards. The knowledge contained in this talk should help
developers integrate Secure Boot into their platforms, contributing to increased
security in the world of embedded devices.

[1] https://archive.fosdem.org/2021/schedule/event/tee_arm_secboot/
[2] https://archive.fosdem.org/2023/schedule/event/arm_secure_boot_2/
