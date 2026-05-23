# Nmap Scan Examples and Analysis

## 1. TCP SYN "Stealth" Scan
The default and most popular scan. It sends a SYN packet and waits for a response.
**Command:** `nmap -sS target_ip`
**Sample Output:**
```text
Starting Nmap 7.92
Nmap scan report for target_ip (192.168.1.10)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

## 2. Service Version Detection
Probes open ports to determine what service and version are running.
**Command:** `nmap -sV target_ip`
**Sample Output:**
```text
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
```

## 3. Aggressive Scan
Enables OS detection, version detection, script scanning, and traceroute.
**Command:** `nmap -A target_ip`
