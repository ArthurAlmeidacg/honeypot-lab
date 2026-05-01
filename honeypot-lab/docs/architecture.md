# Honeypot Lab — Architecture
 
## Overview
 
This project simulates the security architecture of a manufacturing company,
with three honeypot layers covering different attack vectors.
 
 
## Network Diagram
 
```
                        [ Internet ]
                             │
                             ▼
                    [ Perimeter Firewall ]──── DMZ Honeypot
                             │                 (fake web server)
                             ▼
          ┌──────────────────────────────────┐
          │       Corporate Network (IT)     │
          │                                  │
          │  [CAD Workstations] [File        │
          │                  Server]  [ERP]  │
          │                                  │
          │  ⚠ Honeytoken: secret_           │
          │    projects.dwg                  │
          └──────────────────────────────────┘
                             │
                    [ OT/IT Firewall ]
                             │
                             ▼
          ┌──────────────────────────────────┐
          │       Industrial Network (OT)    │
          │                                  │
          │  [CNC]  [SCADA/PLC]  [Sensors]  │
          │                                  │
          │                  ⚠ OT Honeypot  │
          │                    (fake PLC)    │
          └──────────────────────────────────┘
```
 
 
## The Three Honeypots
 
### 1. DMZ Honeypot — Fake Web Server
 
**Location:** external network edge, internet-facing  
**Port:** 80 (HTTP)  
**Detects:** external scans, bots looking for admin panels,
WordPress and CMS exploits  
**Alert severity:** low to medium  
 
Any connection to this honeypot is suspicious — no legitimate user
should access it because it is not published anywhere.
 
 
### 2. Honeytoken — Fake File on Corporate Network
 
**Location:** shared file server on the internal network  
**Format:** `.dwg` (CAD project) or `.xlsx` file with an attractive name  
**Detects:** insider threats, phishing-compromised accounts,
attackers already inside the network searching for data to steal  
**Alert severity:** high  
 
Unlike a network honeypot, the honeytoken does not listen on any port —
it is a file monitored by the SIEM. If opened, immediate alert.
 
 
### 3. OT Honeypot — Fake PLC on Industrial Network
 
**Location:** production machines network segment  
**Protocol:** Modbus TCP (standard industrial protocol)  
**Detects:** lateral movement from IT network to OT network,
attacker trying to reach physical machines  
**Alert severity:** critical (P1)  
 
This is the most serious alert. It means an attacker crossed the OT/IT
firewall and is one step away from compromising the factory's
physical production.
 

## Data Flow
 
```
Attacker attempts connection
        │
        ▼
Honeypot captures: IP, port, payload, timestamp
        │
        ▼
Event saved as structured JSON log
        │
        ▼
analyze.py processes the logs
        │
        ▼
Report: top IPs, credentials, payloads, temporal distribution
        │
        ▼
SOC analyst acts based on the corresponding playbook
```
 
 
## Why Structured JSON
 
Each event is saved as an independent JSON line:
 
```json
{
  "timestamp": "2026-03-29T12:56:04",
  "remote_ip": "185.220.xx.xx",
  "port": 80,
  "data": "GET /wp-admin HTTP/1.1"
}
```
 
This format allows direct integration with SIEMs such as Splunk, Microsoft
Sentinel and Elastic SIEM — which is how it works in real corporate environments.
 
 
## Tech Stack
 
| Component | Technology | Why |
|-----------|-----------|-----|
| Fake SSH server | Python + Paramiko | full SSH protocol implementation |
| Generic TCP server | Python + Socket | captures any protocol (FTP, HTTP) |
| Concurrency | Threading | handles multiple simultaneous connections |
| Logging | Structured JSON | compatible with analysis and SIEM tools |
| Analysis | Python + Collections | data aggregation and ranking |
 

 