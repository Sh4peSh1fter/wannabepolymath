---
title: "Key Terms & Concepts — Computer Science"
description: Core terms and concepts in computer science.
tags:
  - topic:computer-science
  - type:reference
  - status:budding
  - concept:cryptography
entry_type: DefinedTermSet
aliases:
  - cs
---

# Key Terms & Concepts — Computer Science

A curated, scannable reference of important terms in computer science. Hover a term to
reveal its definition. Terms are grouped by real sub-fields.

## Operating Systems & Low Level

<div class="annotate" markdown>

- `File Allocation Table (FAT)` (1)
- `DWARF` (2)
- `Executable and Linkable Format (ELF)` (3)
- `Operating Systems (OS)` (4)
- `Scheduling` (5)
- `IRIX` (6)
- `sbrk` (7)
- `Windows Driver Model (WDM)` (8)
- `Windows Driver Kit (WDK)` (9)
- `Paging` (10)
- `Debian` (11)
- `Linux Namespaces` (12)
- `Linux Capabilities` (13)
- `Root Directory` (14)
- `seccomp` (15)
- `Linux Security Modules (LSM)` (16)
- `ld_preload` (17)
- `ptrace` (18)
- `Hooking` (19)
- `USDT (User-Level Statically Defined Tracing)` (20)
- `Tracepoints` (21)
- `kprobes` (22)
- `uprobes` (23)
- `eBPF (extended Berkeley Packet Filter)` (24)
- `ext4` (25)
- `Hypervisor` (26)
- `Loadable Kernel Module (LKM)` (27)
- `MS-DOS` (28)
- `Kubuntu` (29)
- `Arch Linux` (30)
- `Kali Linux` (31)
- `Ubuntu` (32)
- `VT-x` (33)
- `Windows Message Queue` (34)
- `hooking trampoline` (35)
- `Control group (Cgroup)` (36)
- `union mount` (37)
- `overlay2` (38)
- `gnu grub` (39)
- `LILO (boot loader)` (40)
- `Master Boot Record (MBR)` (41)
- `boot record` (42)
- `GUID Partition Table (GPT)` (43)
- `boot loader` (44)
- `RHEL` (45)
- `Kernel panic` (46)
- `emergency mode linux` (47)
- `linux targets \ linux run levels` (48)
- `Memory Dump Files` (49)
- `Rsyslog` (50)
- `Syslog` (51)
- `Klogd` (52)
- `Syslogd` (53)
- `rotating logs` (54)
- `interrupt handler \ system call handler` (55)
- `Interrupt Descriptor Table (IDT)` (56)
- `interrupt request (or IRQ)` (57)
- `kernel oops` (58)
- `system calls` (59)
- `Ctype` (60)
- `Busybox` (61)
- `freebsd` (62)
- `file based encryption` (63)
- `libfuse` (64)
- `windows drivers` (65)
- `KVM` (66)
- `ESXI` (67)
- `vSphere` (68)
- `turbonomic` (69)
- `Object Storage` (70)
- `samba software` (71)
- `network file system (NFS)` (72)
- `neo4j` (73)
- `hbase` (74)
- `Inode` (75)
- `BTRFS` (76)
- `Distributed File System (DFS)` (77)
- `Gluster` (78)
- `bit rot - Data degradation` (79)
- `disk quota` (80)
- `geo replication` (81)
- `super block` (82)
- `glusterFS` (83)
- `Ceph` (84)
- `CephFS` (85)
- `jslinux` (86)
- `virtual network computing (vnc)` (87)
- `parrot linux` (88)
- `Portable Operating System Interface (POSIX)` (89)
- `workload` (90)
- `vm paging` (91)
- `windows paginf file` (92)
- `page fault` (93)
- `victim page` (94)
- `virtual address space` (95)
- `swappiness` (96)
- `translation looaside buffer (TLB)` (97)
- `huge pages` (98)
- `copy on write (COW)` (99)
- `dirty COW` (100)
- `Unix v7` (101)
- `FreeBSD jails` (102)
- `Linux vserver` (103)
- `Lxc` (104)
- `Docker` (105)
- `active file system` (106)
- `snapshot (storage)` (107)
- `hot spare` (108)
- `cold spare` (109)
- `file descriptor ( windows – handle)` (110)
- `context` (111)
- `hardware context` (112)
- `inter process communication (IPC)` (113)
- `zeta file system (ZFS)` (114)
- `Reliable Autonomic Distributed Object Store (RADOS)` (115)
- `FAT32 system` (116)
- `exFAT file system` (117)
- `hierarchical system` (118)
- `xtreemFS` (119)
- `stratis storage` (120)
- `SheepdogFS` (121)
- `lizardFS` (122)
- `system v` (123)

</div>

1.  A file system developed for hard drives that originally used 12 or 16 bits for each cluster entry into the file allocation table.
2.  A standardized debugging data format.
3.  A common standard file format for executables, object code, shared libraries, and core dumps.
4.  System software that manages computer hardware, software resources, and provides common services for computer programs.
5.  The action of assigning resources to perform tasks. In computing, it usually refers to the way processes are assigned to the CPU.
6.  A discontinued operating system developed by Silicon Graphics (SGI) to run on SGI workstations and servers.
7.  A system call in Unix-like operating systems to change the space allocated for the data segment of a process.
8.  A framework for device drivers that was introduced with Windows 98 and Windows 2000 to replace the older VxD driver model.
9.  A software toolset from Microsoft that enables the development of device drivers for the Microsoft Windows platform.
10.  A memory management scheme by which a computer stores and retrieves data from secondary storage for use in main memory.
11.  A popular and influential Linux distribution.
12.  A feature of the Linux kernel that partitions kernel resources such that one set of processes sees one set of resources while another set of processes sees a different set.
13.  A feature of the Linux kernel that divides the privileges traditionally associated with superuser into distinct units, which can be independently enabled and disabled.
14.  The first or top-most directory in a hierarchy.
15.  A computer security facility in the Linux kernel that allows a process to make a one-way transition into a "secure" state where it cannot make any system calls except `exit()`, `sigreturn()`, `read()` and `write()` to already-open file descriptors.
16.  A framework that allows the Linux kernel to support a variety of computer security models without favoring any single one.
17.  An environment variable in Unix-like systems that lists shared libraries to be loaded before any others.
18.  A system call found in Unix and Unix-like operating systems that allows one process to control another, enabling the controller to read and write the other's memory and registers.
19.  A range of techniques used in programming to alter or augment the behavior of an operating system, of applications, or of other software components by intercepting function calls or messages or events passed between software components.
20.  A tracing framework that allows developers to insert tracepoints into their applications.
21.  A type of instrumentation in the Linux kernel that can be used to trace kernel events.
22.  A debugging mechanism for the Linux kernel which can be used to probe any kernel function.
23.  A debugging mechanism that allows probing of user-space applications.
24.  A technology that can run sandboxed programs in an operating system kernel. It is used to safely and efficiently extend the kernel's capabilities without requiring to change kernel source code or load kernel modules.
25.  A journaling file system for Linux, developed as the successor to ext3.
26.  Computer software, firmware or hardware that creates and runs virtual machines.
27.  An object file that contains code to extend the running kernel, or so-called base kernel, of an operating system.
28.  An operating system for x86-based personal computers mostly developed by Microsoft.
29.  An official flavour of the Ubuntu operating system that uses the KDE Plasma Desktop instead of the GNOME desktop environment.
30.  A Linux distribution for computers with x86-64 processors.
31.  A Debian-derived Linux distribution designed for digital forensics and penetration testing.
32.  A popular Linux distribution based on Debian.
33.  Intel's technology for virtualization on the x86 platform.
34.  A message queuing implementation developed by Microsoft and deployed in in its Windows Server operating systems.
35.  A small piece of code that jumps to a hook function, used in software hooking.
36.  A Linux kernel feature that limits, accounts for, and isolates the resource usage of a collection of processes.
37.  A mount that allows several filesystems to be mounted at one time in a single directory.
38.  A union mount filesystem for Linux.
39.  A boot loader from the GNU Project.
40.  A boot loader for Linux and other Unix-like operating systems.
41.  A special type of boot sector at the very beginning of partitioned computer mass storage devices.
42.  A type of boot sector stored on a hard disk, floppy disk, or similar data storage device that contains machine code to be loaded into random-access memory by a computer system's built-in firmware.
43.  A standard for the layout of partition tables of a physical computer storage device.
44.  A computer program that is responsible for booting a computer.
45.  Red Hat Enterprise Linux; a Linux distribution developed by Red Hat for the commercial market.
46.  A fatal error from which the operating system cannot safely recover.
47.  A mode of operation in Linux where a minimal environment is loaded to allow the user to perform certain administrative tasks.
48.  The different modes of operation of a Linux system.
49.  A file containing the contents of a computer's memory at a specific point in time.
50.  An open-source software utility used on Unix-like computer systems for forwarding log messages in an IP network.
51.  A standard for message logging.
52.  A Linux kernel daemon for logging kernel messages.
53.  A Unix daemon that logs information from various parts of a system.
54.  A process of archiving old log files and creating new ones.
55.  A software routine that hardware invokes in response to an interrupt.
56.  A data structure used by the x86 architecture to implement an interrupt vector table.
57.  A signal sent to a processor to request its attention.
58.  A non-fatal error in the Linux kernel.
59.  The programmatic way in which a computer program requests a service from the kernel of the operating system on which it is executed.
60.  A header file in the C standard library.
61.  A software suite that combines tiny versions of many common UNIX utilities into a single small executable.
62.  A free and open-source Unix-like operating system.
63.  A cryptographic method of storing data at rest in an encrypted form.
64.  A software library that provides an interface for user-space programs to export a virtual filesystem to the Linux kernel.
65.  A computer program or a set of programs that operates or controls a particular type of device that is attached to a computer.
66.  A full virtualization solution for Linux on x86 hardware containing virtualization extensions.
67.  A bare-metal hypervisor.
68.  A bare-metal hypervisor that is installed on a server and allows you to run multiple virtual machines.
69.  An application resource management software.
70.  A computer data storage that manages data as objects, as opposed to other storage architectures like file systems which manage data as a file hierarchy, and block storage which manages data as blocks within sectors and tracks.
71.  A re-implementation of the SMB networking protocol.
72.  A distributed file system protocol allowing a user on a client computer to access files over a computer network much like local storage is accessed.
73.  A graph database management system.
74.  An open-source non-relational distributed database modeled after Google's Bigtable and written in Java.
75.  A data structure on a Unix-style file system that describes a filesystem object such as a file or a directory.
76.  A copy-on-write filesystem for Linux.
77.  A file system that is distributed over several file servers or locations.
78.  A scalable network filesystem.
79.  A gradual decay of storage media.
80.  A limit that is set by a system administrator that restricts certain aspects of file system usage on modern operating systems.
81.  The replication of data to geographically remote sites.
82.  A record of the characteristics of a file system, including its size, block size, and the location of the inode table.
83.  A scalable network-attached storage file system.
84.  A distributed storage and network file system.
85.  A POSIX-compliant network file system built on top of Ceph.
86.  A PC emulator in JavaScript.
87.  A graphical desktop-sharing system that uses the Remote Frame Buffer protocol to remotely control another computer.
88.  A Linux distribution based on Debian with a focus on security, privacy, and development.
89.  A family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
90.  The amount of processing that a computer does at a given time.
91.  A memory management scheme by which a computer stores and retrieves data from secondary storage for use in main memory.
92.  A file on a hard disk that Windows uses as if it were RAM.
93.  A type of interrupt, raised by hardware when a running program accesses a memory page that is not currently mapped by the memory management unit into the virtual address space of a process.
94.  A page of memory that is selected to be replaced from main memory to make room for a new page.
95.  A memory space that is an abstraction of physical memory.
96.  A Linux kernel parameter that controls the relative weight given to swapping out of runtime memory, as opposed to dropping pages from the system page cache.
97.  A memory cache that is used to reduce the time taken to access a user memory location.
98.  A feature in Linux that allows the kernel to manage large pages of memory.
99.  An optimization strategy used in computer programming.
100.  A security vulnerability in the Linux kernel's implementation of the copy-on-write mechanism.
101.  The seventh edition of the Unix operating system.
102.  A software mechanism in FreeBSD for partitioning a computer system into several independent, smaller systems.
103.  A virtual private server implementation that was created by adding operating-system-level virtualization capabilities to the Linux kernel.
104.  An operating-system-level virtualization method for running multiple isolated Linux systems on a control host using a single Linux kernel.
105.  A set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
106.  A file system that is currently mounted and accessible.
107.  A set of reference markers for data at a particular point in time.
108.  A spare hard drive that is powered on and connected to the system, ready for use.
109.  A spare hard drive that is powered off and not connected to the system.
110.  An abstract indicator used to access a file or other input/output resource, such as a pipe or network socket.
111.  The set of data that is accessible to a program.
112.  The state of a computer's hardware at a specific point in time.
113.  A mechanism which allows processes to communicate with each other and synchronize their actions.
114.  A combined file system and logical volume manager designed by Sun Microsystems.
115.  The object storage system that underlies Ceph.
116.  A file system developed by Microsoft.
117.  A file system introduced by Microsoft in 2006 and optimized for flash memory such as USB flash drives and SD cards.
118.  A system in which components are organized in a tree-like structure.
119.  An open-source, distributed file system for the cloud.
120.  A local storage management for Linux.
121.  A distributed object storage system for QEMU.
122.  A distributed file system.
123.  One of the first commercial operating systems.

## Networking

<div class="annotate" markdown>

- `VPN (Virtual Private Network)` (1)
- `TCP/IP Model` (2)
- `OSI Model` (3)
- `ARP (Address Resolution Protocol)` (4)
- `SMTP (Simple Mail Transfer Protocol)` (5)
- `DHCP (Dynamic Host Configuration Protocol)` (6)
- `RIP (Routing Information Protocol)` (7)
- `SCTP (Stream Control Transmission Protocol)` (8)
- `SPF (Sender Policy Framework)` (9)
- `DKIM (DomainKeys Identified Mail)` (10)
- `SSL (Secure Sockets Layer)` (11)
- `TLS (Transport Layer Security)` (12)
- `HTTPS (Hypertext Transfer Protocol Secure)` (13)
- `FTP (File Transfer Protocol)` (14)
- `Spanning Tree Protocol (STP)` (15)
- `QUIC` (16)
- `DNSSEC (Domain Name System Security Extensions)` (17)
- `SCP (Secure Copy Protocol)` (18)
- `Port Knocking` (19)
- `Network security` (20)
- `Cloud security` (21)
- `INetSim` (22)
- `Shodan` (23)
- `censys` (24)
- `cloudflare` (25)
- `Network Driver Interface Specification` (26)
- `Transport Driver Interface` (27)
- `voice over internet protocol (voip)` (28)
- `sip protocol` (29)
- `wireless ad hoc network (WANET)` (30)
- `Mobile ad hoc network (MANET)` (31)
- `ad hoc` (32)
- `Ad-Hoc command` (33)
- `t-shark` (34)
- `software defined network` (35)
- `Data integrity` (36)
- `Ssh brute force attack` (37)
- `web server gateway interface (wsgi)` (38)
- `reverse tunneling` (39)
- `jdbc drivers` (40)
- `network model` (41)

</div>

1.  A mechanism for creating a secure connection over a public network like the internet.
2.  A conceptual model and set of communications protocols used in the Internet and similar computer networks.
3.  A conceptual framework used to understand network interactions in seven layers.
4.  A communication protocol used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address.
5.  A communication protocol for electronic mail transmission.
6.  A network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network.
7.  One of the oldest distance-vector routing protocols which employ the hop count as a routing metric.
8.  A computer network communications protocol that provides a reliable, message-oriented data transfer service.
9.  An email authentication method designed to detect forging sender addresses during the delivery of the email.
10.  An email authentication method designed to detect forged sender addresses in emails.
11.  A standard security technology for establishing an encrypted link between a server and a client.
12.  A cryptographic protocol designed to provide communications security over a computer network.
13.  An extension of the Hypertext Transfer Protocol (HTTP) for secure communication over a computer network.
14.  A standard network protocol used for the transfer of computer files between a client and server on a computer network.
15.  A network protocol that builds a logical loop-free topology for Ethernet networks.
16.  A general-purpose transport layer network protocol initially designed by Google.
17.  A suite of Internet Engineering Task Force (IETF) specifications for securing certain kinds of information provided by the Domain Name System (DNS) as used on Internet Protocol (IP) networks.
18.  A means of securely transferring computer files between a local host and a remote host or between two remote hosts.
19.  A method of externally opening ports on a firewall by generating a connection attempt on a set of pre-specified closed ports.
20.  Policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources.
21.  A set of policies, controls, procedures and technologies that work together to protect cloud-based systems, data, and infrastructure.
22.  A software suite that simulates common internet services in a lab environment.
23.  A search engine for Internet-connected devices.
24.  A search engine for finding hosts and networks on the internet.
25.  A web performance and security company.
26.  An API for network interface controllers in Microsoft Windows.
27.  A kernel-mode network driver interface for Microsoft Windows.
28.  A methodology and group of technologies for the delivery of voice communications and multimedia sessions over Internet Protocol networks.
29.  A signaling protocol used for initiating, maintaining, and terminating real-time sessions that include voice, video and messaging applications.
30.  A decentralized type of wireless network.
31.  A self-configuring network of mobile devices connected by wireless links.
32.  For a particular purpose only.
33.  A command that is executed on a remote server.
34.  A network protocol analyzer.
35.  A networking approach that uses software-based controllers or application programming interfaces to communicate with underlying hardware infrastructure and direct traffic on a network.
36.  The maintenance of, and the assurance of the accuracy and consistency of, data over its entire life-cycle.
37.  A method of guessing a password by systematically trying all possible combinations of letters, numbers, and symbols.
38.  A simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.
39.  A technique for creating a connection from a private network to a public network.
40.  A set of standard software drivers that allow Java applications to communicate with databases.
41.  A model that describes the communication between different levels of a network.

## Cyber Security

<div class="annotate" markdown>

- `SMEP (Supervisor Mode Execution Prevention)` (1)
- `Sandbox Escape` (2)
- `DEP (Data Execution Prevention)` (3)
- `Cyber Security` (4)
- `Pegasus (spyware)` (5)
- `Fuzzing` (6)
- `ROP (Return-Oriented Programming)` (7)
- `Drive-by Attack` (8)
- `HIDS (Host-based Intrusion Detection System)` (9)
- `Vulnerability Research` (10)
- `XSS (Cross-Site Scripting)` (11)
- `SQL Injection` (12)
- `Stack Smashing` (13)
- `Unvalidated Redirects and Forwards` (14)
- `CSRF (Cross-Site Request Forgery)` (15)
- `SYN Flood` (16)
- `Missing Function Level Access Control` (17)
- `Ping of Death` (18)
- `Command Injection` (19)
- `Zip Bomb` (20)
- `Watering Hole Attack` (21)
- `Fork Bomb` (22)
- `Code Injection` (23)
- `Metasploit` (24)
- `Botnet` (25)
- `Morris Worm` (26)
- `Penetration Tester` (27)
- `Binwalk` (28)
- `foremost` (29)
- `Sulley fuzzer` (30)
- `rop gadget` (31)
- `lkm hacking` (32)
- `rop exploit` (33)
- `modern heap smashing` (34)
- `Using Components with Known Vulnerabilities attack` (35)
- `correlation attack` (36)
- `Onehalf` (37)
- `Bluetooth` (38)
- `fuzzy hashing` (39)
- `Hopper` (40)
- `Qemu` (41)
- `chakra` (42)
- `Wiener's attack` (43)
- `Coppersmith's attack` (44)
- `smurf attack` (45)
- `fraggle attack` (46)
- `google dorking` (47)
- `Remote File Inclusion` (48)
- `Local File Inclusion` (49)
- `Log poisoning` (50)
- `Web application firewall` (51)
- `UEFI Bootkits` (52)
- `Side channel attack` (53)
- `RDP attack` (54)
- `Reverse RDP attack` (55)
- `Samy (computer worm)` (56)
- `web application security` (57)
- `real time protection` (58)
- `filter driver` (59)
- `SIEM` (60)
- `YARA` (61)
- `Software Restriction Policies` (62)
- `NtCreateFile` (63)
- `Quarantine` (64)
- `EICAR` (65)
- `Microsoft Binary Format` (66)
- `ole files` (67)
- `STRIDE` (68)
- `Red team` (69)
- `Blue team` (70)
- `CVE` (71)
- `backtrack` (72)
- `Cain and Abel (software)` (73)
- `Ollydbg` (74)
- `Nikto` (75)
- `Burp Suite` (76)
- `john the ripper` (77)
- `netcat` (78)
- `Ettercap` (79)
- `Mstsc` (80)
- `Veyon` (81)
- `rdp protocol` (82)
- `domain controller` (83)
- `ntds.dit` (84)
- `active directory` (85)
- `ad ds` (86)
- `azure` (87)
- `lsass` (88)
- `Kerberos` (89)
- `Key distribution center` (90)
- `Prism` (91)
- `Windows password hashing` (92)
- `Linux password hashing` (93)
- `Diginotar` (94)
- `enfal Trojan` (95)
- `zlob trojan` (96)
- `virus heat` (97)
- `MS antivirus` (98)
- `shadow IT` (99)
- `reverse tracert` (100)
- `record route` (101)
- `SELinux` (102)
- `directory access control (dac)` (103)
- `mandatory access control (mac)` (104)
- `access vector cache (avc)` (105)
- `ursnif Trojan` (106)
- `cutwail botnet` (107)
- `macro malware` (108)
- `Visual Basic for Applications (VBA)` (109)
- `sigreturn oriented programming` (110)
- `srum forensics` (111)
- `confidentiality integrity availability (CIA)` (112)
- `dll hijacking` (113)
- `win-internals` (114)
- `cyber kill chain` (115)
- `advanced persistent threat (apt)` (116)
- `data encryption standard (des)` (117)
- `Triple DES` (118)
- `advanced encryption standard (aes)` (119)
- `intrusion detection system (IDS)` (120)
- `intrusion prevention system (IPS)` (121)
- `WMI Query Language (WQL)` (122)
- `Link-Local Multicast Name Resolution (LLMNR)` (123)
- `NetBIOS` (124)
- `Server Message Block (SMB)` (125)
- `cicada 3301` (126)
- `Tor browser` (127)
- `asruex Trojan` (128)
- `css injection` (129)
- `blind sql (injection)` (130)
- `banner grabbing` (131)

</div>

1.  A security feature in some CPUs that prevents the execution of code in pages belonging to user-space applications while the CPU is in supervisor mode.
2.  Exploiting a bug in a sandbox's implementation that allows a program to bypass its restrictions.
3.  A security feature that can help prevent damage from viruses and other security threats by monitoring your programs to make sure they use system memory safely.
4.  The practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks.
5.  A spyware developed by the Israeli cyberarms firm NSO Group that can be covertly installed on mobile phones running most versions of iOS and Android.
6.  An automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program.
7.  A computer security exploit technique that allows an attacker to execute code in the presence of security defenses such as non-executable memory and code signing.
8.  A malware attack that is downloaded and installed on a computer without the user's knowledge.
9.  An intrusion detection system that is capable of monitoring and analyzing the internals of a computing system as well as the network packets on its network interfaces.
10.  The process of discovering vulnerabilities in software and computer systems.
11.  A type of security vulnerability typically found in web applications that enables attackers to inject client-side scripts into web pages viewed by other users.
12.  A code injection technique that might destroy your database.
13.  A type of buffer overflow attack where the attacker overwrites the return address on the stack.
14.  A web application security vulnerability that occurs when a web application redirects a user to a new page without properly validating the target URL.
15.  An attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated.
16.  A form of denial-of-service attack in which an attacker sends a succession of SYN requests to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic.
17.  A security vulnerability where a user is able to perform actions they should not be able to.
18.  A type of denial-of-service (DoS) attack in which an attacker attempts to crash, destabilize, or freeze a targeted computer or service by sending a malformed or oversized ICMP packet.
19.  A type of attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application.
20.  A malicious archive file designed to crash or render useless the program or system reading it.
21.  A computer attack strategy, in which the victim is a particular group (organization, industry, or region). In this attack, the attacker guesses or observes which websites the group often uses and infects one or more of them with malware.
22.  A denial-of-service attack wherein a process continually replicates itself to deplete available system resources, slowing down or crashing the system due to resource starvation.
23.  The exploitation of a computer bug that is caused by processing invalid data.
24.  A popular penetration testing framework.
25.  A number of Internet-connected devices, each of which is running one or more bots.
26.  One of the first computer worms distributed via the Internet.
27.  A person who performs a penetration test, which is an authorized simulated cyberattack on a computer system, performed to evaluate the security of the system.
28.  A tool for analyzing, reverse engineering, and extracting firmware images.
29.  A console program to recover files based on their headers, footers, and internal data structures.
30.  A fuzzer development and fuzz testing framework consisting of multiple extensible components.
31.  A sequence of instructions already present in the program's memory that ends with a `ret` instruction, used in Return-Oriented Programming (ROP) attacks.
32.  Techniques involving the malicious use or manipulation of Loadable Kernel Modules (LKMs) to compromise an operating system's kernel.
33.  A cybersecurity exploit technique that uses return-oriented programming (ROP).
34.  A technique that involves exploiting memory corruption vulnerabilities in the heap data area.
35.  An attack targeting software components, such as libraries and frameworks, with known vulnerabilities.
36.  An attack that uses statistical analysis of encrypted traffic to infer information.
37.  A polymorphic computer virus that infects `.COM` and `.EXE` files.
38.  A short-range wireless technology standard.
39.  A technique used to check whether two files are similar without storing the file contents.
40.  A reverse engineering tool for macOS and Linux.
41.  A free and open-source emulator and virtualizer.
42.  The JavaScript engine used in Microsoft Edge.
43.  A cryptographic attack on RSA that uses continued fractions.
44.  A cryptographic attack on RSA with a small public exponent.
45.  A type of denial-of-service attack that floods a network with ICMP echo requests.
46.  A denial-of-service attack that uses a large amount of UDP echo traffic.
47.  A search technique that uses advanced search operators to find specific strings of text within search results.
48.  A type of vulnerability that allows an attacker to include a remote file.
49.  A type of vulnerability that allows an attacker to include a local file.
50.  A technique that involves injecting malicious code into a server's log files.
51.  A firewall that monitors, filters, and blocks HTTP traffic to and from a web application.
52.  Malicious code that is loaded before the operating system starts.
53.  An attack based on information gained from the implementation of a computer system, rather than weaknesses in the implemented algorithm itself.
54.  An attack that targets the Remote Desktop Protocol.
55.  An attack that allows an attacker to gain access to a network from the outside by exploiting a compromised machine within the network.
56.  A cross-site scripting worm designed to propagate across the MySpace social networking site.
57.  The branch of information security that deals specifically with security of websites, web applications and web services.
58.  A security feature that continuously monitors and protects a system from threats.
59.  A program that intercepts and processes I/O requests.
60.  Security Information and Event Management; a set of tools and services that combines security information management (SIM) and security event management (SEM).
61.  A tool used to identify and classify malware samples.
62.  A feature of Microsoft Windows that identifies and controls the execution of software.
63.  A Windows API function used to create or open a file.
64.  The isolation of suspicious files in a restricted environment.
65.  A standard for antivirus test files.
66.  A family of file formats for storing structured data.
67.  A file format used by Microsoft for its Object Linking and Embedding (OLE) technology.
68.  A model for identifying and categorizing security threats.
69.  A group of security professionals who act as aggressors in a simulated cyberattack.
70.  A group of security professionals who defend against a simulated cyberattack.
71.  Common Vulnerabilities and Exposures; a list of publicly disclosed computer security flaws.
72.  A Linux distribution that focused on security.
73.  A password recovery tool for Microsoft Windows.
74.  A debugger for 32-bit executables.
75.  A web server scanner.
76.  A graphical tool for testing Web application security.
77.  A password cracking software tool.
78.  A computer networking utility for reading from and writing to network connections.
79.  A free and open source network security tool for man-in-the-middle attacks on a LAN.
80.  A command-line tool for connecting to a remote computer.
81.  A computer monitoring and classroom management software.
82.  A proprietary protocol developed by Microsoft which provides a user with a graphical interface to connect to another computer over a network connection.
83.  A server that is responsible for responding to security authentication requests within a Windows Server domain.
84.  A database that stores Active Directory data, including user objects and password hashes.
85.  A directory service developed by Microsoft for Windows domain networks.
86.  Active Directory Domain Services; a server role in Active Directory that allows admins to manage and store information about resources from a network, as well as application data, in a distributed database.
87.  A cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers.
88.  A process in Microsoft Windows operating systems that is responsible for enforcing the security policy on the system.
89.  A computer-network authentication protocol that works on the basis of tickets to allow nodes communicating over a non-secure network to prove their identity to one another in a secure manner.
90.  A component of a cryptosystem that is responsible for generating and distributing keys.
91.  A clandestine surveillance program under which the United States National Security Agency (NSA) collects internet communications from at least nine major US internet companies.
92.  The methods used by Windows to store user passwords.
93.  The methods used by Linux to store user passwords.
94.  A Dutch certificate authority that was compromised in 2011.
95.  A Trojan horse that was used in a series of attacks against Israeli websites.
96.  A Trojan horse that masquerades as a video codec.
97.  A type of malware that displays a fake warning that the computer is infected with a virus.
98.  A family of antivirus software products from Microsoft.
99.  The use of information technology systems, devices, software, applications, and services without explicit IT department approval.
100.  A network diagnostic tool that determines the path to a destination by recording the route of packets through the network.
101.  An option in the IP protocol that allows the route of a packet to be recorded.
102.  A security enhancement to Linux which allows users and administrators more control over access control.
103.  A type of security that grants or restricts access to objects based on the identity of subjects and/or groups to which they belong.
104.  A type of access control by which the operating system constrains the ability of a subject or initiator to access or generally perform some sort of operation on an object or target.
105.  A cache in the Linux kernel that stores access control decisions.
106.  A banking Trojan.
107.  A botnet that is primarily involved in sending spam e-mail.
108.  A type of malware that is written in the same macro language as the software it infects.
109.  A programming language and integrated development environment from Microsoft.
110.  A computer security exploit technique that allows an attacker to execute code in the presence of security defenses such as non-executable memory and code signing.
111.  A forensic technique for analyzing the SRUM database in Windows.
112.  A model for information security.
113.  A method of injecting a malicious DLL into a running process.
114.  A suite of tools for Windows that includes a number of utilities for system administration and troubleshooting.
115.  A framework for understanding the steps an attacker takes to compromise a system.
116.  A stealthy threat actor that gains unauthorized access to a computer network and remains undetected for an extended period.
117.  A symmetric-key algorithm for the encryption of digital data.
118.  A symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block.
119.  A symmetric block cipher chosen by the U.S. government to protect classified information.
120.  A device or software application that monitors a network or systems for malicious activity or policy violations.
121.  A network security/threat prevention technology that examines network traffic flows to detect and prevent vulnerability exploits.
122.  A query language for WMI.
123.  A protocol based on the Domain Name System (DNS) packet format that allows both IPv4 and IPv6 hosts to perform name resolution for hosts on the same local link.
124.  A networking protocol that allows applications on different computers to communicate with each other.
125.  A network protocol that provides shared access to files, printers, and serial ports between nodes on a network.
126.  A nickname given to an organization that on three occasions has posted a set of puzzles to recruit codebreakers from the public.
127.  A free and open-source web browser that enables anonymous communication.
128.  A Trojan horse that is used to steal banking information.
129.  An attack technique that involves injecting a Cascading Style Sheets (CSS) code into a web page to change its appearance.
130.  A type of SQL injection attack that asks the database true or false questions and determines the answer based on the applications response.
131.  A technique used to gain information about a remote system.

## Programming Languages

<div class="annotate" markdown>

- `Ruby` (1)
- `Java` (2)
- `JavaScript` (3)
- `HTML (HyperText Markup Language)` (4)
- `CSS (Cascading Style Sheets)` (5)
- `XML (eXtensible Markup Language)` (6)
- `PHP` (7)
- `Kotlin` (8)
- `C` (9)
- `C++` (10)
- `Python` (11)
- `Flutter` (12)
- `Assembly Language` (13)
- `R` (14)
- `XOD` (15)
- `Lua` (16)
- `TypeScript` (17)
- `Pascal (programming language)` (18)
- `Scala (programming language)` (19)
- `Dart` (20)
- `cobol` (21)
- `CPython` (22)
- `AWK` (23)
- `Pedump` (24)
- `Ipython` (25)
- `Cython` (26)
- `.net framework` (27)
- `Ruby on Rails` (28)
- `Kanban` (29)
- `Scrum` (30)
- `Scrumban` (31)
- `metadata` (32)
- `namespace` (33)
- `Uniform Resource Identifier (URI)` (34)
- `Microframework` (35)
- `Etcher` (36)
- `information technology` (37)
- `monolithic application` (38)
- `monolithic architecture` (39)
- `microservices architecture` (40)
- `two pizza rule` (41)
- `openxml` (42)
- `Macro (computer science)` (43)
- `miniservices architecture` (44)
- `macro architecture` (45)
- `Service oriented architecture (SOA)` (46)
- `Kido \ xbmc` (47)
- `software suite` (48)
- `Data model` (49)
- `data structures` (50)
- `database model` (51)
- `object model` (52)
- `structure translation system` (53)
- `associative data model` (54)
- `ibm associative data model` (55)
- `Vendor-Managed Inventory (VMI)` (56)
- `pyEMU` (57)
- `openGL` (58)
- `abstract syntax tree (AST)` (59)
- `Application security` (60)
- `fortran programming` (61)
- `Swift` (62)
- `erlang` (63)
- `ironpython` (64)
- `hoisting js` (65)
- `currying js` (66)

</div>

1.  A dynamic, open source programming language with a focus on simplicity and productivity.
2.  A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
3.  A programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.
4.  The standard markup language for documents designed to be displayed in a a web browser.
5.  A style sheet language used for describing the presentation of a document written in a markup language like HTML.
6.  A markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
7.  A general-purpose scripting language especially suited to web development.
8.  A cross-platform, statically typed, general-purpose programming language with type inference.
9.  A general-purpose, procedural computer programming language.
10.  A general-purpose programming language created as an extension of the C programming language, or "C with Classes".
11.  An interpreted, high-level and general-purpose programming language.
12.  An open-source UI software development kit created by Google.
13.  A low-level programming language for a computer, or other programmable device, in which there is a very strong correspondence between the instructions in the language and the architecture's machine code instructions.
14.  A programming language and free software environment for statistical computing and graphics.
15.  A visual programming language for microcontrollers.
16.  A lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications.
17.  A programming language developed and maintained by Microsoft. It is a strict syntactical superset of JavaScript and adds optional static typing to the language.
18.  An influential imperative and procedural programming language.
19.  A general-purpose programming language providing support for functional programming and a strong static type system.
20.  A programming language designed for client development, such as for the web and mobile apps.
21.  A compiled English-like computer programming language designed for business use.
22.  The default, most widely used implementation of the Python programming language.
23.  A domain-specific language designed for text processing and typically used as a data extraction and reporting tool.
24.  A command-line tool to dump information about Win32 executable files.
25.  A command shell for interactive computing in multiple programming languages.
26.  A programming language that is a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python.
27.  A software framework developed by Microsoft that runs primarily on Microsoft Windows.
28.  A server-side web application framework written in Ruby.
29.  A lean method to manage and improve work across human systems.
30.  A lightweight agile framework for managing and sustaining complex projects.
31.  A hybrid of Scrum and Kanban.
32.  Data that provides information about other data.
33.  A set of symbols that are used to identify and refer to objects of various kinds.
34.  A string of characters that unambiguously identifies a particular resource.
35.  A web application framework that is minimal, providing only the essential features needed to build a web application.
36.  A free and open-source utility used for writing image files such as .iso and .img files, as well as zipped folders onto storage media to create live SD cards and USB flash drives.
37.  The use of computers to store, retrieve, transmit, and manipulate data, or information.
38.  An application that is designed as a single, indivisible unit.
39.  A software architecture in which an application is designed as a single, indivisible unit.
40.  A software architecture in which an application is designed as a collection of loosely coupled services.
41.  A rule that states that a team should be small enough to be fed by two pizzas.
42.  A file format for representing electronic documents.
43.  A rule or pattern that specifies how a certain input sequence should be mapped to a replacement output sequence according to a defined procedure.
44.  A software architecture in which an application is designed as a collection of small services.
45.  A software architecture in which an application is designed as a collection of large services.
46.  A software architecture in which an application is designed as a collection of services that communicate with each other.
47.  A free and open-source media player software application.
48.  A collection of computer programs that are packaged together.
49.  An abstract model that organizes elements of data and standardizes how they relate to one another and to the properties of real-world entities.
50.  A data organization, management, and storage format that enables efficient access and modification.
51.  A model that describes the structure of a database.
52.  A model that describes the structure of a system in terms of objects, their attributes, and the relationships between them.
53.  A system that translates from one language to another.
54.  A data model in which the primary data structure is a network of nodes and links.
55.  A data model that is based on the principles of associative memory.
56.  A supply chain arrangement where a supplier of goods is responsible for generating orders and maintaining the inventory level of the consumer.
57.  A Python-based x86 emulator.
58.  A cross-language, cross-platform application programming interface for rendering 2D and 3D vector graphics.
59.  A tree representation of the abstract syntactic structure of source code written in a programming language.
60.  The process of making applications more secure by finding, fixing, and enhancing the security of apps.
61.  A general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing.
62.  A general-purpose, multi-paradigm, compiled programming language developed by Apple Inc.
63.  A general-purpose, concurrent, functional programming language, and a garbage-collected runtime system.
64.  An implementation of the Python programming language targeting the .NET Framework.
65.  A JavaScript mechanism where variables and function declarations are moved to the top of their scope before code execution.
66.  A technique of evaluating function with multiple arguments, into sequence of functions with single argument.

## Software Development & Tools

<div class="annotate" markdown>

- `ALM (Application Lifecycle Management)` (1)
- `Redis` (2)
- `PowerShell` (3)
- `Batch File` (4)
- `Bash` (5)
- `RabbitMQ` (6)
- `Vagrant` (7)
- `Reverse Engineering` (8)
- `Ionic` (9)
- `NestJS` (10)
- `Yarn` (11)
- `Lerna` (12)
- `Wine` (13)
- `Radare2` (14)
- `JDK (Java Development Kit)` (15)
- `Postman` (16)
- `ExifTool` (17)
- `Beautiful Soup` (18)
- `Selenium` (19)
- `Figma` (20)
- `Virtualenv` (21)
- `PyAutoGUI` (22)
- `Axure RP` (23)
- `Microsoft Foundation Class Library (MFC)` (24)
- `R&D` (25)
- `Pedump` (26)
- `PhantomJS` (27)
- `Web crawler (spider bot)` (28)
- `Web scraping` (29)
- `Core dump` (30)
- `WPF` (31)
- `system administrator` (32)
- `Gantt` (33)
- `DIY` (34)
- `Simple Object Access Protocol` (35)
- `Representational State Transfer` (36)
- `Gunicorn` (37)
- `Jenkins` (38)
- `Axios` (39)
- `eel python` (40)
- `Software as a service (SaaS)` (41)
- `Symbolic link` (42)
- `Sdk` (43)
- `SciPy` (44)
- `Ocr` (45)
- `imagemagick` (46)
- `textcleaner` (47)
- `pytesseract` (48)
- `Jira` (49)
- `Entity Relationship Diagram (ERD)` (50)
- `tkinter` (51)
- `Sqlplus` (52)
- `Backpropagation` (53)
- `Squid server` (54)
- `Prometheus` (55)
- `terraform` (56)
- `infrastructure as code (iac)` (57)
- `Ansible` (58)
- `Ansible tower` (59)
- `agile programming` (60)
- `devsecops` (61)
- `cd pipeline` (62)
- `Computer integrated manufacturing (CIM)` (63)
- `Agron (information system)` (64)
- `Continuous Integration (CI)` (65)
- `Travis CI` (66)
- `Jenkinsfile` (67)
- `Groovy` (68)
- `internet information services (iis) server` (69)
- `nginx` (70)
- `powercli` (71)
- `context switch` (72)
- `configuration management (cm)` (73)
- `saltstack` (74)
- `puppet software` (75)
- `chef software` (76)
- `YAML` (77)
- `Ipython` (78)
- `Cython` (79)
- `namespace` (80)
- `Uniform Resource Identifier (URI)` (81)
- `Microframework` (82)
- `Etcher` (83)
- `information technology` (84)
- `monolithic application` (85)
- `monolithic architecture` (86)
- `microservices architecture` (87)
- `two pizza rule` (88)
- `openxml` (89)
- `Macro (computer science)` (90)
- `miniservices architecture` (91)
- `macro architecture` (92)
- `Service oriented architecture (SOA)` (93)
- `Kido \ xbmc` (94)
- `software suite` (95)
- `Data model` (96)
- `data structures` (97)
- `database model` (98)
- `object model` (99)
- `structure translation system` (100)
- `associative data model` (101)
- `ibm associative data model` (102)
- `Vendor-Managed Inventory (VMI)` (103)
- `pyEMU` (104)
- `openGL` (105)
- `abstract syntax tree (AST)` (106)
- `Application security` (107)

</div>

1.  The product lifecycle management (governance, development, and maintenance) of computer programs.
2.  An in-memory data structure store, used as a database, cache and message broker.
3.  A task automation and configuration management framework from Microsoft, consisting of a command-line shell and the associated scripting language.
4.  A script file in DOS, OS/2 and Microsoft Windows.
5.  A Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.
6.  An open-source message-broker software that originally implemented the Advanced Message Queuing Protocol (AMQP).
7.  An open-source software product for building and maintaining portable virtual software development environments.
8.  The processes of extracting knowledge or design information from anything man-made and re-producing it or re-producing anything based on the extracted information.
9.  A complete open-source SDK for hybrid mobile app development.
10.  A framework for building efficient, scalable Node.js server-side applications.
11.  A package manager for your code.
12.  A tool for managing JavaScript projects with multiple packages.
13.  A compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD.
14.  A complete framework for reverse-engineering and analyzing binaries.
15.  An implementation of either one of the Java SE, Java EE or Java ME platforms released by Oracle Corporation in the form of a binary product aimed at Java developers on Solaris, Linux, macOS or Windows.
16.  An API platform for developers to design, build, test and iterate their APIs.
17.  A free and open-source software program for reading, writing, and manipulating image, audio, video, and PDF metadata.
18.  A Python package for parsing HTML and XML documents.
19.  A portable framework for testing web applications.
20.  A vector graphics editor and prototyping tool which is primarily web-based.
21.  A tool to create isolated Python environments.
22.  A Python module for programmatically controlling the mouse and keyboard.
23.  A software for creating prototypes and specifications for websites and applications.
24.  A C++ object-oriented library for developing desktop applications for Windows.
25.  Research and Development; creative work undertaken on a systematic basis to increase the stock of knowledge and use it to devise new applications.
26.  A command-line tool to dump information about Win32 executable files.
27.  A discontinued headless browser used for automating web page interaction.
28.  An Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing.
29.  The process of extracting data from websites.
30.  The recorded state of the working memory of a computer program at a specific time, generally when the program has terminated abnormally.
31.  A free and open-source graphical user interface framework for building desktop applications for Windows.
32.  A person who is responsible for the upkeep, configuration, and reliable operation of computer systems.
33.  A type of bar chart that illustrates a project schedule.
34.  Do It Yourself; the method of building, modifying, or repairing things by oneself without the direct aid of experts or professionals.
35.  A messaging protocol specification for exchanging structured information in the implementation of web services in computer networks.
36.  A software architectural style that defines a set of constraints to be used for creating Web services.
37.  A Python Web Server Gateway Interface (WSGI) HTTP server.
38.  An open source automation server.
39.  A promise-based HTTP client for the browser and node.js.
40.  A library for Python to create GUIs for desktop applications.
41.  A software licensing and delivery model in which software is licensed on a subscription basis and is centrally hosted.
42.  A file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution.
43.  Software Development Kit; a collection of software development tools in one installable package.
44.  A free and open-source Python library used for scientific computing and technical computing.
45.  Optical Character Recognition; the mechanical or electronic conversion of images of typed, handwritten or printed text into machine-encoded text.
46.  A free and open-source software suite for editing and converting raster image files.
47.  A shell script for cleaning image files of text.
48.  An optical character recognition tool for Python.
49.  A proprietary issue tracking product that allows bug tracking and agile project management.
50.  A diagram that shows the relationships of entity sets stored in a database.
51.  Python's standard GUI framework.
52.  An interactive command-line interface for Oracle Database.
53.  A method for finding the minimum of a function of several variables.
54.  A reverse proxy server and web cache.
55.  An open-source monitoring system.
56.  A configuration management tool.
57.  An approach to managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.
58.  An open-source software provisioning, configuration management, and application-deployment tool.
59.  A web-based graphical user interface for Ansible.
60.  A methodology that combines software development with information technology operations.
61.  A set of practices that combines software development (Dev) and IT operations (Ops) with a focus on security (Sec).
62.  Continuous Delivery; a software engineering approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time.
63.  The use of computers to control the entire production process.
64.  A database of Israeli citizens.
65.  The practice of merging all developer working copies to a shared mainline several times a day.
66.  A hosted continuous integration service used to build and test software projects hosted at GitHub.
67.  A text file that contains the definition of a Jenkins Pipeline.
68.  A programming language for the Java platform.
69.  A web server for the Windows NT family of operating systems.
70.  A web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
71.  A command-line interface for managing and automating VMware vSphere.
72.  The process of storing the state of a process or thread so that it can be restored and resume execution at a later point.
73.  The process of managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.
74.  An open source software for configuration management, remote execution, and monitoring.
75.  A software configuration management tool.
76.  A configuration management tool written in Ruby and Erlang.
77.  A human-readable data-serialization language.
78.  A command shell for interactive computing in multiple programming languages.
79.  A programming language that is a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python.
80.  A set of symbols that are used to identify and refer to objects of various kinds.
81.  A string of characters that unambiguously identifies a particular resource.
82.  A web application framework that is minimal, providing only the essential features needed to build a web application.
83.  A free and open-source utility used for writing image files such as .iso and .img files, as well as zipped folders onto storage media to create live SD cards and USB flash drives.
84.  The use of computers to store, retrieve, transmit, and manipulate data, or information.
85.  An application that is designed as a single, indivisible unit.
86.  A software architecture in which an application is designed as a single, indivisible unit.
87.  A software architecture in which an application is designed as a collection of loosely coupled services.
88.  A rule that states that a team should be small enough to be fed by two pizzas.
89.  A file format for representing electronic documents.
90.  A rule or pattern that specifies how a certain input sequence should be mapped to a replacement output sequence according to a defined procedure.
91.  A software architecture in which an application is designed as a collection of small services.
92.  A software architecture in which an application is designed as a collection of large services.
93.  A software architecture in which an application is designed as a collection of services that communicate with each other.
94.  A free and open-source media player software application.
95.  A collection of computer programs that are packaged together.
96.  An abstract model that organizes elements of data and standardizes how they relate to one another and to the properties of real-world entities.
97.  A data organization, management, and storage format that enables efficient access and modification.
98.  A model that describes the structure of a database.
99.  A model that describes the structure of a system in terms of objects, their attributes, and the relationships between them.
100.  A system that translates from one language to another.
101.  A data model in which the primary data structure is a network of nodes and links.
102.  A data model that is based on the principles of associative memory.
103.  A supply chain arrangement where a supplier of goods is responsible for generating orders and maintaining the inventory level of the consumer.
104.  A Python-based x86 emulator.
105.  A cross-language, cross-platform application programming interface for rendering 2D and 3D vector graphics.
106.  A tree representation of the abstract syntactic structure of source code written in a programming language.
107.  The process of making applications more secure by finding, fixing, and enhancing the security of apps.

## Data Science & AI/ML

<div class="annotate" markdown>

- `Computer Vision` (1)
- `Data Science` (2)
- `Deepfake` (3)
- `Q-learning` (4)
- `Neural Network` (5)
- `Primrose machine learning` (6)
- `RNN (Recurrent neural network)` (7)
- `LSTM (Long short-term memory)` (8)
- `CNN (Convolutional neural network)` (9)
- `Overfitting` (10)
- `underfitting` (11)
- `Sigmoid function` (12)
- `Gradient descent` (13)
- `Linear regression` (14)
- `Natural Language Processing (NLP)` (15)
- `Principal Component Analysis` (16)
- `t-Distributed Stochastic Neighbor Embedding` (17)
- `global average pooling (GAP)` (18)
- `deep learning` (19)
- `deep dream (deep learning)` (20)
- `classification model` (21)
- `exploratory data analysis (EDA)` (22)
- `latent dirichlet allocation (lda)` (23)
- `Depth-first search (DFS)` (24)
- `natural language understanding` (25)
- `natural language interpretation` (26)
- `python pandas` (27)
- `sklearn python` (28)
- `Sentiment analysis` (29)
- `Natural Language Toolkit` (30)
- `Synonym ring` (31)
- `supervised learining` (32)
- `Long short-term memory (LSTM)` (33)
- `Gated recurrent units (GRUs)` (34)
- `recurrent neural network (RNN)` (35)
- `dimensionality reduction` (36)
- `batch normalization` (37)
- `NeuroEvolution of Augmenting Topologies (NEAT)` (38)
- `genetic algorithm (GA)` (39)
- `chain rule` (40)
- `random forest` (41)
- `multinomial naive bayes` (42)
- `Multinomial logistic regression` (43)
- `anamorphic stretch transform` (44)

</div>

1.  An interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos.
2.  An interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.
3.  Synthetic media in which a person in an existing image or video is replaced with someone else's likeness.
4.  A model-free reinforcement learning algorithm to learn a policy telling an agent what action to take under what circumstances.
5.  A series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.
6.  A machine learning platform.
7.  A class of artificial neural networks where connections between nodes form a directed graph along a temporal sequence.
8.  An artificial recurrent neural network architecture used in the field of deep learning.
9.  A class of deep neural networks, most commonly applied to analyzing visual imagery.
10.  The production of an analysis that corresponds too closely or exactly to a particular set of data, and may therefore fail to fit additional data or predict future observations reliably.
11.  A model that neither models the training data well nor generalizes to new data.
12.  A mathematical function having a characteristic "S"-shaped curve or sigmoid curve.
13.  An optimization method that's used to train deep learning models.
14.  A statistical process for estimating the relationships among variables.
15.  A subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language.
16.  A statistical procedure that is used to reduce the dimensionality of a data set.
17.  A machine learning algorithm for visualization developed by Laurens van der Maaten and Geoffrey Hinton.
18.  A pooling operation designed to replace fully connected layers in classical CNNs.
19.  A subset of machine learning based on artificial neural networks with representation learning.
20.  A computer vision program created by Google engineer Alexander Mordvintsev which uses a convolutional neural network to find and enhance patterns in images via algorithmic pareidolia, thus creating a dream-like psychedelic appearance in the deliberately over-processed images.
21.  A supervised learning model that predicts a class label from a set of input features.
22.  An approach to analyzing data sets to summarize their main characteristics, often with visual methods.
23.  A generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.
24.  An algorithm for traversing or searching tree or graph data structures.
25.  A subtopic of natural language processing in artificial intelligence that deals with machine reading comprehension.
26.  The process of converting a natural language query into a formal representation of its meaning.
27.  A software library written for the Python programming language for data manipulation and analysis.
28.  A free software machine learning library for the Python programming language.
29.  The use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.
30.  A suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.
31.  A group of words that are considered to be synonyms.
32.  A type of machine learning in which an algorithm is trained on a labeled dataset.
33.  An artificial recurrent neural network architecture used in the field of deep learning.
34.  A gating mechanism in recurrent neural networks, introduced in 2014.
35.  A class of artificial neural networks where connections between nodes form a directed graph along a temporal sequence.
36.  The process of reducing the number of random variables under consideration by obtaining a set of principal variables.
37.  A method used to make artificial neural networks faster and more stable through normalization of the input layer by re-centering and re-scaling.
38.  A genetic algorithm for the generation of evolving artificial neural networks.
39.  A metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms.
40.  A method of computing the derivative of a composite function.
41.  An ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time.
42.  A Naive Bayes classifier for multinomial models.
43.  A classification method that generalizes logistic regression to multiclass problems, i.e. with more than two possible discrete outcomes.
44.  A method of stretching a widescreen image to fit a standard aspect ratio.

## Web Technologies

<div class="annotate" markdown>

- `PWA (Progressive Web Application)` (1)
- `SEO (Search Engine Optimization)` (2)
- `UX (User Experience)` (3)
- `svelte` (4)
- `IOT devices` (5)
- `Hyper-threading` (6)
- `document object module (DOM)` (7)
- `HID protocol` (8)

</div>

1.  A type of application software delivered through the web, built using common web technologies including HTML, CSS and JavaScript.
2.  The process of improving the quality and quantity of website traffic to a website or a web page from search engines.
3.  A person's emotions and attitudes about using a particular product, system or service.
4.  A free and open-source front-end component framework or language.
5.  A network of physical objects embedded with sensors and software to connect and exchange data over the Internet.
6.  A proprietary simultaneous multithreading implementation used by Intel to improve parallelization of computations performed on x86 microprocessors.
7.  An API for HTML and XML documents.
8.  A protocol for human interface devices.

## Hardware & Architecture

<div class="annotate" markdown>

- `ARM architecture` (1)
- `IOT devices` (2)
- `Hyper-threading` (3)
- `tty` (4)
- `ACPI` (5)
- `Hyper-V` (6)
- `Reduced instruction set computer architecture` (7)
- `arm processor` (8)
- `Complex instruction set computing architecture` (9)
- `x86 processor` (10)
- `cics architecture` (11)
- `cpu bound` (12)
- `io bound` (13)
- `ia64` (14)
- `compute unified device architecture (cuda)` (15)
- `commodity hardware` (16)
- `grid computing` (17)
- `grid network` (18)
- `Open Smart Grid Protocol (OSGP)` (19)
- `grok` (20)
- `virtual file system` (21)
- `filesystem in username (FUSE)` (22)
- `B tree` (23)
- `Sub volumes` (24)
- `Lustre` (25)
- `Electromagnetic compatibility (EMC)` (26)
- `electromagnetic interference (EMI)` (27)
- `Advanced Video Coding (AVC)` (28)
- `raspberry pi` (29)
- `system on chip (SoC)` (30)
- `qualcomm chip` (31)
- `connectivity chip` (32)
- `wireless connectivity types` (33)
- `Over-the-Air programming (OTA)` (34)

</div>

1.  A family of reduced instruction set computing (RISC) architectures for computer processors, configured for various environments.
2.  A network of physical objects embedded with sensors and software to connect and exchange data over the Internet.
3.  A proprietary simultaneous multithreading implementation used by Intel to improve parallelization of computations performed on x86 microprocessors.
4.  A teletypewriter, the device used for text-based communication.
5.  An open standard for unified power management.
6.  A native hypervisor developed by Microsoft.
7.  A computer instruction set that allows a computer's central processing unit to access data with a smaller number of instructions.
8.  A family of reduced instruction set computing architectures for computer processors, configured for various environments.
9.  A computer architecture where single instructions can execute several low-level operations.
10.  A family of instruction set architectures for computer processors.
11.  A family of IBM mainframe systems.
12.  A condition where the time it takes to complete a computation is determined principally by the speed of the central processor.
13.  A condition where the time it takes to complete a computation is determined principally by the period spent waiting for input/output operations to be completed.
14.  The 64-bit version of the Intel Itanium architecture.
15.  A parallel computing platform and application programming interface model created by Nvidia.
16.  Inexpensive and widely available computer hardware.
17.  A computer network composed of many networked loosely coupled computers that act together to perform large tasks.
18.  A network of computers that work together to perform a task.
19.  An open standard for secure, reliable, and scalable smart grid applications.
20.  A computer program that is used for parsing and structuring text data.
21.  An abstraction layer on top of a more concrete file system.
22.  A software interface for Unix and Unix-like computer operating systems that lets non-privileged users create their own file systems without editing kernel code.
23.  A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.
24.  A feature of some file systems that allows a single file system to be partitioned into multiple logical volumes.
25.  A parallel distributed file system, generally used for large-scale cluster computing.
26.  The ability of electrical equipment and systems to function acceptably in their electromagnetic environment, by limiting the unintentional generation, propagation and reception of electromagnetic energy.
27.  The disruption of operation of an electronic device when it is in the vicinity of an electromagnetic field in the radio frequency spectrum that is caused by another electronic device.
28.  A video compression standard.
29.  A series of small single-board computers.
30.  An integrated circuit that integrates all components of a computer or other electronic system.
31.  A chip that is used in mobile devices.
32.  A chip that is used for wireless communication.
33.  The different ways that wireless devices can connect to each other.
34.  A method of updating the software on a device wirelessly.

## Cryptography

<div class="annotate" markdown>

- `RSA Encryption` (1)
- `MD5` (2)
- `ROT13` (3)
- `vernam algorithm` (4)
- `Zero-knowledge proof` (5)
- `AES` (6)
- `ECB and CBC modes` (7)
- `Padding oracles` (8)
- `Caesar cipher` (9)
- `XOR` (10)
- `Site recovery menagment` (11)
- `orchestrator` (12)
- `Docker swarm` (13)
- `Application platform as a service (aPaaS)` (14)
- `hybrid cloud` (15)

</div>

1.  A public-key cryptosystem that is widely used for secure data transmission.
2.  A widely used hash function producing a 128-bit hash value.
3.  A simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet.
4.  A symmetric key encryption technique that cannot be cracked.
5.  A method by which one party (the prover) can prove to another party (the verifier) that they know a value x, without conveying any information apart from the fact that they know the value x.
6.  Advanced Encryption Standard; a symmetric block cipher chosen by the U.S. government to protect classified information.
7.  Electronic Codebook (ECB) and Cipher Block Chaining (CBC) are two modes of operation for a block cipher.
8.  A cryptographic oracle which replies to queries about whether a given ciphertext has a valid padding.
9.  A simple substitution cipher.
10.  A bitwise operation that outputs true only when inputs differ.
11.  A disaster recovery solution from VMware.
12.  A system that automates the deployment, scaling, and management of containerized applications.
13.  A container orchestration tool for Docker.
14.  A cloud computing model that provides a platform for developers to build and run applications without having to manage the underlying infrastructure.
15.  A cloud computing environment that uses a mix of on-premises, private cloud and third-party, public cloud services with orchestration between the two platforms.

## Storage

<div class="annotate" markdown>

- `DAS storage` (1)
- `RAID` (2)
- `File system` (3)
- `NAS storage` (4)
- `SAN storage` (5)
- `LUN (SAN)` (6)
- `Iscsi` (7)
- `Fiber chanel protocol (FCP)` (8)
- `fibre channel over ethernet (fcoe)` (9)
- `serial advanced technology attachment (sata)` (10)
- `Fibre Channel (FC)` (11)
- `fabric attached storage` (12)
- `Data ONTAP` (13)
- `trusted storage pool (TSP)` (14)
- `disk quota system` (15)
- `data deduplication` (16)
- `data compression` (17)
- `lun thin provisioning` (18)
- `multipath io` (19)
- `multipath storage` (20)
- `software defined storage` (21)
- `Input/Output Operations Per Second (iops)` (22)
- `throughput storage` (23)
- `software raid` (24)
- `firmware raid` (25)
- `hardware raid` (26)
- `erasure coding` (27)
- `lun zoning` (28)
- `lun masking` (29)
- `Vsan` (30)
- `Hybrid raid` (31)
- `radosgw` (32)

</div>

1.  Digital attached storage; a digital storage system directly attached to a server or workstation, without a network in between.
2.  Redundant Array of Independent Disks; a data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both.
3.  A data structure that a computer uses to organize and access data on a storage device.
4.  Network-attached storage; a file-level computer data storage server connected to a computer network providing data access to a heterogeneous group of clients.
5.  Storage area network; a computer network which provides access to consolidated, block-level data storage.
6.  Logical Unit Number; a number used to identify a logical unit, which is a device addressed by the SCSI protocol or by Storage Area Network protocols that encapsulate SCSI, such as Fibre Channel or iSCSI.
7.  Internet Small Computer Systems Interface; an Internet Protocol-based storage networking standard for linking data storage facilities.
8.  A transport protocol that predominantly transports SCSI commands over Fibre Channel networks.
9.  A computer network technology that allows Fibre Channel to run on top of Ethernet networks.
10.  A computer bus interface that connects host bus adapters to mass storage devices such as hard disk drives, optical drives, and solid-state drives.
11.  A high-speed data transfer protocol providing in-order, lossless delivery of raw block data.
12.  A storage device that is connected to a network.
13.  NetApp's proprietary operating system used in their storage systems.
14.  A pool of storage that is protected from unauthorized access.
15.  A system for limiting the amount of disk space a user can occupy.
16.  A specialized data compression technique for eliminating duplicate copies of repeating data.
17.  The process of modifying, encoding or converting the bits structure of data in such a way that it consumes less space on disk.
18.  A method for optimizing the efficiency with which the available space is utilized in storage area networks.
19.  A fault-tolerance and performance-enhancement technique that defines more than one physical path between the CPU in a computer system and its mass-storage devices.
20.  A storage system that has multiple paths from the host to the storage device.
21.  A form of storage virtualization that separates the storage hardware from the software that manages it.
22.  A performance measurement used to characterize computer storage devices like hard disk drives, solid state drives, and storage area networks.
23.  The amount of data that can be transferred from a storage device to a host in a given amount of time.
24.  A RAID system that is implemented entirely in software.
25.  A RAID system that is implemented in the system's BIOS.
26.  A RAID system that is implemented in a dedicated hardware controller.
27.  A method of data protection in which data is broken into fragments, expanded and encoded with redundant data pieces and stored across a set of different locations or storage media.
28.  A method of provisioning storage in a storage area network.
29.  A method of making a LUN available to some hosts and unavailable to others.
30.  A software-defined storage solution from VMware.
31.  A RAID system that combines multiple RAID levels.
32.  An object storage gateway for Ceph.

## Cloud Computing

<div class="annotate" markdown>

- `Cloud computing` (1)
- `P2V` (2)
- `V2V` (3)
- `IAAS` (4)
- `PAAS` (5)
- `SAAS` (6)
- `XAAS` (7)
- `Openstack` (8)
- `amazon elastic compute cloud (ec2)` (9)
- `mws clouding` (10)
- `fuse cloud` (11)
- `Cloud native` (12)
- `BAAS blockchain as a service` (13)
- `redhat tripleo` (14)
- `red hat openstack kola` (15)
- `Openshift` (16)
- `Serverless computing` (17)
- `Serverless Framework` (18)
- `egress` (19)
- `ingress` (20)
- `AWS Amplify` (21)
- `quantum computing as a service` (22)
- `Site recovery menagment` (23)
- `orchestrator` (24)
- `Docker swarm` (25)
- `Application platform as a service (aPaaS)` (26)
- `hybrid cloud` (27)

</div>

1.  The on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user.
2.  Physical-to-Virtual; the process of migrating a physical server's operating system, applications, and data from a physical server to a virtual machine.
3.  Virtual-to-Virtual; the process of migrating a virtual machine from one virtualization platform to another.
4.  Infrastructure as a Service; a cloud computing service model where a vendor provides users access to computing resources such as servers, storage and networking.
5.  Platform as a Service; a cloud computing model where a third-party provider delivers hardware and software tools to users over the internet.
6.  Software as a Service; a software licensing and delivery model in which software is licensed on a subscription basis and is centrally hosted.
7.  Anything as a Service; a cloud computing model that provides access to a wide range of services over the internet.
8.  An open standard cloud computing platform for all clouds.
9.  A web service that provides secure, resizable compute capacity in the cloud.
10.  A cloud computing service.
11.  A cloud-based file system.
12.  An approach to building and running applications that exploits the advantages of the cloud computing delivery model.
13.  A service that allows customers to use cloud-based solutions to build, host and use their own blockchain applications, smart contracts and functions on the blockchain.
14.  A project that aims to provide a production-ready cloud deployment of OpenStack.
15.  A tool for testing OpenStack deployments.
16.  A family of containerization software products from Red Hat.
17.  A cloud computing execution model in which the cloud provider runs the server, and dynamically manages the allocation of machine resources.
18.  A free and open-source web framework written using Node.js.
19.  Network traffic that exits a network.
20.  Network traffic that enters a network.
21.  A set of tools and services that can be used together or on their own, to help front-end web and mobile developers build scalable full stack applications, powered by AWS.
22.  A cloud computing service that provides access to quantum computers.
23.  A disaster recovery solution from VMware.
24.  A system that automates the deployment, scaling, and management of containerized applications.
25.  A container orchestration tool for Docker.
26.  A cloud computing model that provides a platform for developers to build and run applications without having to manage the underlying infrastructure.
27.  A cloud computing environment that uses a mix of on-premises, private cloud and third-party, public cloud services with orchestration between the two platforms.

## Big Data

<div class="annotate" markdown>

- `Big data` (1)
- `3 V's of big data` (2)
- `Big data ecosystem` (3)
- `Cloudera` (4)
- `Hadoop` (5)
- `Mesos` (6)
- `Yarn` (7)
- `Solr` (8)
- `Apache Pig` (9)
- `Apache Spark` (10)
- `Apache Kafka` (11)
- `Apache Storm` (12)
- `Apache ZooKeeper` (13)
- `HDFS` (14)
- `DataNode (HDFS)` (15)
- `NameNode (HDFS)` (16)
- `MapReduce` (17)
- `Apache Hive` (18)
- `Big data technologies` (19)
- `t-shark` (20)
- `software defined network` (21)
- `Data integrity` (22)
- `Ssh brute force attack` (23)
- `web server gateway interface (wsgi)` (24)
- `reverse tunneling` (25)
- `k8s` (26)

</div>

1.  A field that treats ways to analyze, systematically extract information from, or otherwise deal with data sets that are too large or complex to be dealt with by traditional data-processing application software.
2.  Volume, Velocity, and Variety; the three defining properties or dimensions of big data.
3.  The various tools and technologies that are used to store, process, and analyze big data.
4.  A software company that provides a software platform for data engineering, data warehousing, machine learning and analytics that runs in the cloud or on premises.
5.  A collection of open-source software utilities that facilitates using a network of many computers to solve problems involving massive amounts of data and computation.
6.  An open-source cluster manager.
7.  Yet Another Resource Negotiator; a component of Hadoop that is responsible for allocating system resources to the various applications running in a Hadoop cluster and scheduling tasks to be executed on different cluster nodes.
8.  An open-source enterprise-search platform, written in Java.
9.  A high-level platform for creating programs that run on Apache Hadoop.
10.  An open-source, distributed, general-purpose cluster-computing framework.
11.  A distributed event streaming platform.
12.  A distributed stream processing computation framework written predominantly in the Clojure programming language.
13.  A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.
14.  Hadoop Distributed File System; a distributed, scalable, and portable file-system written in Java for the Hadoop framework.
15.  A node in a Hadoop cluster that is responsible for storing data.
16.  A node in a Hadoop cluster that is responsible for managing the file system namespace and regulating access to files by clients.
17.  A programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.
18.  A data warehouse software project built on top of Apache Hadoop for providing data query and analysis.
19.  A set of tools and technologies for working with big data.
20.  A network protocol analyzer.
21.  A networking approach that uses software-based controllers or application programming interfaces to communicate with underlying hardware infrastructure and direct traffic on a network.
22.  The maintenance of, and the assurance of the accuracy and consistency of, data over its entire life-cycle.
23.  A method of guessing a password by systematically trying all possible combinations of letters, numbers, and symbols.
24.  A simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.
25.  A technique for creating a connection from a private network to a public network.
26.  An open-source container-orchestration system for automating computer application deployment, scaling, and management.

<!--
  Orphaned definitions recovered during the 2026 re-section: these definitions
  existed in the original file but no term pointed to them. Re-attach a term or
  delete. (Kept here so the content is not lost.)
  [150] The protection of websites from unauthorized access, use, modification, destruction, or disruption.
  [151] A slow-rate HTTP POST denial-of-service tool.
  [152] A denial-of-service attack tool that creates a large number of HTTP requests with a small payload.
  [153] A botnet primarily involved in click fraud.
  [154] A DDoS botnet that targets Windows systems.
  [155] A botnet that targets Windows systems.
  [156] A malware strain used in targeted attacks.
  [157] A DDoS botnet.
  [158] A botnet primarily used for sending spam.
  [159] A botnet consisting of around 200,000 infected computers.
  [160] A Trojan horse malware package that runs on versions of Microsoft Windows.
  [161] A free and open-source reverse engineering tool developed by the NSA.
  [162] A professional who specializes in the analysis of malware samples.
  [213] A text editor for Unix-like computing systems or operating environments using a command line interface.
  [214] A Unix shell and command language.
  [215] A multi-paradigm, general-purpose programming language designed for performance and safety, especially safe concurrency.
  [216] A preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS).
  [217] An API for retrieving resources from a server.
  [218] A web application bundler.
  [219] A toolkit for automating painful or time-consuming tasks in your development workflow.
  [220] A feature in the .NET Framework that allows you to get information about loaded assemblies and the types defined within them, such as classes, interfaces, and value types.
  [221] A set of principles for software development under which requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams.
  [222] An open-source container orchestration system for automating software deployment, scaling, and management.
  [223] A free and open-source machine learning platform designed to enable composing, deploying, and managing portable and scalable machine learning workflows on Kubernetes.
  [224] A function that returns a generator object.
  [225] A keyword in Python that is used to return from a function without destroying the states of its local variable.
  [226] A design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
  [227] A general-purpose programming language and integrated development environment (IDE).
  [228] An integrated development environment for rapid application development of desktop, mobile, web, and console software.
  [229] A parallel computing platform and application programming interface (API) model created by Nvidia.
  [230] An open standard for parallel programming of heterogeneous systems.
  [231] A file format used to store data, such as a spreadsheet or database, in a plain text format.
  [232] A family of two high-level, general-purpose, interpreted, dynamic programming languages.
  [233] A free and open-source, cross-platform FTP application.
-->
