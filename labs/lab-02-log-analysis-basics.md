# Lab 02 – Log Analysis Basics

## Objective
Understand how to analyze system logs for security-related events such as failed logins, authentication issues, and suspicious activity.

## Tools
- Any `.log` file (macOS, Linux, or sample logs)
- `grep` (optional)
- Python (optional for automated parsing)
- GitHub `simple_log_parser.py` script (from this repo)

---

## Steps

### 1. Identify the log file
Common log locations:

- macOS: `/var/log/system.log`
- Linux: `/var/log/auth.log`, `/var/log/syslog`
- Application logs: `application.log`, `access.log`, etc.

For this lab, I used a basic system/auth log.

---

### 2. Manually review log entries
Look for:

- `failed`
- `denied`
- `authentication`
- `error`
- `login`
- `invalid user`

Example patterns:
Failed password for invalid user root from 192.168.1.50 port 52214


---

### 3. Use grep to filter specific events (optional)
```bash
grep -i "failed" /var/log/auth.log
grep -i "error" /var/log/system.log
grep -i "invalid" /var/log/auth.log
