 Linux Commands for Cybersecurity & System Administration

 1. Basic File & Directory Management

  Print Current Directory

 bash
pwd
 

Displays the current working directory.

 

  List Files and Directories

 bash
ls
 

  Advanced Listing

 bash
ls -la
 

Options:

* `-l` → Long format
* `-a` → Show hidden files

 

  Change Directory

 bash
cd /home/user/Documents
 

Move between directories.

  Return to Previous Directory

 bash
cd ..
 

 

  Create Directory

 bash
mkdir cybersecurity
 

  Create Nested Directories

 bash
mkdir -p projects/week1/notes
 

 

  Create Files

 bash
touch notes.txt
 

  Multiple Files

 bash
touch file1.txt file2.txt file3.txt
 

 

 2. File Operations

  Copy Files

 bash
cp source.txt destination.txt
 

  Copy Directories Recursively

 bash
cp -r folder1 folder2
 

 

  Move or Rename Files

 bash
mv old.txt new.txt
 

 

  Remove Files

 bash
rm file.txt
 

  Remove Directories Recursively

 bash
rm -rf foldername
 

⚠ Warning:
`rm -rf` permanently deletes files.

 

 3. Viewing File Contents

  Display File Content

 bash
cat file.txt
 

 

  View Large Files

 bash
less largefile.log
 

Navigation:

* `q` → Quit
* `/keyword` → Search

 

  Read First Lines

 bash
head -n 10 file.txt
 

 

  Read Last Lines

 bash
tail -n 20 logs.txt
 

  Real-Time Monitoring

 bash
tail -f access.log
 

Used heavily in SOC monitoring.

 

 4. User & Permission Management

  Check Current User

 bash
whoami
 

 

  View User Identity

 bash
id
 

 

  Switch User

 bash
su username
 

 

  Run Command as Administrator

 bash
sudo apt update
 

 

 5. Linux File Permissions

  Permission Structure

Example:

 bash
-rwxr-xr--
 

Meaning:

* Owner → Read, Write, Execute
* Group → Read, Execute
* Others → Read

 

  Change Permissions

 bash
chmod 755 script.sh
 

  Numeric Permission Breakdown

| Number | Permission |
|    |    - |
| 7      | rwx        |
| 6      | rw-        |
| 5      | r-x        |
| 4      | r--        |

 

  Change Ownership

 bash
chown user:user file.txt
 

 

 6. Process Management

  View Running Processes

 bash
ps aux
 

 

  Real-Time Process Monitoring

 bash
top
 

  Improved Version

 bash
htop
 

 

  Kill Process

 bash
kill PID
 

  Force Kill

 bash
kill -9 PID
 

 

 7. Networking Commands

  Check IP Address

 bash
ip addr
 

 

  Test Connectivity

 bash
ping google.com
 

 

  DNS Lookup

 bash
nslookup google.com
 

 

  Show Open Ports

 bash
netstat -tulnp
 

  Modern Alternative

 bash
ss -tulnp
 

 

  Trace Network Path

 bash
traceroute google.com
 

 

 8. Cybersecurity & Penetration Testing Commands

  Network Scanning with Nmap

  Basic Scan

 bash
nmap 192.168.1.1
 

 

  Service Version Detection

 bash
nmap -sV 192.168.1.1
 

 

  Aggressive Scan

 bash
nmap -A 192.168.1.1
 

 

  Scan Specific Ports

 bash
nmap -p 80,443 192.168.1.1
 

 

 9. Packet Analysis Commands

  Start Wireshark

 bash
wireshark
 

 

  Packet Capture via Terminal

 bash
tcpdump -i eth0
 

  Save Capture

 bash
tcpdump -i eth0 -w capture.pcap
 

 

 10. File Searching & Analysis

  Find Files

 bash
find / -name passwords.txt
 

 

  Search Inside Files

 bash
grep "admin" users.txt
 

  Recursive Search

 bash
grep -r "password" /var/log
 

 

 11. Disk & System Information

  Disk Usage

 bash
df -h
 

 

  Directory Size

 bash
du -sh foldername
 

 

  System Information

 bash
uname -a
 

 

  Memory Usage

 bash
free -h
 

 

 12. Package Management

  Update Packages

 bash
sudo apt update
 

 

  Upgrade Packages

 bash
sudo apt upgrade
 

 

  Install Software

 bash
sudo apt install nmap
 

 

 13. SSH & Remote Access

  Connect to Remote Server

 bash
ssh user@192.168.1.10
 

 

  Secure File Transfer

 bash
scp file.txt user@192.168.1.10:/home/user/
 

 

 14. Log Analysis & Monitoring

  Authentication Logs

 bash
cat /var/log/auth.log
 

 

  Failed Login Attempts

 bash
grep "Failed password" /var/log/auth.log
 

 

  Monitor System Logs

 bash
journalctl -xe
 

 

 15. Bash Scripting Basics

  Create Script

 bash
nano script.sh
 

 

  Example Script

 bash
 !/bin/bash

echo "Cybersecurity Scan Started"
date
whoami
 

 

  Make Script Executable

 bash
chmod +x script.sh
 

 

  Run Script

 bash
./script.sh
 

 

 16. Advanced Linux Security Commands

  Check Listening Ports

 bash
lsof -i -P -n
 

 

  Check Logged-In Users

 bash
w
 

 

  File Integrity Verification

 bash
sha256sum file.txt
 

 

  Generate SSH Keys

 bash
ssh-keygen
 

 

 17. Malware & Suspicious Activity Detection

  Find SUID Files

 bash
find / -perm -4000 2>/dev/null
 

Important for privilege escalation analysis.

 

  Check Cron Jobs

 bash
crontab -l
 

Attackers often use cron persistence.

 

  Monitor Active Connections

 bash
netstat -antp
 

 

 18. Compression & Archiving

  Create Archive

 bash
tar -cvf backup.tar folder/
 

 

  Extract Archive

 bash
tar -xvf backup.tar
 

 

  Compress with Gzip

 bash
gzip file.txt
 

 

 19. Ethical Hacking Linux Environment

Common cybersecurity distributions:

* Kali Linux
* Parrot Security OS

Common tools:

* Burp Suite
* Metasploit Framework
* John the Ripper

 

 20. Professional Linux Learning Path

  Beginner

* File management
* Permissions
* Networking basics
* Package management

  Intermediate

* Bash scripting
* SSH
* Process monitoring
* Log analysis

  Advanced

* Kernel tuning
* Security hardening
* Automation
* Penetration testing
* Malware analysis
* Digital forensics

 

 Final Note

Linux mastery is one of the most valuable skills in cybersecurity. Security analysts, penetration testers, SOC engineers, cloud engineers, and red team operators rely heavily on Linux environments for:

* Threat detection
* Vulnerability analysis
* Security automation
* Infrastructure management
* Ethical hacking
* Incident response

The more comfortable you become with Linux command-line operations, the more capable you become as a cybersecurity professional.
