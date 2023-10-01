Title:
FIDO Device Onboarding: Late-binding Provisioning & Tales from the Trenches of
Bleeding Edge Tech

Abstract:
This talk explores the role of FIDO Device Onboarding [1] in strengthening the
device provisioning process, emphasizing both its security and extensibility.
I'll also share my personal experience and challenges faced while implementing
the fido-device-onboard-rs [2] project in the YOCTO environment, offering a
practical perspective on working with this promising technology

Description:
In this presentation, we'll delve into how FDO [1] offers innovative solutions
to prevalent challenges in embedded device onboarding. We'll explore existing
implementations of this protocol and their compatibility within the Yocto
Environment. A closer look will be given to the fido-device-onboard-rs [2]
project by Fedora IoT, which I employed in a recent project. I'll share
firsthand challenges faced in integrating it with Yocto, especially the
nuances of cross-compiling Rust and the solutions available in OpenEmbedded
layers. I'll conclude the presentation by showcasing a live demonstration of
the protocol in action on a Raspberry Pi platform.

[1] https://fidoalliance.org/specs/FDO/FIDO-Device-Onboard-RD-v1.1-20211214/FIDO-device-onboard-spec-v1.1-rd-20211214.pdf
[2] https://github.com/fedora-iot/fido-device-onboard-rs
