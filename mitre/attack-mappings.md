# MITRE ATT&CK Mappings – Ronald Walker

This document maps the techniques, behaviors, and detections from my labs, scripts, and playbooks to the MITRE ATT&CK (Enterprise) framework. This demonstrates how each activity in my home lab aligns to real-world adversarial behaviors and SOC detection use cases.

---

# 🔐 Credential Access (TA0006)

## **T1110 – Brute Force**
**Where in my portfolio:**
- Lab 04: Incident Response Simulation (failed SSH login attempts)
- Brute Force Attack Playbook
- Log Analysis Lab (Lab 02)
- Python log parser script

**Detections:**
- Excessive failed logins
- Invalid user attempts
- Attempts from the same external IP
- Multiple usernames tried in short timeframes

**Defensive Controls:**
- MFA
- SSH key-based authentication
- Lockout policies
- Firewall rules to block malicious IPs

---

# 🚨 Discovery (TA0007)

## **T1046 – Network Service Scanning**
**Where in my portfolio:**
- Lab 01: Basic Network Scanning
- Custom port_checker.py script
- Docker-based Nmap Scanner API project (in progress)

**Detections:**
- High volume of connection attempts
- Sequential port scans
- SYN scanning behavior

**Defensive Controls:**
- Network segmentation  
- IDS/IPS  
- Firewall rules  

---

# ⚙️ Execution (TA0002)

## **T1059 – Command and Scripting Interpreter (Linux/Unix Bash)**
**Where in my portfolio:**
- Linux log review (grep commands)
- Custom Python automation scripts
- Incident response evidence collection
- Security+ IAM and endpoint hardening notes

**Detections:**
- Suspicious shell commands
- Unexpected process execution
- Unusual authentication attempts

---

# 🧰 Defense Evasion (TA0005)

## **T1027 – Obfuscated/Encrypted Files or Information**
*(Indirect via file integrity concepts)*

**Where in my portfolio:**
- File Integrity Checker (SHA-256 hashing)
- Security+ cryptography notes

**Detections:**
- Modified system files
- Unexpected hash changes
- Unauthorized changes to logs or binaries

**Defensive Controls:**
- Integrity monitoring
- SIEM correlation
- Change control

---

# 🛡️ Persistence (TA0003)

## **T1098 – Account Manipulation**
*(Referenced in IR simulation and playbooks)*

**Where in my portfolio:**
- Lab 04 (checking authorized_keys)
- SSH hardening recommendations
- IAM & Security+ notes

**Detections:**
- New or modified SSH keys
- Unexpected user accounts
- Unauthorized group membership changes

---

# 📡 Command & Control (TA0011)

## **T1071 – Application Layer Protocol**
*(Conceptual mapping from Nmap + port checking)*

**Where in my portfolio:**
- Port checker script  
- Network scanning lab  
- Docker multi-service networking notes  

**Detections:**
- Unexpected open ports  
- Services running on non-standard ports  
- Outbound connections from internal hosts  

---

# 📝 Additional Techniques Mapped

### **T1003 – Credential Dumping**  
Referenced in Security+ notes (LSASS, hashes, password protections)

### **T1566 – Phishing**  
Mapped through IAM notes + future playbook expansion

### **T1499 – Endpoint Denial of Service**  
Referenced in network security notes (SYN flood)

### **T1082 – System Information Discovery**  
Covered in labs involving enumeration and system log review

---

# ✔️ Summary

These MITRE ATT&CK mappings demonstrate:
- How my labs align to real attacker techniques  
- How my scripts support detection and triage  
- Understanding of adversarial behavior and SOC defensive workflows  
- Application of Security+ knowledge to hands-on investigations  

This file will continue to grow as I expand my home lab, write additional playbooks, and build new detection tools.
