# SIEM Concepts & Detection Rules – Ronald Walker

This document outlines key Security Information and Event Management (SIEM) concepts, how alerts are generated, and how correlation rules help detect real-world threats. These concepts are used across SOC environments.

---

# 🧠 What Is a SIEM?

A **SIEM (Security Information and Event Management)** system:
- Collects logs from multiple sources  
- Normalizes and parses data  
- Correlates events  
- Generates alerts  
- Supports investigations, dashboards, reporting, and threat hunting  

Common SIEMs:
- Splunk  
- Elastic SIEM  
- Microsoft Sentinel  
- QRadar  
- LogRhythm  

---

# 🗂️ Core SIEM Components

### **1. Log Collection**
Pulls data from:
- Operating systems  
- Firewalls  
- IDS/IPS  
- Active Directory  
- Cloud services  
- Applications & APIs  

### **2. Parsing & Normalization**
Converts logs into a consistent schema:
- `source.ip`
- `destination.port`
- `event.action`
- `user.name`
- `process.name`

### **3. Correlation Engine**
Creates **logic rules** that combine events into alerts.

### **4. Dashboards & Visualizations**
For monitoring trends and suspicious activity.

### **5. Alerting**
Triggers when rule conditions are met.

### **6. Case Management**
Allows analysts to track investigations.

---

# 🛡️ SIEM Use Cases

SIEMs detect:
- Brute-force attacks  
- Password spraying  
- Lateral movement  
- Malware execution  
- Privilege escalation  
- Suspicious login patterns  
- Data exfiltration attempts  

Your labs already demonstrate several use cases (brute force, scanning, log analysis).

---

# 🔍 Detection Rule Basics (Core Logic)

A SIEM rule is typically built using:

### **IF + AND/OR + THEN logic**

Example structure:

