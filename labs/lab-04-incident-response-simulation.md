# Lab 04 – Incident Response Simulation (Unauthorized Login Attempts)

## Objective
Simulate a small security incident involving repeated failed login attempts from a suspicious IP address.  
Analyze the logs, determine impact, and document response actions following NIST incident response guidelines.

---

## 🧠 Scenario
During normal log review, multiple failed SSH login attempts were detected from a suspicious external IP address: `185.199.110.55`.

These attempts may indicate:
- Brute-force attempts  
- Credential stuffing  
- Reconnaissance activity  

This lab simulates how I would investigate, contain, and document the event.

---

## 🔍 Step 1 — Detection

Review authentication logs:

Failed password for invalid user admin from 185.199.110.55 port 52914
Failed password for root from 185.199.110.55 port 52914
Failed password for testuser from 185.199.110.55 port 52921
Accepted password for validuser from 10.0.0.12 port 44210
Failed password for root from 185.199.110.55 port 52930

Key indicators:
- Many attempts in a short time frame  
- Multiple usernames being tried  
- External IP origin  

---
