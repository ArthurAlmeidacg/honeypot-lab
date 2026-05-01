# Playbook — Honeytoken Accessed

## Scenario

Fake file accessed inside the corporate network.
Any access is considered suspicious — legitimate users are not aware of this file.

## Severity

High

## Response steps

1. Identify the user and workstation that accessed the file
2. Isolate the workstation from the network — do not shut it down (preserve RAM)
3. Suspend the account in Active Directory
4. Audit in the SIEM which other files this account accessed
5. Verify whether the account may have been compromised through phishing
6. Notify HR and legal teams
7. Preserve logs and acquire a forensic disk image for potential legal proceedings

## Escalation criteria for critical severity

* Files were copied to an external device or cloud storage
* Access occurred outside business hours
* Multiple honeytokens were accessed by the same account
