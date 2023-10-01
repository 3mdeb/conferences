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

# SatlStack init.sh

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

* I'm trying to use SaltStack for Qubes OS and Debian based systems since 2018

---

# Hardware Configuration

.center.image-90[![](/img/dasharo-fidelisguard-z690.jpg)]

* Dasharo FidelisGuard Z690 with 128GB of memory and 2TB NVMe.
* More sophisticated VM configurations we want more memory we need.

???

TODO: read proposal of Qubes OS for VM setup:
https://www.qubes-os.org/news/2022/10/28/how-to-organize-your-qubes/

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

class: center, middle, intro

Q&A

