# Title

Enabling coreboot on Talos II

# Abstract

In a world when it gets harder and harder to even start executing instructions
on main CPU without some kind of blob, OpenPOWER gives hope for open-source
enthusiasts. Talos II is an example of OpenPOWER platform, stuck somewhere
between server and PC. While it already has open-source firmware, that didn't
stop us from adding support for it to coreboot. This subject was already
presented on numerous occasions (OSFC 2020, OpenPOWER Summit 2020 and OpenPOWER
Summit 2021), but this time it is done by someone who spent significant amount
of time working on that code, so the talk will be depicted from more technical
point of view.

This presentation will compare existing open firmware stack with coreboot. Some
parts of the existing firmware (code that runs on on-chip microcontrollers,
because SoC is much more than just the main, OS-visible cores) are reused by
coreboot. Those will be briefly described, along with how coreboot interacts
with them and what debugging options are available. Obstacles (not always
technical) encountered along the way and how we dealt with them will also be
discussed.
