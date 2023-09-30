class: center, middle, intro

# How to setup BTC and XMR cold storage in Qubes OS

### Qubes OS mini-summit 2021

## Piotr Król

<img src="remark-templates/3mdeb-presentation-template/images/logo.png" width="150px" style="margin-left:-20px">

---
# `whoami`

.center[<img src="remark-templates/3mdeb-presentation-template/images/piotr_krol.jpg" width="150px">]

.center[Piotr Król]
.center[_3mdeb Founder & CEO_]

.left-column55[
* coreboot contributor and maintainer
* Conference speaker and organizer
* Trainer for military, government and industrial organizations
* Former Intel BIOS SW Engineer
]

.left-column45[
* 12yrs in business
* Qubes OS user since 2016
* C-level positions in<br>
.image-30[![](remark-templates/3mdeb-presentation-template/images/3mdeb.svg)]
.image-30[![](remark-templates/3mdeb-presentation-template/images/lpnplant.png)]
.image-30[![](remark-templates/3mdeb-presentation-template/images/vitro.svg)]
]

---
# Who we are ?

.center[.image-15[![](remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)] .image-15[![](remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)] .image-15[![](remark-templates/3mdeb-presentation-template/images/lvfs.png)] .image-15[![](remark-templates/3mdeb-presentation-template/images/yocto.png)]]
.center[.image-35[![](remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

* coreboot licensed service providers since 2016 and leadership participants
* UEFI Adopters since 2018
* Yocto Participants and Embedded Linux experts since 2019
* Official consultants for Linux Foundation fwupd/LVFS project since 2020
* IBM OpenPOWER Foundation members since 2020
  - Our Firmware Engineer Michał is chair of SSWG since 2021

---
# Agenda

* Presentation goal
* Terminology
* Architecture
* BTC
  - wallet
  - btc-cs VM preparing
  - online watch-only wallet preparing
  - rx/tx coins
* Qrexec and Qubes RPC 
* SendToSign and SignTxn RPC services
* BTC Demo
* XMR
  - a/a
* Future ideas
* Q&A

---

# Presentation goal

.center[.image-20[![](images/xmr.jpg)] .image-20[![](images/btc.png)]]

### .center[**To demo offline wallet for BTC and XMR with Qubes OS**]

* _**Disclaimer**: We are by no means cryptocurrency experts and you should
not rely on this presentation as source of secure offline wallet configuration.
Please consult domain experts. We are not responsible for any damage caused by
using following information._


.footnote["cryptocurrency monero XMR" by bastamanography CC BY-NC-SA 2.0.]
<br>
.footnote["File:Bitcoin Cash.png" by Amaury Sechet CC0 1.0]

---

# What is cold storage?

.center[.image-65[![](images/cold_storage.jpg)]]

* **Cold storage** is an offline wallet used for storing cryptocurrency.
  - no remote access, reduced attack surface
  - public key is used for watching-only wallet
  - every transaction is signed in cold wallet

.footnote["Diagram of a Cold Storage System (1920)" by Eric Fischer CC BY 2.0]

---

# Architecture

.center[.image-50[![](images/arch.svg)]]

* Architecture consist of offline and online wallet
  - offline wallet can sign transactions before broadcasting online
  - offline wallet can generate payment requests
  - online wallet is watch-only to see transaction history
* Limitation
  - definitely not the setup for high frequency traders, although there is
    place for improvements

---

# Electrum

.center[.image-20[![](images/electrum.png)]]

* Thomas Voegtlin in November 2011
* Wallet is written mostly in Python and its source code is available on
  Github:
https://github.com/spesmilo/electrum
* For following tutorial we used v4.1.5 AppImage version
* Meet our requirements
  - OS: Linux
  - Knowledge: Experienced User
  - License: Open Source
  - Lightweight
* We decided that Electrum meets all those criteria with great balance between
  privacy, transparency and feature-richness

---

# `btc-cs` vm using minimal template

* Minimal templates contain only most important packages
  - save resources
  - reduce attack surface

```shell
(dom0)$ sudo qubes-dom0-update qubes-template-debian-10-minimal
(dom0)$ qvm-prefs debian-10-minimal netvm sys-firewall
(dom0)$ qvm-run -u root debian-10-minimal xterm
```

* Install Electrum dependencies
```shell
(debian-10-minimal)$ apt update
(debian-10-minimal)$ apt install fuse
```

* Create `bt-cs` VM
```shell
(dom0)$ qvm-create --label black --property memory=128 --property maxmem=256
--template debian-10-minimal btc-cs
```

---

# Electrum signature verification

```shell
(trustedvm)$ export ELECTRUM_URL=https://download.electrum.org/4.1.5
(trustedvm)$ wget ${ELECTRUM_URL}/electrum-4.1.5-x86_64.AppImage
(trustedvm)$ wget ${ELECTRUM_URL}/electrum-4.1.5-x86_64.AppImage.ThomasV.asc
(trustedvm)$ wget ${ELECTRUM_URL}/electrum-4.1.5-x86_64.AppImage.sombernight_releasekey.asc
(trustedvm)$ export \
ELECTRUM_KEYS=https://raw.githubusercontent.com/spesmilo/electrum/master/pubkeys
(trustedvm)$ gpg --fetch ${ELECTRUM_KEYS}/ThomasV.asc
(trustedvm)$ gpg --fetch ${ELECTRUM_KEYS}/sombernight_releasekey.asc
```

* Fingerprint can be compared with https://electrum.org/#about and Github
identity.


```shell
(trustedvm) $ gpg --verify electrum-4.1.5-x86_64.AppImage.ThomasV.asc \
electrum-4.1.5-x86_64.AppImage
(trustedvm) $ gpg --verify electrum-4.1.5-x86_64.AppImage.sombernight_releasekey.asc \
electrum-4.1.5-x86_64.AppImage
```

* `trustedvm` should be sufficiently trusted by user to verify signatures


???

```shell
gpg: Signature made Mon 19 Jul 2021 08:22:33 PM CEST
gpg:                using RSA key 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6
gpg: Good signature from "Thomas Voegtlin (https://electrum.org) <thomasv@electrum.org>" [unknown]
gpg:                 aka "ThomasV <thomasv1@gmx.de>" [unknown]
gpg:                 aka "Thomas Voegtlin <thomasv1@gmx.de>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6694 D8DE 7BE8 EE56 31BE  D950 2BD5 824B 7F94 70E6
```

```shell
gpg: Signature made Mon 19 Jul 2021 09:19:58 PM CEST
gpg:                using RSA key 0EEDCFD5CAFB459067349B23CA9EEEC43DF911DC
gpg: Good signature from "SomberNight/ghost43 (Electrum RELEASE signing key) <somber.night@protonmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 0EED CFD5 CAFB 4590 6734  9B23 CA9E EEC4 3DF9 11DC
```

Fingerprint can be compared with https://electrum.org/#about and Github
identity.

---

# Deploy Electrum to `btc-cs`

* Copy Electrum from `anyvm`
```shell
(anyvm)$ qvm-copy electrum-4.1.5-x86_64.AppImage
```

* Choose `btc-cs` as target, and click OK
* Run `btc-cs`
```shell
(dom0)$ qvm-run btc-cs xterm
```

* In `btc-cs` you should be able to run Electrum
```shell
(btc-cs)$ cd ~/QubesIncoming/<anyvm>
(btc-cs)$ chmod +x electrum-4.1.5-x86_64.AppImage
```

* Run Electrum in testnet
```shell
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet daemon -d
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet create | tee seed
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet load_wallet
```

---

# List wallets

.center[.image-70[![](images/wallets.png)]]

```shell
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet list_wallets
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet getinfo
```

---

# Online wallet preparation

.center[.image-60[![](images/getmpk.png)]]

* Obtain Master Public Key and copy it to `anyvm`
* Run Electron GUI:
```shell
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet getmpk | tee mpk
(btc-cs)$ qvm-copy mpk
```

---

# Online wallet preparation

.center[.image-70[![](images/electrum1.png)]]

---

# Online wallet preparation

.center[.image-70[![](images/electrum2.png)]]

---

# Online wallet preparation

.center[.image-70[![](images/electrum3.png)]]

---

# Online wallet preparation

.center[.image-70[![](images/electrum4.png)]]

* Most probably `Next` will be not active, this is because of new line at end
of MPK, when you delete it, Electrum can proceed

---

# Online wallet preparation

.center[.image-70[![](images/electrum5.png)]]

---

# Online wallet preparation

.center[.image-90[![](images/electrum6.png)]]

* Information about wallet working in testnet

---

# Online wallet preparation

.center[.image-70[![](images/electrum7.png)]]

* Information about watch-only mode of the wallet

---

# Obtain some coins from testnet

* Create request payment transaction
```shell
(btc-cs)$ ./electrum-4.1.5-x86_64.AppImage --testnet add_request 0.001
{
    "URI": "bitcoin:tb1q22vafahlyg7ndx6t25qkl0nwle9x9pytn72z(...)",
    "address": "tb1q22vafahlyg7ndx6t25qkl0nwle9x9pytn72znd",
    "amount_BTC": "0.001",
    "amount_sat": 100000,
    "expiration": 3600,
    "is_lightning": false,
    "message": "",
    "status": 0,
    "status_str": "Expires in about 1 hour",
    "timestamp": 1628289375
}
```

* Go to testnet faucet e.g.: https://testnet-faucet.mempool.co/ and send
0.001BTC to the address from request `tb1q22vafahlyg7ndx6t25qkl0nwle9x9pytn72znd`
* You should receive tBTC in online wallet

---

# Send coins manually

* Click `Pay...->Send`
* Export partial transaction using: `Export->Export to file` from transaction menu
* Copy to `btc-cs`
```shell
(anyvm)$ qvm-copy default_wallet-<txid>.psbt
```

* Sign transaction
```shell
(btc-cs)$ cat ~/QubesIncoming/<anyvm>/default_wallet-<txid>.psbt|base64 \
| ./electrum-4.1.5-x86_64.AppImage --testnet signtransaction - > signed_<txid>.txn
```

* Transfer back to `anyvm`
```shell
(btc-cs)$ qvm-copy signed_<txid>.txn
```

---

# Qrexec and Qubes RPC

.center[.image-80[![](images/qrexec3.png)]]

* Qrexec framework implements communicating between domains
* It is built on top of vchan, Xen library providing data links between VMs
* communication between VMs is set up by dom0
* thanks to the framework RPC client/server are simple scripts
  - `qrexec-client-vm` makes RPC calls to target VM
  - call gets through dom0 and policy is checked
  - script in target VM is executed
  - stdin/stdout can be used to exchange data between client and target VMs

.footnote[https://www.qubes-os.org/doc/qrexec/]

---

# Create RPC service

```shell
(dom0)$ qvm-run -u root btc-cs xterm
```

* Create `/etc/qubes-rpc/test.SignTxn` in `btc-cs`

```shell
#!/bin/sh
ELECTRUM="/home/user/QubesIncoming/fw-dev/electrum-4.1.5-x86_64.AppImage"
argument=$(cat -)
if [ -z "$argument" ]; then
	echo "ERROR: No argument given!"
	exit 1
fi
${ELECTRUM} --testnet signtransaction -- "$argument"
```

---

# Create RPC service

* Create `/etc/qubes-rpc/test.SignTxn` in `dom0`
```shell
$anyvm btc-cs ask
```

* Create `/etc/qubes-rpc/test.SendToSign` in `anyvm`
```shell
#!/bin/sh
cat "$1"
exec cat >&$SAVED_FD_1
```

---

# BTC Demo

.center[
<iframe allow="fullscreen;" frameborder="0" width="600" height="480"
src="https://www.youtube.com/embed/FBtL8tP33U4?rel=0&hd=1">
</iframe>]

---

# Monero CLI Wallet

* Developed by Monero Community
* Written mostly in C++ with source code available on Github:
  https://github.com/monero-project/monero
* For the following tutorial we will use Oxygen Orion v0.17.2.0
* Meet our requirements
  - OS: Linux
  - Knowledge: Experienced User
  - License: Open Source
  - Lightweight

---

# `xmr-cs`

* Create `xmr-cs` based on `debian-10-minimal` template
* Signature verification according to XMR wallet documentation:
  https://monerodocs.org/interacting/verify-monero-binaries/
* Copy XMR CLI wallet to `xmr-cs`
* Start daemon in stagenet mode
```shell
(xmr-cs)$ ./monerod --stagenet
```
* Create wallet by getting following instructions after running
```shell
(xmr-cs)$ ./monero-cli-wallet --stagenet
```

* Set following options in wallet
```shell
set ask-passsword 0
```

---

# XMR watch-only wallet

* Obtain address
```shell
(xmr-cs)$ ./monero-wallet-cli --stagenet \
--wallet-file=/home/user/xmr_stagenet --password "" address \
| grep address | tee address
(xmr-cs)$ qvm-copy address
```

* Obtain private view key
```shell
(xmr-cs)$ ./monero-wallet-cli --stagenet \
--wallet-file=/home/user/xmr_stagenet viewkey
```

* copy private view key from output and transfer to vm where watch-only wallet
  will be created

---

# XMR watch-only wallet

* Use CLI to create watch-only wallet
```shell
(anyvm)$ ./monerod --stagenet --prune-blockchain
(anyvm)$ ./monero-wallet-cli --stagenet --generate-from-view-key xmr_watch-only_wallet
```

* When asked provide address and privet view key
* Wait to synchronize stagenet blockchain
* After synchronizing blockchain you can start mining in `monerod`
```shell
start_mining <address>
```

* When XMR will be mined following message will appear:
```shell
2021-08-09 08:54:12.965 I Found block
<155085fe8df9a587467a5e6cce82b61512fbaef90fb8e669468b2d288a9e10d0> at height
895682 for difficulty: 177850
```

---

# XMR balance

* `balance` command in wallet should give something like this:
```shell
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 6.577195618595, unlocked balance: 0.000000000000 (56 block(s) to
unlock) (Some owned outputs have missing key images - import_key_images needed)
```

* Because XMR has different mechanics then BTC it requires synchronization to
  keep track of balance on watch-only and cold storage
  -  transfers can be monitored by `export_outputs` on watch-only and
     `import_output` on cold storage
  - spent can be monitored by `export_key_images` on cold storage and
    `import_key_images` on watch-only
* You have to wait to see some XMR on `unlocked balance` this may take time (in
  my case 1.5h)

---

# Send XMR manually

.center[.image-80[![](images/xmr_balance.png)]]

* Wallet run following to create transaction

```shell
[wallet 56m3Uc]: transfer 55LTR8KniP4LQGJSPtbYDacR7dz8RBFnsfAKMaMuwUX6aQbBcovzDPyrQF9KXF9tV(..) 1
Wallet password:

Transaction 1/1:
Spending from address index 0
Sending 1.000000000000.  The transaction fee is 0.000063570000

Is this okay?  (Y/Yes/N/No): Y
Unsigned transaction(s) successfully written to file: unsigned_monero_tx
[wallet 56m3Uc]:
```

---

# Send XMR manually

* Copy `unsigned_monero_tx` to `xmr-cs` and sign

.center[.image-60[![](images/sign_transfer.png)]]

* Copy newly created `signed_monero_tx` back to `xmr-cs` and submit transfer

.center[.image-80[![](images/submit_transfer.png)]]

* Please note `signed_monero_tx` file was wallet current working directory

---

# XMR RPC service

```shell
(dom0)$ qvm-run -u root xmr-cs xterm
```

* Create `/etc/qubes-rpc/test.SignXfer` in `xmr-cs`
```shell
#!/bin/sh
XMR_WALLET="/home/user/monero-wallet-cli"
cat - > /home/user/unsigned_monero_tx
xterm -e "${XMR_WALLET} --stagenet --wallet-file=/home/user/xmr_stagenet --password '' sign_transfer"
cat signed_monero_tx
```

* Create `/etc/qubes-rpc/test.SignXfer` in `dom0`
```shell
$anyvm xmr-cs ask
```

* Create `/etc/qubes-rpc/test.SendToSign` in `anyvm`
```shell
#!/bin/sh
cat "$1"
exec cat >&$SAVED_FD_1
```

---

# XMR Demo

.center[
<iframe allow="fullscreen;" frameborder="0" width="600" height="480"
src="https://www.youtube.com/embed/e0WJk1AHOVo?rel=0&hd=1">
</iframe>]

---

# Future ideas

* Confirmation of explicit amount spent in transaction to be signed
* Autostart wallet in daemon mode for real transactions
* Consider VM protection mechanisms
* Private key backups
* Disaster recovery
* Signing PBST vs TXN - recognize with what type of file we dealing with
* Salt stack automation of VM creation
* Combining presented configuration using multisig and keeping one of the keys
  in hardware wallet may improve security of the solution
* Offline wallet software update can be a problem
  - official suggestions saying about complete reinstall
* XMR: improve password handling
* XMR: use RPC instead of cli

---

<br>
<br>
<br>
## .center[Q&A]
