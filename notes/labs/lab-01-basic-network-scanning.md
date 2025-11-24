# Lab 01 – Basic Network Scanning

## Objective
Practice basic network scanning and service enumeration using `nmap`.

## Tools
- `nmap`
- Linux or macOS terminal

## Steps

### 1. Ping the target
```bash
ping <target-ip>
nmap <target-ip>
nmap -sV <target-ip>
nmap -sV -oN scan-results.txt <target-ip>
