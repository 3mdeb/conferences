class: center, middle, intro

# Introduction Day 1

### Qubes OS mini-summit 2021

## Piotr Król

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---

# Mini-summit history

* First mini-summit happen in 2019 in Gdansk 3mdeb office
  - by coincidence it happen Marek came to 3mdeb as trainer to teach our Linux
    Kernel developers
  - we had to leverage that situation and quickly decided about creating what
    is now called Qubes OS mini-summit
  - there was no recordings, but presentations area available on our website:
    https://3mdeb.com/events/#Qubes-OS-and-3mdeb-minisummit
* Second event was held virtually in 2020
  - it was purely virtual event, videos and presentations can be found here:
  https://3mdeb.com/events/#Qubes-OS-and-3mdeb-minisummit
  - we expand our reach through public Youtube stream and AMA at the
  end of each minisummit day

---

# What changed since last year?

* We were able to coordinate some joint marketing with Qubes OS Team:
  https://www.qubes-os.org/news/2021/07/30/minisummit-agenda/
* We get through little bit more formal CfP
* We were able to get more talks from community members and Qubes OS Team
* Talks touch other areas then security, we will talk about Qubes OS future,
  UX, backups, cryptocurrency and many more
* Overall we hope you will enjoy this event
  - feel free to provide feedback

---

# Event organization

* This is 2 day event
  - August 3rd 2021
  - August 10th 2021
* Each day has 2 parts:
  - 6PM-9:45PM UTC - lectures and discussion focused on presented topics and not only
  - 9:45PM UTC - vPub, informal after-party with adult beverages allowed

---

# Day 1 organization

* 06:00-06:15 PM UTC - this introduction
* 06:15-06:00 PM UTC - "Qubes OS 4.1 highlights" by Marek Marczykowski-Górecki
* 07:00-07:45 PM UTC - "First Impressions Count: Onboarding Qubes Users Through an Integrated Tutorial" by deeplow
* 07:45-08:15 PM UTC - break
* 08:15-09:00 PM UTC - "Wyng-backups: revertible local and remote known safe Qubes OS states (including dom0)" by Thierry Laurion
* 09:00-09:45 PM UTC - "SRTM and Secure Boot for VMs" by Piotr Król

---

# Future ideas

* provide better historical statistics

---

# Notes

- Any wireguard VPN support in sys-net for 4.1?
- any ideas an AMD-SEV for securing VMs?
- What about mirageOS firewall?
- what is the most-tested modern laptop for running Qubes on (a) Intel and (b) AMD Ryzen?
    - Lenovo X1 Carbon
    - S0ix is problem
    - Thinkpads tXXX
    - System76 looking for Qubes OS support
    - HP - random laptop with AMD
- What is the future of Snaps, Flatpak, and AppImage features to make them easier and efficient?

???

https://forum.qubes-os.org/t/a-proposal-for-independent-security-standards-body/5411
http://libgen.li/item/index.php?md5=573B5B507152242DEC7397652588081A
https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/
https://textslashplain.com/2021/06/02/leaky-abstractions/
https://www.crowdsupply.com/libre-risc-v/m-class/updates/openpower-eula-released-fosdem-and-more
https://forum.qubes-os.org/t/kernel-implosion-support-needed/5414
https://en.wikipedia.org/wiki/Gorgon_Stare
https://privacywonk.net/2014/11/cybersecurity-as-realpolitik-by-dan-geer.php

stacktrust says:"Misrepresentation is using disinformation to frustrate data
fusion on the part of whomever it is that is watching you. Some of it can be
low-tech, such as misrepresentation by paying your therapist in cash under an
assumed name. Misrepresentation means arming yourself not at Walmart but in
living rooms. Misrepresentation means swapping affinity cards at random with
like-minded folks. Misrepresentation means keeping an inventory of
misconfigured webservers to proxy through. Misrepresentation means putting a
motor-generator between you and the Smart Grid. Misrepresentation means using
Tor for no reason at all. Misrepresentation means hiding in plain sight when
there is nowhere else to hide. Misrepresentation means having not one digital
identity that you cherish, burnish, and protect, but having as many as you can.
Your fused identity is not a question unless you work to make it be. Lest you
think that this is a problem statement for the random paranoid individual
alone, let me tell you that in the big-I Intelligence trade, crafting good
cover is getting harder and harder and for the exact same reasons:
misrepresentation is getting harder and harder. If I was running field
operations, I would not try to fabricate a complete digital identity, I'd
"borrow" the identity of someone who had the characteristics that I needed for
the case at hand."

https://www.sli.do/pricing?plan=annual

Qubes OS 4.1
- is it possible and make sense to have some authorization of policy calls? (e.g. TOTP)
- what are the most used policies?
- how long was 4.1 release cycle?
- when new release is planned?
- what is the purpose of audio subsystem isolation?
    - does it help to support some specific audio hw configs?
- USBIP: this was quite popular in the past, but what is the development of it right now? What is the future of it?
- GRUB2: enables also trenchboot, what may make sense in Qubes OS context
- what is the support of debian for GUI qube

deeplow first try o Qubes OS
- we should always think if what we talking about is not too complex
- maybe OST2 is also the place for Qubes OS training?
- Electron based application should have little memory and lot of swap

wyng:
- what is the security of backups
- what are the concerns about SHA256?

What we should improve next time:
- respect timeline
- youtube for questions is not the best place since it requires google account

---
