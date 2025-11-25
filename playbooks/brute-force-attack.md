# Playbook: Brute Force Attack (SSH Login Attempts)

## 🎯 Purpose
This playbook outlines the steps for identifying, triaging, containing, and responding to brute-force login attempts—specifically repeated failed SSH authentications.

---

# 1. Alert Summary

**Alert Name:** Multiple Failed SSH Login Attempts  
**Alert Source:** Authentication Logs / SIEM (auth.log, system.log)  
**Severity:** Medium (can escalate to High if successful login occurs)  
**MITRE ATT&CK Mapping:**  
- **T1110 — Brute Force**

---

# 2. Trigger Conditions
Alert fires when:

- More than **5 failed SSH attempts** within **60 seconds**  
- Same external IP attempts multiple usernames  
- Signs of credential stuffing (many users attempted)  
- “Failed password for invalid user” entries seen repeatedly  

---

# 3. Initial Triage (What to check first)

### ✔ Check logs for patterns
Commands:

```bash
grep -i "failed" /var/log/auth.log
grep -i "invalid" /var/log/auth.log
grep -i "password" /var/log/auth.log
