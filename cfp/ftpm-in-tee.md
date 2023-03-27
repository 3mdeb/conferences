Title: "Securing Embedded Systems with fTPM implemented as Trusted Application
in TEE"

Description: In this presentation, we will discuss how to enhance the security
of embedded systems using a Trusted Execution Environment (TEE) to implement a
Firmware Trusted Platform Module (fTPM) as a Trusted Application (AP). We will
cover the benefits of using TEE and fTPM, and additionally, we will provide an
example of how to implement that and demonstrate the code. It is important to
note that there is already a kernel driver available that supports fTPM in TEE,
which can be found in the latest Linux kernel source code [1]. Part of this talk
will cover examples available on Microsoft GitHub [2] page which provide a guide
on how to implement fTPM on ARM32 platforms. Attendees will leave with a better
understanding of how to leverage TEE and fTPM, as well as the knowledge and
tools needed to implement fTPM on their embedded systems and enhance their
security.

[1] https://elixir.bootlin.com/linux/latest/source/drivers/char/tpm/tpm_ftpm_tee.h
[2] https://github.com/microsoft/ms-tpm-20-ref/tree/main/Samples/ARM32-FirmwareTPM

Agenda:

1.  Introduction
2.  Trusted Execution Environment (TEE)
3.  Firmware Trusted Platform Module (fTPM)
4.  Implementing fTPM using TEE
5.  Example of implementation, PoC demo
6.  Conclusion
