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
  and automation for managing and scaling server infrastructure.
* Utilizes a central management server (Salt Master) to communicate with and
  control target systems (Salt Minions), with an option for masterless
  operation.
* Employs a declarative language in YAML to define desired system
  configurations, ensuring consistency and compliance across the
  infrastructure.
* **SaltStack** was aquired by VMware in 2020
* SaltStack integration was introducted to Qubes R3.1 (Q1'2016)

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

* I will not talk about, pillars, formulas and grains, because I have no idea
  about those and how to apply those in practice. 
* state

```yaml
stateid:
  cmd.run:
    - name: echo 'hello world'
```

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

* Apply predefined SaltStack states
* Change Qubes OS defaults
* Install packages
* Setup policy
* Enable/disable(?) services
* Configure Xfce
* Create VMs
* Update templates

---

# Standard operation procedure

* Since nothing is configured on your cleanly installed Qubes OS you have to
  deploy SaltStack scripts somehow.
* CaaC typically won't be public, so there is no way to download it and even
  downloading means some curl/wget or other software.
* Cloning from private repo would require some previous configuration.
* Easiest way seem to be to deliver on USB stck and then copy content to dom0.
* Before running anything let's start with making sure that dom0's and domU's
  is up to date:
  ```shell
  sudo qubesctl --show-output state.sls update.qubes-dom0
  sudo qubesctl --show-output --skip-dom0 --templates state.sls update.qubes-vm
  ```

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

---

# Other projects

* https://github.com/unman/shaker
* https://github.com/unman/qubes.3isec.org/blob/main/tasks.html



---

class: center, middle, intro

# Q&A

