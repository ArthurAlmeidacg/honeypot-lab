# Playbook — OT Honeypot Accessed

## Scenario

Connection originating from the IT network attempting to access a fake industrial controller.
This indicates lateral movement toward physical machines.

## Severity

Critical — P1

## Immediate response steps (first 15 minutes)

1. Notify the security manager and executive leadership immediately
2. Isolate the OT segment from the IT segment on the intermediate firewall
3. Notify shop floor operators to check for anomalous behavior on physical CNC machines
4. Identify the source machine within the IT network

## Investigation (first 2 hours)

5. Trace how the source machine was compromised
6. Map the full path taken by the attacker across the network
7. Verify whether data was exfiltrated before containment
8. Engage an incident response company if necessary

## Post-incident

9. Produce a full report from the initial attack vector to the OT honeypot
10. Review OT/IT firewall rules
11. Train the team on the attack vector used
