# Title: TrenchBoot - the only AEM-way to boot Qubes OS

## Session Type

Speaker at location 30 minutes

## Abstract

Qubes OS Anti Evil Maid [AEM](1) heavily depends on the availability of the
Dynamic Root of Trust for Measurement (D-RTM) technologies to prevent the Evil
Maid attacks[2]. However, the project hasn't evolved much since the beginning
of 2018 and froze on the support of TPM 1.2 with Intel TXT in legacy boot mode
(BIOS). Because of that, the usage of this security software is effectively
limited to older Intel machines only.  Some attempts were already made to
support AMD and TPM 2.0 by 3mdeb[3], however the work suffered from lack of
business justification and stopped at porting AEM scripts to use TPM 2.0. But a
successfull demo of AMD D-RTM with Qubes OS has been shown on Qubes OS
minisummit 2020[4]. This year the efforts are traditionally continued.

The presentation will describe the project plan of improving and extending the
Qubes OS AEM with TrenchBoot[5] covering both Intel and AMD hardware, TPM 1.2
and 2.0. The goal is to unify the D-RTM early launch and Anti Evil Maid
software to secure the Qubes OS boot process for basically any hardware device
(as long as it supports the required technologies). The presenter will give
detailed overview of project phases and tasks to be fulfilled as well as the
cost outline. At the end a short demo of Qubes OS AEM with TrenchBoot on Dell
OptiPlex 7010/9010 with Intel TXT and TPM1.2 will be shown.

[1] https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html
[2] https://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html
[3] https://github.com/3mdeb/qubes-antievilmaid-amd/pull/1/files
[4] https://www.youtube.com/watch?v=rM0vRi6qABE
[5] https://trenchboot.org/

## Description (optional and publicly visible)

<!-- taken from https://docs.dasharo.com/projects/trenchboot-aem/#abstract -->

The firmware is the heart of the security of a given system and should always
be up-to-date to maintain the computer's security. However, being up to date
does not prevent the firmware vulnerabilities from appearing. The Static Root
of Trust (SRT) like Unified Extensible Firmware Interface (UEFI) Secure Boot
and measured boot provided by the firmware is not always sufficient to
establish a secure environment for an operating system. If the firmware is
compromised, it could inject malicious software into operating system
components and prevent the machine owner from detecting it. Silicon vendors
implement alternative technologies to establish a Dynamic Root of Trust (DRT)
to provide a secure environment for operating system launch and integrity
measurements. Either from SRT or DRT, these integrity measurements can be used
for operating system attestation. However, DRT technologies are designed to
provide the ability to establish a secure environment for integrity
measurements at any arbitrary point of time instead of relying on the firmware,
which requires machine reset to establish the aforementioned secure
environment.

The usage of Dynamic Root of Trust technologies like Intel Trusted Execution
Technology (TXT) or AMD Secure Startup becomes more and more significant, for
example, Dynamic Root of Trust for Measurement (D-RTM) requirements of
Microsoft Secured Core PCs[6]. D-RTM hasn't found its place in open-source
projects yet, but that gradually changes. The demand on having firmware
independent Roots of Trust is increasing, and projects that satisfy this demand
are growing, for instance, TrenchBoot. TrenchBoot is a framework that allows
individuals and projects to build security engines to perform launch integrity
actions for their systems. The framework builds upon Boot Integrity
Technologies (BITs) that establish one or more Roots of Trust (RoT) from which
a degree of confidence that integrity actions were not subverted. The project
has grown a lot thanks to the previous NLnet NGI0 PET[7] grant and now it looks
for further expansion into extensive use of the DRT technologies in open-source
and security-oriented operating systems like Qubes OS. Qubes OS Anti Evil Maid
(AEM) software heavily depends on the availability of the D-RTM technologies to
prevent the Evil Maid attacks. However, the project hasn't evolved much since
the beginning of 2018 and froze on the support of TPM 1.2 with Intel TXT in
legacy boot mode (BIOS). Because of that, the usage of this security software
is effectively limited to older Intel machines only. TPM 1.2 implemented SHA1
hashing algorithm, which is nowadays considered weak in the era of
forever-increasing computer performance and quantum computing. The solution to
this problem comes with a newer TPM 2.0 with more agile cryptographic
algorithms and SHA256 implementation by default.

The initial AEM implementation relied on the Trusted Boot[8], Intel's reference
implementation of Intel TXT. It never had any plans to support AMD processors.
TrenchBoot is filling this gap, supporting both Intel and AMD hardware which
makes it an ideal target to replace Trusted Boot in Qubes OS AEM
implementation. Furthermore, the project grant would be used to implement the
missing pieces in the Qubes OS AEM software to cover the AMD and Intel support
for both TPM 1.2 and TPM 2.0.

[6] https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure#what-makes-a-secured-core-pc
[7] https://nlnet.nl/project/OpenDRTM/
[8] https://sourceforge.net/p/tboot/wiki/Home/

## Notes (optional, not publicly visible, only for organizers)

None

## Duration

30 min
