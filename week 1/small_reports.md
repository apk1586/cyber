# Vulnerability Assessment Report

## Executive Summary
A simulated vulnerability assessment was conducted on the target host `192.168.1.10`. The objective was to identify potential security weaknesses and provide remediation steps.

## Findings

### 1. High Severity: Unencrypted FTP Access
- **Description:** Port 21 is open and running vsftpd 2.3.4. This service allows unencrypted authentication and data transfer. Additionally, this specific version has a known backdoor vulnerability.
- **Remediation:** Disable FTP and migrate to a secure alternative such as SFTP (SSH File Transfer Protocol). 

### 2. Medium Severity: Outdated Web Server
- **Description:** Port 80 is running Apache 2.4.29, which is missing several security patches.
- **Remediation:** Upgrade the Apache package to the latest stable version provided by the OS vendor.

## Conclusion
The target system presents significant security risks, primarily due to the use of insecure, unencrypted protocols and outdated software. Immediate remediation is strongly advised.
