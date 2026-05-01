# Playbook — DMZ Honeypot Triggered

## Scenario

External bot attempting to access services in the DMZ.

## Severity

Low to medium, depending on the source.

## Response steps

1. Identify the source IP in the logs
2. Check IP reputation (AbuseIPDB, VirusTotal)
3. Block the IP on the perimeter firewall
4. Verify whether the IP made other attempts in the last 7 days
5. Add the IP to the internal threat intelligence feed
6. Document the incident and close the ticket

## Escalation criteria for high severity

* IP belongs to a known APT range
* Volume exceeds 1,000 attempts per hour
* Payload indicates a specific exploit rather than generic scanning
