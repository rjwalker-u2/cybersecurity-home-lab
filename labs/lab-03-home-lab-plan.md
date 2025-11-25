# Lab 03 – Home Lab Plan (Docker, VMs, and Blue Team Tools)

## Objective
Design a beginner-friendly cybersecurity home lab that supports hands-on learning in network scanning, log analysis, identity management, and incident response.

This plan outlines the tools, layout, and project roadmap for building my personal blue-team/defensive security lab.

---

## 🖥️ Lab Goals
- Build and containerize basic security tools (scanner, log analyzer)
- Practice SOC-style investigations
- Analyze logs from multiple sources
- Run Kali Linux for offensive testing
- Maintain notes, screenshots, and documentation in GitHub
- Learn modern security workflows using Docker and Python

---

## 🧱 Home Lab Architecture
Host Machine
│
├── Docker Toolkit (on newer laptop)
│ ├── Nmap Scanner API
│ ├── Log Analyzer API
│ └── Custom Python tools
│
├── Kali Linux VM (VirtualBox)
│ ├── Scanning
│ ├── Password attacks
│ ├── Recon/Enumeration
│
└── GitHub Repository
├── Labs
├── Notes
├── Scripts
└── Documentation

This structure allows me to separate offensive tools (Kali), defensive tools (logging & analysis), and documentation (GitHub).

---

## 🧰 Tools I Plan to Use

### 🔹 **1. Docker-Based Tools**
These will run on my newer machine (not the old Mac):

- Custom Nmap scan API  
- Log analyzer API  
- Python scripts containerized for portability  
- Docker Compose for multi-service apps  

### 🔹 **2. Virtual Machines**
- **Kali Linux** for penetration testing  
- (Optional later) **Ubuntu Server** for log generation and Syslog practice  

### 🔹 **3. Python Scripts**
- Log parsing  
- Port scanning  
- File integrity checking  
- Keyword alerting  

### 🔹 **4. GitHub for Documentation**
This repository will track:

- Labs  
- Projects  
- Scans  
- Findings  
- Notes  
- Screenshots  

---

## 🚀 Phase Breakdown

### **Phase 1 — Documentation & Scripts (Current Phase)**
- Build Markdown labs  
- Add beginner-friendly security scripts  
- Learn Python basics  
- Document everything in GitHub

### **Phase 2 — Docker Toolkit (Next)**
- Create containerized scanner  
- Add custom APIs  
- Use Docker Compose for multiple tools  
- Add healthchecks, volumes, and networking

### **Phase 3 — Kali VM Work**
- Learn scanning, enumeration, and reporting  
- Test simple attacks and analyze logs  
- Document findings in `labs/`

### **Phase 4 — Blue Team Workflow**
- Collect logs  
- Analyze events (failed logins, errors, suspicious IPs)  
- Build alerts using Python  
- Create mock incident response documentation  

---

## 📈 What I Expect to Learn
- Realistic scanning & recon workflows  
- Docker concepts (images, containers, Compose, networking)  
- SOC analysis patterns  
- Log investigation  
- Python automation  
- GitHub project structure  
- Incident documentation  

---

## 📝 Next Steps
- Add more Python scripts to `scripts/`
- Create screenshots of Docker containers on the other laptop
- Add a simple API endpoint for nmap scanning
- Add credential brute force detection in log parser

