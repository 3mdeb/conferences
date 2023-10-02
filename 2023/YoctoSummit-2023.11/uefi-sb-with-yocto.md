# Title

Dealing with UEFI Secure Boot support using Yocto Project

# Abstract

UEFI Secure Boot, a standard within the UEFI framework, enhances embedded
platform security by verifying signatures for loaded images in the UEFI BIOS.
However, integrating it into a project involves challenges such as ensuring the
level of UEFI specification compliance that UEFI BIOS implementation on a given
hardware target provides, planning for certificate rotation to maintain
security, and seamlessly integrating CI/CD pipelines for component signing. In
the upcoming discussion, I will explore strategies and solutions for resolving
these challenges within Yocto-based projects, demonstrating how to successfully
implement UEFI Secure Boot to bolster platform security.

# Description

This presentation builds upon my earlier work [1], which introduced the basics
of using the meta-secure-core [2] layer. Beginning with a brief recap of UEFI
Secure Boot, I will delve into the continued efforts outlined in the previous
presentation. I'll provide insights into my solutions for the discussed
challenges and demonstrate the professional implementation of UEFI Secure Boot
support in production environments. The primary objective is to raise awareness
among the audience about the comprehensive process of implementing this critical
functionality in ongoing projects. This encompasses everything from analyzing
the UEFI BIOS to seamless integration and long-term maintenance, all achieved
with the support of the Yocto Project wich I will show using meta-dts [3] layer.

[1] https://pretalx.com/yocto-project-summit-2022-11/talk/KJDAFF/
[2] https://github.com/jiazhang0/meta-secure-core
[3] https://github.com/Dasharo/meta-dts
