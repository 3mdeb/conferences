class: center, middle, intro

# Tailoring Your Qubes OS Environment: A Developer’s Guide to Leveraging SaltStack 

## Qubes OS Summit 2023

### Piotr Król


<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">

---

# Agenda


* lorem ipsum

---

# Disclaimer (aka legal mumbo jumbo)

.center.image-35[![](/img/qubes_os_disclaimer.png)]

_I am not a SaltStack sage or a Qubes OS guru. The contents of this
presentation are more of a curious exploration than an expert guide. If you
decide to use any materials, knowledge, or scripts shared today and somehow
trigger a digital Armageddon, start a nuclear showdown, or just plain old crash
your system, remember, it's not on me!_

_Use the information at your own risk._

---

# Qubes OS and SaltStack

<center>
.centre.image-10[![](/img/qubesos_logo.png)] .image-50[![](/img/saltstack.png)]
</center>

* **SaltStack** is Apache 2.0 licensed, written in Python configuration management
  and automation tool.
* Utilizes a central management server (Salt Master) to communicate with and
  control target systems (Salt Minions), with an option for masterless
  operation.
  - Masterless configurtion is used by Qubes OS
* Employs a declarative language in YAML to define desired system
  configurations, ensuring consistency and compliance across the
  infrastructure.
* **SaltStack** was aquired by VMware in 2020
* **SaltStack** integration was introducted to Qubes R3.1 (Q1'2016)

---

# SaltStack vs Backup

TODO: meme

* We typically face two situations?
  - clean new deployment
  - migration from previously working configuration
* In case of migration **CaaC (_Configuration as a Code_)** have to face its
  natural opponent: **recovery from backup**.
* There is no officially supported recovery from backup for whole dom0.

???

* There is no officially supported way to rollback whole dom0, just home
  directory
  - there are many threads and complex discussion aroudnd dom0 lvm and
    snapshotting
  - `tasket` and `tlaurion` have some success, which leverage `wyng-backup`,
    but whole solution is not described well enough, so casual user like me
    could leverage that

---

# SaltStack vs Backup

* In case of AppVMs, TemplateVMs and dom0 home directory:
  - Recovery for backup for VMs requiring complex manual provisoning, which is
    hard to write code for, could be better.
  - Both TemplateVM and AppVM need appropriate backup to be in sync.
  - Backups take disk space, which may be limited by using CaaC
  - Applying changes which we track in version control is less error prone,
    stable and reproducible than content of the backup.
  - CaaC is portable between target OSes, backups typically not.
  - CaaC maybe more time consuming.

???

* TemplateVM have to be upgradable otherwise new system may bring template
  upgrade which is is not compatible with what we have in appvm. This maybe not
  an issue if difference in versions is small, but for big difference upgrade
  may be impossible.


---

# SaltStack basics

* Pillars, formulas and grains and other Salt terminology make learning curve
  steep.
* States are defined in `*.sls` files.

```yaml
stateid:
  cmd.run:
    - name: echo 'hello world'
```
* Top files define which states should be applied to which targets.
* Most usage of SaltStack in Qubes OS is not related to Qubes OS specific
  modules and libraries.

???

TODO: explain top and sls files

---

# SaltStack in Qubes OS basics

* `qubesctl` is a tool used to manage and configure Qubes OS using SaltStack.
   In essence it is inter-changeable and an alias for `salt-call --local` and
   contains additional code to apply any required patches.

---

# Declarative configuration

* **Desired outcome** - You specify what you want the final configujration to
  look like, not how to get there. 
* **Idempotency** - Declarative states are idempotent, meaning you can apply
  them multiple times without changing the result beyond the initial
  application.
  - This can be annoying when we we would like to remove some state, we have to
    make sure it is reverted first, otherwise that state is still in the target
    VM.

---

# Developer story

* I'm trying to use SaltStack for Qubes OS and Debian based systems since 2018.
* In any case we are starting with clean Qubes OS installation

---

# Hardware Configuration

.center.image-70[![](/img/dasharo-fidelisguard-z690.jpg)]

* Dasharo FidelisGuard Z690 with 128GB of memory and 2TB NVMe.
* More sophisticated VM configurations we want more memory we need.
* Tested on HP Compaq Elite 8300 32GB RAM and 256GB disk.

???

TODO: read proposal of Qubes OS for VM setup:
https://www.qubes-os.org/news/2022/10/28/how-to-organize-your-qubes/

# How to recover to clean state without system reinstallation

* Remove VMs
* Private volumes revert?
* Reinstall Templates 
* What about dom0? Backup and restore?

---

# How to start?

* Qubes organization (reading [How to organize your
  qubes](https://www.qubes-os.org/doc/how-to-organize-your-qubes/) highly
  recommended)
* What Dom0 customizations I need?


---

# Qubes organization

.center.image-99[![](/img/qubes_organization.svg)]

* Not the most important thing for our purpose, just to have some template.

???

* IMHO building embedded and firmware projects on computer you use for work
  does not make sense. I argue for external build system in intranet.

---

# Dom0 customization

* Apply formulas
* Install templates
* Change Qubes OS defaults
* Install packages
* Setup policy
* Xfce configuration
* Create VMs
* Enable/disable services
* Update templates

---

# Apply formulas

* There are already quite a lot of them in Qubes 4.2-rc3
  - located in /srv/formulas/base
  - GPLv2 licensed
  - download, install and configure VMs using pillar data to define deault nams
    and configuration details
  - update dom0, TemplateVMs and AppVMs
* Some examples:
  - usb-keyboard - setup policy, modify Xen boot params, modify GRUB boot
    params, regenerate grub config
  - vault - install vault AppVM

```shell
sudo qubesctl --show-output state.sls update.qubes-dom0
sudo qubesctl --show-output state.sls qvm.usb-keyboard
```

---

# Install templates

* If we do it from command line it would be `qvm-template install
  TEMPLATESPEC`
* AFAIK there is no `qvm-template` command, so we have to run regular
  command:

```yaml
install debian-12-minimal template:
  cmd.run:
    - name: qvm-template install debian-12-minimal
```

---

# Change Qubes OS defaults

```yaml
set default template:
  cmd.run:
    - name: qubes-prefs --set default_template debian-12-minimal
    - runas: pietrushnic
```

* There are bunch of other options to deal with:
  - clockvm
  - default_kernel
  - default_netvm
  - update_vm
  - others

---

# Install packages

* Packages you may find worth of installing
  - qubes-video-companion-dom0
  - kernel-latest

```yaml
install qubes-video-companion:
  pkg.installed:
    - name: qubes-video-companion-dom0
    - fromrepo: fedora,updates,qubes-dom0-current-testing
    - refresh: True
install other dom0 packages:
  pkg.installed:
    - pkgs:
      - kernel-latest
    - fromrepo: fedora,updates,qubes-dom0-current-testing
    - refresh: True
```

* `pkg` documentation is extensive but most used, are: `pkg.installed`,
  `pkg.removed`, `pkg.managed`, `pkg.latest`

---

# Setup policy

* Policies defining which VMs can communicate via RPC.
* Some of the popular one:
  - SshAgent
  - SplitGpg
  - InputKeyboard/Mouse

```yaml
add SshAgent policy:
  file.prepend:
    - name: /etc/qubes-rpc/policy/qubes.SshAgent
    - text:
      - work vault ask,default_target=vault
      - dev vault allow notify=yes
```

---

# Xfce configuration

* Xfce configuration as code is PITA
  - finding correct property is not easy task
  - naming scheme of properties is not self-explaining
* Best what I was able to find is `xfconf-query` a tool created for
  querying and setting Xfce configuration database.

```yaml
enable left-handed mouse:
  cmd.run:
    - name: xfconf-query -c pointers -p
    /sys-usb_Logitech_USB_Optical_Mouse/Properties/libinput_Left_Handed_Enabled
    -n -t int -s 1
    - runas: pietrushnic
```

* Content of `name` should be one line it was changed for presentation
  readability.

---

# Create VMs

* Clean Qubes OS installation has some VMs created (personal, work,
  vault, untrusted).
* We may have to modify those or create new one.

```yaml
dev vm present:
  qvm.present:
    - name: dev
    - label: blue
    - klass: AppVM
    - template: debian-12-minimal
dev vm prefs:
  qvm.prefs:
    - name: dev
    - autostart: True
dev increase storage size:
  cmd.run:
    - name: qvm-volume resize dev:private 32G
    - runas: pietrushnic
```

* Aparently 32G translate to `32*10^9`, but `qvm-volume` set power of two,
  so calling this second time return error: `32*10^9 < 32002539520`
  - incidental sefty check, but IDK how to handle that correctly

---

# Enable/disable services

* `qvm.service` is used in similar way as `qvm-service` to manage Qubes
  OS specific services srted in VMs

```yaml
enable split-gpg2 service in email:
  qvm.service:
    - name: email
    - enable: split-gpg2-client
```

```yaml
set service for company-vpn VM:
  qvm.service:
    - name: company-vpn
    - enable:
      - network-manager
```

---

# Standard operation procedure (SOP)

* Since nothing is configured on your cleanly installed Qubes OS you have to
  deploy SaltStack scripts somehow.
* CaaC typically won't be public, so there is no way to download it and even
  downloading means some curl/wget or other software.
* Cloning from private repo would require some previous configuration.
* Easiest way seem to be to deliver on USB stck and then copy content to dom0.
  - connect USB/storage with SaltStack scripts
  - connect USB/stotage to untrusted VM
  - copy scripts from untrusted VM to dom0

---

# SOP: Updates

* Before kick any Salt script let's make sure that dom0's and AppVM
  templates are up to date:

  ```shell
  sudo qubesctl --show-output state.sls update.qubes-dom0
  sudo qubesctl --show-output --skip-dom0 --templates state.sls update.qubes-vm
  ```
* The same thing should happen after executing CaaC.
* Logs from template and VM configuration can be found in `/var/log/qubes/mgmy-VMNAME.log`

---

# SOP: Structure of script package

* `*.sls` and `*.top` are named after the target names: dom0,
  debian-12-minimal, dev, etc.
  - this simplify tree organization, but cause some limitation

???

* configure dom0
* install template
* modify template
* create VMs based on template

---

# init.sh

* Following is an example:

```bash
#!/bin/bash

for f in *.{sls,top};do
	sudo ln -sf $PWD/${f} /srv/salt/${f}
done

sudo mkdir /srv/salt/files
for f in files/*;do
	sudo ln -sf $PWD/${f} /srv/salt/${f}
done

sudo qubesctl top.enable ${1}
# sudo qubesctl --targets ${1} state.highstate -l debug
sudo qubesctl --targets ${1} state.highstate
sudo qubesctl top.disable ${1}


for f in *.{sls,top};do
	sudo unlink /srv/salt/${f}
done
for f in files/*;do
	sudo unlink /srv/salt/${f}
done
sudo rm -rf /srv/salt/files
```

---

# init-all.sh

```bash
sudo qubesctl --show-output state.sls update.qubes-dom0
sudo qubesctl --show-output --templates state.sls update.qubes-vm

for vm in dom0 my-vms-list;do
	./init.sh ${vm}
done

# make sure that after template modification everything will continue to be up
# to date
sudo qubesctl --show-output --templates state.sls update.qubes-vm
```

---

# Issues on Qubes OS 4.2.0-rc2

.center[_No Top file or master_tops data matches found. Please see master log for details.]

* There is nothing in `/var/log/salt/master`
* It seems that new Qubes OS consume top files differently because there
  is no `/srv/salt/_tops/base/topd.top` symlink to
  `/srv/salt/topd/init.top`
* Despite that there are more issue running scripts using above method.

---

# TemplateVMs customizations

* To really minimize storage footprint, configuration time and bandwith
  required for package installation we should first modify
  `debian-12-minimal` with all necessary common packages between `comm`
  and `dev`.
* TemplateVMs commons can be added by include in sls:

```yaml
include:
  - template_common
```

* _template_common.sls_:

```yaml
set zsh as default shell:
  user.present:
    - name: user
    - shell: /bin/zsh
    - groups: 
      - user
      - qubes
```

???

---

# TemplateVMs customizations

* What actions we may want to perform in TemplateVMs
  - debian-12-comm
    - add gpg keys for custom communication app repos
    - install communication apps (element, wire, keybase etc.)

---

# Developer workflow

* Scripts are typically modified in dom0
  - whenver you need to improve TemplateVM you apply change and test it, if it
    works you would like to add changes to version control
  - you don't want version control nor keys in dom0, that's why changes have to
    be synced to dev VM
  - archive scripts and copy to vm designated to development
  - when in development vm, unpack archive, fetch changes just in case your
    introduced some changes, checkout on branch commit changes and rebase based
    on newest top of tree, push changes

---

# Challanges

* Avoid laziness, which lead to manual modification and not recording steps
  that lead to current state of AppVM
* For changes which are not persistence (require template modifcation) this is
  not an issue, because those changes are lost and next time you try to use
  those you will know "Aha! I forget to put that in my SaltStack scripts"
* For changes which are persistent it is an issue if we forgot what we changed.
* I don't like to blow up my template, it already has too much, I can have
  multiple template but this is expensive in terms of maintenece time
  - Starting from debian-minimal would be great in many situations
* Dealing with Qubes OS UI without keyboard: [Xfce Cheat
  Sheet](https://defkey.com/xfce-shortcuts?orientation=landscape&cellAlternateColor=%23d6ffef&showPageNumber=true&pdf=True&showPageNumber=false)
* organization of SLS and TOP files could be way better, especially considering
  fact that top file can refernce multiple individual states from multiple sls
  files
  - in that context it may mean init.sh is redundant
* Things change between Qubes OS releases
  * Description of VMs (`qvm-prefs`)
  * Template names
* Order in which we apply states does matter.
* Do things in a way that new version of Qubes OS will not break it.

???

* Why we should base on debian-12-xfce?
  - isnt it bloated by default?

---

# Other projects

* https://github.com/unman/shaker
* https://github.com/unman/qubes.3isec.org/blob/main/tasks.html



---

class: center, middle, intro

# Q&A

