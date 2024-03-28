class: center, middle, intro

# Creating a Tool to Check Platform Security Features for Qubes OS

## Piotr Król

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# Goal

<!-- markdownlint-disable-next-line MD013 -->

### Create tool containing set of tests, which will assess how well different hardware support platform security features like D-RTM, S-RTM, Intel Boot Guard, AMD Platform Secure Boot, and UEFI Secure Boot, and how they align with Qubes OS security standards

---

# Requirement

<!-- markdownlint-disable-next-line MD013 -->

### Parts of the tools or results reported by it could be presented directly within the Qubes OS User Interface, so users can easily understand the security readiness of their system

---

# Problems

- What technology we can asses and how
  + D-RTM
  + S-RTM
  + Intel Boot Guar
  + AMD Platform Secure Boot
  + UEFI Secure Boot
- How to present results to maximize usability
  + Qubes HCL
  + Dasharo HCL

---

# UEFI Secure Boot

**Description:**

This product offers open-source test code designed to validate the proper
functioning of UEFI Secure Boot on the platform. These tests can be executed
within the Robot Framework environment and cover various scenarios, including:

- Testing the default state of Secure Boot.
- Testing the provisioning of Secure Boot certificates.
- Testing the visibility of Secure Boot state from operating system.
- Testing the execution of correctly signed file.
- Testing the execution of correctly signed file without certificate.
- Testing the execution of wrong-signed file.
- Testing the reset of Secure Boot keys and databases to factory defaults.
- Testing the operating system booting after restoring Secure Boot keys to
  default.

---

# UEFI Secure Boot

- Testing the enrollment of Secure Boot certificates in the incorrect format.
- Testing the execution of correctly signed firmware when the built-in RTC
  (Real-Time Clock) is malfunctioning, affecting certificate date verification.
- Testing the range of supported cryptographic algorithms in the firmware.
- Testing the execution of file signed for intermediate certificate.

Furthermore, alongside the test code, the product also furnishes the results
obtained from running these tests.

---

# UEFI Secure Boot

**Deliverables:**

- Documentation to run tests in the Robot Framework environment.
- Test scenarios to verify the correct implementation of UEFI Secure Boot with
  code to execute them in Robot Framework environment.

---

class: center, middle, intro

# Q&A
