# Wireshark Packet Analysis Guide

*(Note: These are descriptive summaries and mockups representing typical Wireshark captures.)*

## 1. TCP 3-Way Handshake
When a client connects to a server, Wireshark captures three packets establishing the connection:
1. **SYN (Synchronize):** Client -> Server (I want to connect)
2. **SYN-ACK:** Server -> Client (I acknowledge, let's connect)
3. **ACK (Acknowledge):** Client -> Server (Acknowledged, connection established)

**Analysis:** This is the foundation of any TCP connection. Filtering by `tcp.flags.syn == 1` helps identify connection attempts.

## 2. Cleartext HTTP Credentials
When a user logs into a site using HTTP instead of HTTPS, Wireshark captures the plaintext credentials.
- **Filter:** `http.request.method == "POST"`
- **Payload Analysis:** Looking at the "HTML Form URL Encoded" section reveals `username=admin&password=secretpassword`.

## 3. DNS Resolution
Before connecting to a web server, the system resolves the domain.
- **Filter:** `dns`
- **Analysis:** You will see a standard query.

> **Screenshot Mockup:**
> `[No. 45] [Time: 1.234] [Source: 192.168.1.5] [Destination: 8.8.8.8] [Protocol: DNS] [Info: Standard query 0x1a2b A example.com]`
