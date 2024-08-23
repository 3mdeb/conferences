class: center, middle, intro

# Enabling coreboot on Talos II

### Open Source Firmware Conference 2024

## Krystian Hebel

<img src="/remark-templates/3mdeb-presentation-template/images/logo.png"
  width="150px" style="margin-left:-20px">

---

# `whoami`

.center[<img
  src="/remark-templates/3mdeb-presentation-template/images/your_name.png"
  width="150px" style="marking-top:-50px">
]

.center[Your Name]
.center[_Your Job Title_]
.right-column50[
- X years in 3mdeb
- Work experience
- interested in:
  - interest 1
  - interest 2
  - interest 3
]
.left-column50[
- <a href="https://twitter.com/YOUR_TWITTER">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/twitter.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      @YOUR_TWITTER_
   </a>
- <a href="mailto:YOUR.NAME@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    YOUR.NAME@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/YOUR_LINKEDIN">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    linkedin.com/in/YOUR_LINKEDIN
  </a>
]

---

# Who we are ?

.center[
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png)]
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/uefi-1024x1024.png)]
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/lvfs.png)]
  .image-15[![](/remark-templates/3mdeb-presentation-template/images/yocto.png)]
]
.center[.image-35[![](/remark-templates/3mdeb-presentation-template/images/openpower.svg)]]

* coreboot licensed service providers since 2016 and leadership participants
* UEFI Adopters since 2018
* Yocto Participants and Embedded Linux experts since 2019
* Official consultants for Linux Foundation fwupd/LVFS project since 2020
* IBM OpenPOWER Foundation members since 2020

---

# Agenda

* Why?
* Hardware
* Reset vector and thereabouts
* Debugging tools
* PPC64 ABI, decisions and assumptions
* Implementation
* Current state & TODOs
* Q&A

???

- why: coreboot is simpler than hostboot
- hardware: how many cores in SoC
- reset vector: SBE, SEEPROM, PNOR, initial state
- Debugging: BMC => pdbg, QEMU => monitor
- decisions & assumptions: BE
- implementation: easy and hard part
- current state: what works, what doesn't

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
]

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
- PPC64 only
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
- x68, ARM, RISC-V, PPC64
]

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
- PPC64 only
- C++, XML, Perl, C, Tcl
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
- x68, ARM, RISC-V, PPC64
- mostly C, some ACPI
]

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
- PPC64 only
- C++, XML, Perl, C, Tcl
- partially machine-generated
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
- x68, ARM, RISC-V, PPC64
- mostly C, some ACPI
- written by humans for humans
]

???

- machine generated: initfiles, will be shown later

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
- PPC64 only
- C++, XML, Perl, C, Tcl
- partially machine-generated
- 1735196 LOC (a2ddbf3)
  - +424336 lines of comments
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
- x68, ARM, RISC-V, PPC64
- mostly C, some ACPI
- written by humans for humans
- 1562749 LOC (24.05)
  - +729830 lines of comments
]

???

- LOC counted with cloc 1.82
- empty lines not counted
- coreboot includes documentation and utils, src only is 1298407/686173

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
- PPC64 only
- C++, XML, Perl, C, Tcl
- partially machine-generated
- 1735196 LOC (a2ddbf3)
  - +424336 lines of comments
- OS:
  - user mode
  - virtual memory
  - dynamically loaded libraries
  - on-demand paging
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
- x68, ARM, RISC-V, PPC64
- mostly C, some ACPI
- written by humans for humans
- 1562749 LOC (24.05)
  - +729830 lines of comments
- program:
  - supervisor mode
  - physical memory
  - static code<br>&nbsp;
  - everything fits in cache
]

---

# Why?

.left-column50[
### Hostboot

- Apache 2.0
- PPC64 only
- C++, XML, Perl, C, Tcl
- partially machine-generated
- 1735196 LOC (a2ddbf3)
  - +424336 lines of comments
- OS:
  - user mode
  - virtual memory
  - dynamically loaded libraries
  - on-demand paging
- slow 🐢
]

.right-column50[
### coreboot

- GPLv2, some BSD-3-clause
- x68, ARM, RISC-V, PPC64
- mostly C, some ACPI
- written by humans for humans
- 1562749 LOC (24.05)
  - +729830 lines of comments
- program:
  - supervisor mode
  - physical memory
  - static code<br>&nbsp;
  - everything fits in cache
- fast <img style="height:1em" src="/remark-templates/3mdeb-presentation-template/images/coreboot-1024x1024.png" />
]

---

# Why?

Example of initfile in source form:

.center[.image-100[![](/img/initfile0.png)]]

.footnote[Source: https://git.raptorcs.com/git/talos-hostboot/tree/src/import/chips/p9/initfiles/p9a.int.scan.initfile?id=a2ddbf3150e2c02ccc904b25d6650c9932a8a841]

This form isn't used, AFAICT there is no public parser available.

???

Not actually used by Talos II. File name suggests it is for Axone, while Talos
has Nimbus chips.

There are only 2 .initfile files, probably someone forgot to remove them from
the tree.

---

# Why?

Example of initfile in converted form:

.center[.image-75[![](/img/initfile1.png)]]

.footnote[Source: https://git.raptorcs.com/git/talos-hostboot/tree/src/import/chips/p9/procedures/hwp/initfiles/p9_npu_scom.C?id=a2ddbf3150e2c02ccc904b25d6650c9932a8a841]

???

There are four different ways of writing 0 and three ways of writing 1 on this
slide.

---

# Why?

Flow of every initfile is similar: read some unnamed register, check CPU
version and attributes, write magic number back, repeat for the next register.

.center[.image-100[![](/img/initfile2.png)]]

.footnote[Source: https://git.raptorcs.com/git/talos-hostboot/tree/src/import/chips/p9/procedures/hwp/initfiles/p9_npu_scom.C?id=a2ddbf3150e2c02ccc904b25d6650c9932a8a841]

???

Most of the registers are documented, but not all.

--

Can you spot the difference between statements of middle level `if`s?

???

There is no difference!

---

# Hardware

Talos II:

.center[.image-80[![](/img/talos2.png)]]

.footnote[Source: https://raptorcs.com/content/TL2MB1/intro.html]

???

SATA controller - not open, version without it is also available.

2 CPUs, lots of RAM slots (registered DDR4 with ECC), lots of PCIe

---

# Hardware

Talos II Lite:

.center[.image-80[![](/img/talos2_lite.png)]]

.footnote[Source: https://raptorcs.com/content/TL1MB1/intro.html]

???

Less slots, SATA not an option

---

# Hardware

Specifications:

- 2 POWER9-compatible CPU sockets
  - Talos II Lite: 1 socket
- EATX form factor
- 16 DDR4 ECC registered RAM slots
  - Talos II Lite: 8 slots
- 3 PCIe 4.0 x16 slots
  - Talos II Lite: 1 slots
- 2 PCIe 4.0 x8 slots
  - Talos II Lite: 1 slots
- 2 Broadcom Gigabit Ethernet ports, one shared with BMC
- 1 Microsemi SAS 3.0 controller (**optional**)
  - Talos II Lite: n/a
- 4 USB 3.0 ports, 1 USB 2.0 port
- 1 ASpeed BMC with OpenBMC
- 1 VGA video port

---

# Hardware

POWER9 chip types:

- Scale Out (Nimbus) with directly attached memory, used on Talos II
- Scale Up (Cumulus) with memory connected through memory controllers called
  Centaurs

Nimbus modules (packages):

- Sforza - 50 mm × 50 mm, 4 DDR4, 48 PCIe lanes, 1 XBus 4B, used on
  Talos&nbsp;II
- Monza - 68.5 mm × 68.5 mm, 8 DDR4, 34 PCIe lanes, 1 XBus 4B, 48 OpenCAPI lanes
- LaGrange - 68.5 mm × 68.5 mm, 8 DDR4, 42 PCIe lanes, 2 XBus 4B, 16 OpenCAPI
  lanes

.footnote[Source: https://en.wikipedia.org/wiki/POWER9#Chip_types]

???

Talos II uses least server-like option.

XBus connects two CPUs. There is only one XBus for Sforza, so max 2 CPUs on
board.

---

# Hardware

Many cores of SoC:

.center[.image-80[![](/img/power9_ppe_instances.png)]]

.footnote[Source: https://wiki.raptorcs.com/w/images/c/ce/POWER9_um_OpenPOWER_v21_10OCT2019_pub.pdf]

???

PPE - Programmable PowerPC-lite Engines

OCC - On-Chip Microcontroller, responsible for "high-level" power management

CME - Core Management Engine, responsible for low-level power management, e.g.
waking up the core after it was powered off.

4 GPEs in OCC complex - 2 of them have dedicated uses:

- SGPE - Stop GPE, used to bring back powered-down CMEs
- PGPE - Pstate GPE, used for frequency/voltage control of cores and package as
  a whole

Sforza has less I/O PPEs than shown on the diagram.

---

# Hardware

Yet another view of POWER9:

.center[.image-75[![](/img/power9_pervasive.png)]]

.footnote[Source: https://wiki.raptorcs.com/w/images/c/c7/POWER9_Registers_vol2_version1.2_pub.pdf]

???

This is POWER9 Processor from a Pervasive Point of View.

Simply put, Pervasive is kind of bus used to communicate with chiplets through
a mechanism called SCOM - Serial Communications. It exposes registers used for
configuring hardware. It was used in initfiles shown on previous slides.

Each chiplet has its own prefix in SCOM address space.

---

# Reset vector and thereabouts

.center[.image-80[![](/img/p9_ipl.png)]]

.footnote[Source: https://wiki.raptorcs.com/w/images/b/bd/IPL-Flow-POWER9.pdf]

???

Sorry about quality, it was already like this in the linked source.

Hostboot (and by extension coreboot) only does the steps in blue.

Each step has substeps, called 'istep' - IPL step, IPL =  Initial Program Load.
Those are described in the PDF, but no time to describe them all in detail. As
we're talking about reset vector, let's focus on the left column.

---

# Reset vector and thereabouts

.left-column30[.center.image-55[![](/img/p9_ipl_self_init.png)]]

.right-column70[
- Step 0: on OpenPOWER done by BMC.
- Pervasive: bus between internal SoC chiplets, also accessible to BMC.
- SBE (Self Boot Engine): PPE 42 embedded core used to do some basic
  initialization to each chip and to load and start the Hostboot firmware.
- SEEPROM: Secure EEPROM, 256 KiB, part of SoC.
- EQ: cache chiplet, `Q` stands for quad as it is common to 4 core chiplets.
  It contains one L3 and two sets of L2 cache. Sometimes L2 and surrounding
  logic is described as EX, but from Pervasive point of view it is part of EQ.
- EC: core chiplet, each core has 4 threads.
- SBE initializes one EQ and one EC, copies HBBL from SEEPROM to L3 cache, sets
  up registers and lets one thread on that EC to start executing.
]

???

Step 0 isn't 'IBM confidential' on OpenPOWER, it is done by BMC and partially
FPGA for low level power management.

Pervasive is the name of bus between SBE and other cores, including external
(from SoC point of view) interface to BMC.

SBE (Self-Boot Engine) is one of many embedded cores in P9 SoC, it is not one of
the cores available to OS. It is also of POWER architecture, but an older
version of it (ISA 2.07 instead of 3.0 used by main cores). It starts execution
from ROM mask - while the code for it is publicly available, it is fused into
the processor and can't be freely modified.

SEEPROM is Secure EEPROM (electrically erasable programmable read-only memory)
embedded in the SoC, it is not the main flash. It holds most of the SBE code,
as well as HBBL (Hostboot bootloader). ROM mask has enough code to load further
stages into SBE SRAM and start its execution.

SBE initializes just enough of SoC to let it start executing on its own. This
includes one EQ (quad, mostly L3 and L2 cache) and one EC (core). HBBL is loaded
from SEEPROM to L3, register values are set and execution on one of main cores
finally starts.

---

# Reset vector and thereabouts

.left-column45[

PNOR layout (as of v2.00):

.small-code[
```
       part 0x00000000..0x00002000 (actual=0x00002000) [----R-----]
       HBEL 0x00008000..0x0002c000 (actual=0x00024000) [E-----F-C-]
      GUARD 0x0002c000..0x00031000 (actual=0x00005000) [E--P--F-C-]
      NVRAM 0x00031000..0x000c1000 (actual=0x00090000) [---P--F---]
    SECBOOT 0x000c1000..0x000e5000 (actual=0x00024000) [E--P------]
      DJVPD 0x000e5000..0x0012d000 (actual=0x00048000) [E--P--F-C-]
       MVPD 0x0012d000..0x001bd000 (actual=0x00090000) [E--P--F-C-]
       CVPD 0x001bd000..0x00205000 (actual=0x00048000) [E--P--F-C-]
        HBB 0x00205000..0x00305000 (actual=0x00100000) [EL--R-----]
        HBD 0x00305000..0x00425000 (actual=0x00120000) [EL--------]
        HBI 0x00425000..0x019c5000 (actual=0x015a0000) [EL--R-----]
        SBE 0x019c5000..0x01a81000 (actual=0x000bc000) [ELI-R-----]
      HCODE 0x01a81000..0x01ba1000 (actual=0x00120000) [EL--R-----]
       HBRT 0x01ba1000..0x021a1000 (actual=0x00600000) [EL--R-----]
    PAYLOAD 0x021a1000..0x022a1000 (actual=0x00100000) [-L--R-----]
 BOOTKERNEL 0x022a1000..0x03821000 (actual=0x01580000) [-L--R-----]
        OCC 0x03821000..0x03941000 (actual=0x00120000) [EL--R-----]
    FIRDATA 0x03941000..0x03944000 (actual=0x00003000) [E-----F-C-]
    VERSION 0x03944000..0x03946000 (actual=0x00002000) [-L--R-----]
    BMC_INV 0x03968000..0x03971000 (actual=0x00009000) [------F---]
       HBBL 0x03971000..0x03978000 (actual=0x00007000) [EL--R-----]
   ATTR_TMP 0x03978000..0x03980000 (actual=0x00008000) [------F---]
  ATTR_PERM 0x03980000..0x03988000 (actual=0x00008000) [E-----F-C-]
IMA_CATALOG 0x03989000..0x039c9000 (actual=0x00040000) [EL--R-----]
    RINGOVD 0x039c9000..0x039e9000 (actual=0x00020000) [----------]
    WOFDATA 0x039e9000..0x03ce9000 (actual=0x00300000) [EL--R-----]
HB_VOLATILE 0x03ce9000..0x03cee000 (actual=0x00005000) [E-----F-CV]
       MEMD 0x03cee000..0x03cfc000 (actual=0x0000e000) [EL--R-----]
       SBKT 0x03d02000..0x03d06000 (actual=0x00004000) [EL--R-----]
       HDAT 0x03d06000..0x03d0e000 (actual=0x00008000) [EL--R-----]
     UVISOR 0x03d10000..0x03e10000 (actual=0x00100000) [-L--R-----]
 BOOTKERNFW 0x03e10000..0x03ff0000 (actual=0x001e0000) [---P------]
BACKUP_PART 0x03ff7000..0x03fff000 (actual=0x00000000) [----RB----]
```
]]

.right-column55[
- PNOR is Processor NOR, to distinguish from other flash media (e.g. BMC).
- Partitions starting with `HB` are part of Hostboot, they take roughly half of
  64&nbsp;MiB flash.
- It has HBBL partition, but this is only an image that Hostboot uses to update
  SEEPROM.
- `PAYLOAD` is Skiboot, which implements OPAL (OpenPower Abstraction Layer):
  boot and runtime firmware services.
- `BOOTKERNEL` and `BOOTKERNFW` is Petitboot with optional GPU firmware, it
  starts target OS.
- Partitions with `E` flag use ECC for integrity checks.
]

???

For easier transition we decided to reuse this layout, and put coreboot in
partitions used previously by Hostboot.

Normally SBE starts HBBL from SEEPROM, which loads HBB and jumps to it. HBB
loads other code as needed.

Writing to SEEPROM is scary - we don't have any idea how many write cycles it
can take, and POWER9 CPUs aren't cheap. Because of that we decided to use HBB
for coreboot's bootblock and HBI for the rest. Writing bootblock to SEEPROM was
tested and it worked, but then bootblock became too big, now it only fits after
enabling LTO.

---

# Reset vector and thereabouts

Initial state depends on how the code was started:

.pure-table.pure-table-striped[
|          | HBBL       | HBB        | QEMU<br>(hb-mode) | description |
|----------|-----------:|-----------:|------------------:|-------------|
| NIA      | 0x00003000 | 0x00000000 | 0x00000010        | Next Instruction Address |
| HRMOR    | 0xF8200000 | 0xF8000000 | 0x08000000        | Hypervisor Real Mode Offset Register, every address is logically OR-ed with this value |
| L3 start | 0xF8200000 | 0xF8000000 | n/a               | Starting address of initialized L3 cache, it is physically-tagged so HRMOR is applied |
| L3 size  | 0x00008000 | 0x00400000 | n/a               | Size of initialized L3 cache, trying to access memory outside of initialized part of L3 results in error |
]

In case of HBBL, it is actually loaded at 0xF8203000, and first 12 KiB are
filled with placeholder for interrupt vectors. This leaves only 20 KiB for code,
and it must include SECUREROM (set of functions for calculating and verifying
SHA-512 hashes, part of Hostboot code, ~9 KiB after compilation) if Secure Boot
is to be used.

???

QEMU has `hb-mode` that is supposed to emulate how Hostboot is started, but
instruction pointer looks like a bug. HRMOR has value from IPL document, perhaps
this is how it was set for POWER8.

Next slide shows how those values were obtained.

---

# Debugging tools

- QEMU monitor
  - but QEMU is nowhere close to real hardware
--

- BMC `pdbg`: https://github.com/open-power/pdbg
<!-- Options must not be indented, it breaks rendering ¯\_(ツ)_/¯ -->
.small-code[
    ```
Options:
            -p, --processor=processor-id
            -c, --chip=chiplet-id
            -t, --thread=thread
            -a, --all
                    Run command on all possible processors/chips/threads (default)
    Commands:
            getscom <address>
            putscom <address> <value> [<mask>]
            getmem <address> <count>
            putmem <address>
            getvmem <virtual address>
            getgpr <gpr>
            putgpr <gpr> <value>
            getnia
            putnia <value>
            getspr <spr>
            putspr <spr> <value>
            start
            stop
            threadstatus
    ```
]

  - supposedly works with GDB, haven't tried

???

This isn't a full list, just the most interesting commands.

GPR - general purpose register

SPR - special purpose register

---

# PPC64 ABI, decisions and assumptions

Boring ISA and ABI stuff:

- 64b CPU, supports both big and little endian
- RISC, 32b instructions (usually)
- 32 GPRs, some of them have defined use:
  - R1: stack pointer
  - R2: TOC base - combines GOT and SDA
  - R3-R10: passing parameters to functions
  - R3: return value register
  - R13: reserved for system thread ID
- other registers:
  - CR0-CR7: conditions registers (4b each, similar to FLAGS on x86)
  - LR: link register, holds return address
  - CTR: counter
  - XER: fixed-point exception register
  - FPSCR: floating-point status and control register

???

Important parts of this slide:
- endianness
- R1 - stack is purely software concept
- R2

GOT - global offset table

SDA - small data area

---

# PPC64 ABI, decisions and assumptions

Function descriptors:

- TOC base must be loaded before calling external functions.
- Most instructions allow 16b offsets, so TOC base is typically the first
  address in the TOC plus 0x8000, this allowing access to up to 64 KiB in single
  instruction.
- Function descriptor holds 3 doubleword pointers: entry point, TOC base (R2
  value) and environment (not used in C).
- Function pointers are actually pointers to function descriptor, not its entry
  point as on x86.
- All descriptors are collected in `.opd` (official procedure descriptors)
  section.
- This renders `build/cbfs/fallback/*.map` less useful for PPC64.
- More info about descriptors: https://refspecs.linuxfoundation.org/ELF/ppc64/PPC-elf64abi.html#FUNC-DES

---

# PPC64 ABI, decisions and assumptions

Endianness:

- POWER9 can use both big and little endian, and switching between them doesn't
require a reset.
- GCC build as part of `crossgcc` is able to use both, and it works for very
  simple C code as well as assembly.
- Anything complicated links with `libgcc.a`, a library of internal subroutines
  overcoming shortcomings of particular machines. It has e.g. epilogues for
  restoring many registers at once so they aren't repeated in each function.
- Separate `libgcc.a` for BE and LE, compiler defaults to BE one. At the time
  I&nbsp;didn't know that LE version existed and could be used, so BE was chosen.
- This exposed some endianness bugs and inaccuracies in:
  - CBFS: `cbfstool` runs on LE host,
  - FMAP: not immediately caught because `0x00020200` is a palindrome,
  - CBMEM: written in BE, read from LE OS,
  - Mostly fixed by adding `htole`/`letoh` and clearly defining fields as LE.

---

# PPC64 ABI, decisions and assumptions

Decisions and assumptions:

- SBE configures serial, coreboot doesn't have to.
- Make transition between Hostboot and coreboot easy for users by reusing PNOR
  partitions.
  - This results in having to use ECC. Other partitions read by coreboot use
    ECC so code for reading from them would exist anyway.
- Focus on use as a workstation, not as a server.
  - Some RAS functionality was skipped.
  - Fail on most errors, don't boot with parts of hardware disabled.
  - Don't use Processor Runtime Diagnostics error logging, not sure if it even
    applies to BMC-based platforms.
- Use Skiboot as payload.
  - Don't use the one from PNOR, add another to CBFS for simplicity. We have
    more than enough space available.
  - Use FDT for passing information to Skiboot.

???

There is a comment in SBE code that HB team asked them to configure serial,
because HB couldn't fit the code to do so. Remember that HB is ~30 MB and SBE
fits in 256 KB SEEPROM with ECC and HBBL.

FDT - flat device tree. Hostboot used HDAT.

---

# Implementation

- All<sup>*</sup> required registers are documented in POWER9 registers
  specification
  - https://wiki.raptorcs.com/wiki/Category:Documentation
- Many hours (~2/3 of total time) spent on analysis.
  - Results at https://github.com/3mdeb/openpower-coreboot-docs/.
- Initfiles and other code written into more readable pseudocode, with register
  names and fields decoded whenever possible.
- Some assumptions were made to simplify the code.

.small-code[
```
        *0x0501082b =       // P9N2_MCS_PORT02_MCPERF3
            [31] = 1                                    // ENABLE_CL0
            [41] = 1                                    // ENABLE_AMO_MSI_RMW_ONLY
            [43] = !ATTR_ENABLE_MEM_EARLY_DATA_SCOM     // ENABLE_CP_M_MDI0_LOCAL_ONLY, !0 = 1?
            [44] = 1                                    // DISABLE_WRTO_IG
            [45] = 1                                    // AMO_LIMIT_SEL

        MC01.PORT0.SRQ.MBA_DSM0Q =       // 0x701090a
            // These are set per port so all latencies should be calculated from both DIMMs (if present)
            [0-5]   MBA_DSM0Q_CFG_RODT_START_DLY =  ATTR_EFF_DRAM_CL - ATTR_EFF_DRAM_CWL
            [6-11]  MBA_DSM0Q_CFG_RODT_END_DLY =    ATTR_EFF_DRAM_CL - ATTR_EFF_DRAM_CWL + 5
            [12-17] MBA_DSM0Q_CFG_WODT_START_DLY =  0
            [18-23] MBA_DSM0Q_CFG_WODT_END_DLY =    5
            [24-29] MBA_DSM0Q_CFG_WRDONE_DLY =      24
            [30-35] MBA_DSM0Q_CFG_WRDATA_DLY =      ATTR_EFF_DRAM_CWL + ATTR_MSS_EFF_DPHY_WLO - 8
            // Assume RDIMM, non-NVDIMM only
            [36-41] MBA_DSM0Q_CFG_RDTAG_DLY =
                MSS_FREQ_EQ_1866:                   ATTR_EFF_DRAM_CL[l_def_PORT_INDEX] + 7
                MSS_FREQ_EQ_2133:                   ATTR_EFF_DRAM_CL[l_def_PORT_INDEX] + 7
                MSS_FREQ_EQ_2400:                   ATTR_EFF_DRAM_CL[l_def_PORT_INDEX] + 8
                MSS_FREQ_EQ_2666:                   ATTR_EFF_DRAM_CL[l_def_PORT_INDEX] + 9
```
]

???

1st register wasn't documented, its name was taken from Hostboot definitions,
but those definitions weren't used by initfiles. Some of them we found later,
documentation usually has only one instance of e.g. port, which may not be the
first one.

Numbers in square brackets are bit numbers. Because these registers are BE,
MSB is bit 0, contrary to x86.

About `ATTR_`, Hostboot keeps **everything** in attributes, kind of database.
As this is part of RAM initialization, those particular values came from SPD.

---

# Implementation

Largest implemented features:

- internal buses and chiplets init
  - power on, initialize clocks, deassert reset, the usual
- RAM init
  - ECC requires all of RAM to be initialized (written) so ECC bytes match the
    data
  - Hostboot writes in order multiple patterns on each boot, we decided that it
    isn't necessary for workstation use
- PCIe init
  - just power on, train lanes and set up links, no resource allocation
- SMP init
  - OCC, CME
  - HOMER

???

RAM init: don't buy JEDEC spec if you don't need it, most of the spec is
available for free on DRAM vendors sites.

PCIe init: resource allocation done by Skiboot

OCC - On-Chip Microcontroller, responsible for "high-level" power management

CME - Core Management Engine

HOMER - Hardware Offload Microcode Engine Region

---

# Implementation

.center[.image-100[![](/img/power9_homer.png)]]

.footnote[Source: https://github.com/open-power/docs/blob/P9/occ/p9_pmcd_homer.pdf]

???

This document was added as a result of us asking on OP mailing list.

HOMER is 4 MB (per chip/CPU) block of data and code in main RAM. Without getting
into too much details, it is divided into 4 x 1MB sections, each responsible for
different part of PM.

1st: main OCC core code and data, OCC overviews work of all of the smaller
pieces, it also communicates with outside world (host and BMC).

2nd: SGPE code and data, responsible for managing and restoring state of Quad
(L3 cache).

3rd: CME code and data, basically does to core chiplets what SPGE did to quad
chiplets. It also includes self-restore code: few instructions that are run by
main cores/threads to restore GPRs, SPRs and some SCOM registers. Values to be
restored are written as part of the instructions.

4th: PGPE code and data, includes large tables mapping frequency and voltage 
values to Pstates.

---

# Implementation

Currently, HOMER prepared by coreboot is different than what Hostboot does:

- enabling existing Hostboot's debug output to log math done when building HOMER
  increases boot time to 4 hours (6 when booting with both CPUs)
- Hostboot uses complicated floating-point operations that in the end result in
  the same floor values as integer math would do
  - except sometimes intermediate values exceed `float` precision
- Hostboot has an interesting approach to rounding:

```
        uint32_t l_vdd = ...;

        // Round up
        l_vdd = (l_vdd << 1) + 1;
        l_vdd = l_vdd >> 1;
```

- https://github.com/3mdeb/openpower-coreboot-docs/blob/main/devnotes/hostbug.md
  contains this and more examples of original programming ideas

.footnote[https://github.com/open-power/hostboot/blob/4689d6d20fccc4587aea2cdfa843dc9881ff6482/src/import/chips/p9/procedures/hwp/pm/p9_pstate_parameter_block.C#L1803]

???

**TBD**
- RNG timeout - coreboot too fast
- non-technical issues:
  - lost XIVE documentation
  - https://lists.ozlabs.org/pipermail/openpower-firmware/2021-January/000611.html,
    https://lists.ozlabs.org/pipermail/openpower-firmware/2021-February/000628.html
  - platform moved to lab - full-speed CPU fan unnoticed because of that (Heads)

---

# Current state & TODOs

**TBD**

---

<br>
<br>
<br>

## .center[Q&A]

???

bonus slides:
- https://gitlab.raptorengineering.com/openpower-firmware/machine-talos-ii/machine-xml/-/blob/raptor-aggressive/raptor-util/woferclock.php
- `eieio`, `darn`, `miso`
- Linux CBMEM driver
- SEEPROM
  - SEEPROM I2C from BMC?
  - ECC
- https://github.com/3mdeb/openpower-coreboot-docs/blob/main/devnotes/hostbug.md
- Heads in PNOR (?)
