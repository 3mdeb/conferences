class: center, middle, intro

# Introduction Day 2

### Qubes OS mini-summit 2021

## Piotr Król

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---


# Event organization

* This is 2 day event
  - August 3rd 2021
  - **August 10th 2021**
* Each day has 2 parts:
  - 6PM-9:45PM UTC - lectures and discussion focused on presented topics and not only
  - 9:45PM UTC - vPub, informal after-party with adult beverages allowed

---

# Day 2 organization

* 06:00-06:15 PM UTC - this introduction
* 06:15-07:00 PM UTC - "Usability Within A Reasonably Secure, Multi-Environment System" by Nina Alter
* 07:00-07:45 PM UTC - "Qubes OS Native App Menu: UX Design and Implementation" by Marta Marczykowska-Górecka and Nina Alter
* 07:45-08:15 PM UTC - break
* 08:15-09:00 PM UTC - "A brief history of USB camera support in Qubes OS" by Piotr Król
* 09:00-09:45 PM UTC - "How to setup BTC and XMR cold storage in Qubes OS" by Piotr Król

---

# Questions from Day 1

- Any wireguard VPN support in sys-net for 4.1?
- any ideas an AMD-SEV for securing VMs?
- What about mirageOS firewall?
- What is the future of Snaps, Flatpak, and AppImage features to make them easier and efficient?

---

# Questions from Day 1

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

---

# Questions from Day 1

wyng:
- what is the security of backups
- what are the concerns about SHA256?

email:
- hello, I'm trying to chat on your live stream but it's impossible. So I send
  you my question by email. If mafia or cartels or police or rebels want to
  access my qubesOS, is there a way I could open it up and show them my VMs
  without the sensible ones that I would like to hide? Like having some
  sensible VMs hidden and only unlockable by using a special shortcut and a
  password? It this possible somehow or should I just hope this feature will be
  added in the future? Thank you in advance. Take care


---

# Questions from Day 2

- For some motherboards there is workaround to solve not working USB problem, by manually creating sys-usb qube and set permissive mode to USB controller there.
- ​What are security risks with this and what user can do to reduce the risk?
- will there be any sys-usb changes to make it a bit easier to use for desktop users? (ie using usb kb/mice)


XMR/BTC cs wallet suggestions
- /src/local
- think about using dispoable vm
- ​Trust only needs to be in cold storage correct?
- ​If the view only wallet is malicious then it would be picked up by the cold wallet in the amount and address the crypto is sent to?

https://01.org/projectceladon/about
https://virgil3d.github.io/
https://github.com/renchenglei/LookingGlass/commit/42f52c973937c64ff1ee50ba6b0f199ddf1a6f5d
https://discord.gg/xCkJ23pH
https://forum.level1techs.com/t/how-to-sr-iov-mod-the-w7100-gpu/164186
https://looking-glass.io/

https://projectacrn.github.io/latest/tutorials/gpu-passthru.html
https://projectacrn.github.io/2.0/developer-guides/GVT-g-porting.html
https://wiki.xenproject.org/wiki/Hyperlaunch
https://www.youtube.com/watch?v=Xwtq2Q0ylj0

Other idea: create mailing list to discuss complex topics, but instead of talk them through vPubs, discussion have to be focused



--
