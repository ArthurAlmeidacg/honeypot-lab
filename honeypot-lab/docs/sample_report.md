# Honeypot Lab — Attack Analysis Report
 
**Collection date:** 03/29/2026  
**Duration:** 7 minutes (local environment with attack simulator)  
**Environment:** Windows 11, Python 3.11, local network 127.0.0.1  
 
 
## Executive Summary
 
During the collection period, the honeypot recorded **2,996 access attempts**
originating from a single IP (simulated environment). The behavior pattern identified
is consistent with automated botnet scanning — no human interaction detected.
 
FTP (port 21) and SSH (port 22) concentrated 85% of all attacks, reflecting the
global pattern of exploiting misconfigured remote access services.
 

## Results by Port
 
| Port | Service | Attempts | % of Total |
|------|---------|----------|------------|
| 21   | FTP     | 1,393    | 46.5%      |
| 22   | SSH     | 1,174    | 39.2%      |
| 80   | HTTP    | 429      | 14.3%      |
 
 
## Top 10 Credentials Attempted
 
| Rank | Username | Password       | Attempts |
|------|----------|----------------|----------|
| 1    | admin    | password123    | 347      |
| 2    | root     | admin123       | 280      |
| 3    | test     | 123456         | 279      |
| 4    | user     | root           | 278      |
| 5    | admin    | admin123       | 143      |
| 6    | root     | password123    | 143      |
| 7    | test     | 123456         | 143      |
| 8    | admin    | 123456         | 117      |
| 9    | root     | toor           | 69       |
| 10   | admin    | admin          | 68       |
 
 
## Top HTTP Payloads Captured
 
| Payload                        | Attempts |
|-------------------------------|----------|
| GET / HTTP/1.1                | 143      |
| POST /admin HTTP/1.1          | 143      |
| GET /wp-admin HTTP/1.1        | 143      |

## Behavior Analysis
 
**Automation indicators identified:**
 
- Interval between attempts under 0.3 seconds
- Sequential use of standard wordlist (admin, root, test, user)
- No User-Agent variation in HTTP requests
- SSH protocol attempted without valid key negotiation
**Conclusion:** 100% automated traffic. No manual attempts identified.