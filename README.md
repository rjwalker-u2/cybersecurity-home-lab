# 🔐 Cybersecurity Portfolio – Ronald Walker

Welcome to my cybersecurity home lab and blue-team portfolio.  
I am a **CompTIA Security+ certified** cybersecurity professional focused on SOC operations, defensive security, and hands-on technical skills.

This repository showcases:
- 🧪 **Hands-on labs** (network scanning, log analysis, incident response)
- 🧰 **Python security tools** (log parser, port scanner, integrity checker)
- 🛡️ **Blue team playbooks** (brute force attack, SSH hardening)
- 🐳 **Docker & home lab architecture** (multi-container security toolkit)
- 📘 **Security+ notes** that demonstrate my understanding of all core domains
- 📄 **Skills overview** for recruiters and hiring managers

This portfolio is continuously updated as I grow in defensive security, automation, and threat detection.
# cybersecurity-home-lab
Documenting my journey into cybersecurity: labs, notes, blue team projects
# Cybersecurity Home Lab & Notes

Welcome! 👋  
This repo documents my journey breaking into cybersecurity — from Security+ studies to home lab projects, Docker experiments, and blue team tooling.

---

## 🎯 About Me

- Master of Science in Psychology (Capella University, 2024)  
- Bachelor of Science in Health Science (Wilmington University, 2021)  
- CompTIA Security+ certified  
- Transitioning into cybersecurity with a focus on:
  - Blue team operations
  - Governance, risk, and compliance (GRC)
  - Identity and access management
  - Home lab and hands-on projects

---

## 📁 Repo Structure

Planned structure for this project:

```text
.
├── notes/
│   ├── security-plus-notes.md
│   ├── docker-notes.md
│   └── linux-basics.md
├── labs/
│   ├── lab-01-basic-network-scanning.md
│   ├── lab-02-log-analysis-basics.md
│   └── lab-03-home-lab-plan.md
├── scripts/
│   ├── simple_log_parser.py
│   └── port_checker.py
└── README.md
# Network Traffic Analysis Lab (Wireshark + Nmap)

## Objective
To simulate network scanning activity and analyze packet-level traffic using Wireshark.

## Tools Used
- Ubuntu (VirtualBox)
- Wireshark
- Nmap

## Lab Setup
- Created a virtual machine using VirtualBox
- Installed Ubuntu Linux
- Installed Wireshark and Nmap
- Configured network interface for packet capture

## Steps Performed

### 1. Network Traffic Capture
- Started Wireshark on interface (enp0s3)
- Generated traffic using ping:ping -c 5 google.com
- Applied filter: icmp
### 2. Port Scanning Simulation
- Identified local IP address: ip a
- Ran SYN scan:sudo nmap -sS 10.0.2.15
### 3. Traffic Analysis
- Observed TCP SYN packets in Wireshark
- Applied filter:tcp.flags.syn == 1
- Identified scanning behavior and packet patterns

## Key Takeaways
- Learned how to capture and analyze live network traffic
- Understood how port scans appear at the packet level
- Practiced filtering and investigating suspicious activity

## Skills Demonstrated
- Packet Analysis
- Network Monitoring
- Linux Command Line
- Troubleshooting
- Cybersecurity Fundamentals