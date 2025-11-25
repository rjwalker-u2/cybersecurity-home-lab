# Security+ Notes  
**Author:** Ronald Walker  
**Certification:** CompTIA Security+ (SY0-701) — *Completed 2024*  

These notes reflect core Security+ knowledge areas I’ve studied and actively use in my home lab and defensive security projects.

---

# 🧠 1. Risk Management & Governance

### **Concepts**
- **Risk = Threat × Vulnerability**
- **Risk Response:** Mitigate, Transfer, Accept, Avoid
- **Data Classification:** Public → Internal → Confidential → Restricted

### **Frameworks**
- **NIST Cybersecurity Framework (CSF):** Identify → Protect → Detect → Respond → Recover  
- **NIST SP 800-53:** Controls for federal information systems  
- **SOC 2 Trust Principles:** Security, Availability, Processing Integrity, Confidentiality, Privacy  

### **Policies**
- Acceptable Use Policy (AUP)  
- Data retention  
- Account lockout & password policy  
- Change management (strategic + operational)  

---

# 🔐 2. Identity & Access Management (IAM)

### **Authentication Factors**
- **Something you know:** Password, PIN  
- **Something you have:** Smart card, token  
- **Something you are:** Biometrics  

### **Access Controls**
- **Least Privilege**
- **RBAC (Role-Based Access Control)**
- **ABAC (Attribute-Based Access Control)**
- **MAC vs DAC** (Mandatory vs Discretionary)

### **Common Technologies**
- MFA  
- SSO  
- OAuth / OIDC  
- Kerberos (Tickets | TGT | KDC)  
- LDAP / Active Directory basics  

---

# 🚨 3. Incident Response

### **NIST Incident Response Lifecycle**
1. **Preparation**  
2. **Identification**  
3. **Containment**  
4. **Eradication**  
5. **Recovery**  
6. **Lessons Learned**

### **Key Documentation**
- Runbooks (step-by-step tasks)  
- Playbooks (response templates for known threats)  
- Incident Reports  
- Chain of Custody  

### **Indicators**
- **IoC (Indicator of Compromise)** → artifact left by attacker  
- **IoA (Indicator of Attack)** → behavior that suggests attack in progress  

---

# 🧪 4. Network Security

### **Protocols**
- TCP vs UDP  
- HTTPS / TLS basics  
- SSH, SFTP  
- RDP (Remote Desktop Protocol)  
- SMB (File sharing in Windows environments)

### **Common Attacks**
- ARP Spoofing  
- DNS Poisoning  
- SYN Flood  
- Man-in-the-middle (MITM)  

### **Network Segmentation**
- VLANs  
- Firewalls  
- DMZs  

---

# 🛡️ 5. Endpoint & Application Security

### **Hardening Techniques**
- Remove unnecessary services  
- Disable default admin accounts  
- Patch management  
- Enforce strong password policy  
- Anti-malware tools  
- Host-based firewalls  

### **Secure Coding Practices**
- Input validation  
- Sanitization  
- OWASP Top 10 (Injection | Broken Auth | Access Control | XSS | etc.)  

---

# 🧰 6. Cryptography

### **Hashing**
- **SHA-256** (used in my file integrity script)
- MD5 (deprecated)
- Integrity only — no decryption

### **Symmetric Encryption**
- AES (industry standard)
- Used when speed matters  
- Same key for encrypt/decrypt  

### **Asymmetric Encryption**
- RSA  
- Public/private key pairs  
- Used for:  
  - Certificates  
  - Key exchange  
  - Digital signatures  

### **PKI Concepts**
- Certificate Authority (CA)  
- CSR (Certificate Signing Request)  
- CRL / OCSP (revocation checks)

---

# 🔍 7. Threats & Vulnerabilities

### **Common Attack Types**
- Brute Force (T1110)  
- SQL Injection  
- XSS  
- Directory Traversal  
- Phishing / Spear Phishing  
- Ransomware  
- Insider Threat  

### **Vulnerability Scanning**
- Authenticated vs unauthenticated scans  
- False positives  
- Patch prioritization (CVSS score + business impact)  

---

# ⚙️ 8. Security Operations (SOC Basics)

### **Log Sources**
- Authentication logs  
- System logs  
- Firewall logs  
- Web server logs  
- Application logs  

### **SIEM Concepts**
- Correlation rules  
- Dashboards  
- Alerts  
- Data normalization  

### **Common SOC Tasks**
- Investigate failed logins  
- Analyze suspicious IPs  
- Review user activity  
- Respond to alerts  
- Document incidents  

---

# 📘 Summary

These notes demonstrate the foundational and practical knowledge gained through completing the CompTIA Security+ certification and applying these concepts in my hands-on labs, scripts, and home lab environment.
