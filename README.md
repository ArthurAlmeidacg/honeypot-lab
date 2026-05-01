# honeypot-lab - Intrusion Detection in Industrial Environments

A honeypot-based attack detection system, simulating the security 
architecture of a manufacturing company. It captures, records, 
and analyzes intrusion attempts in real time.

## Architecture

The project simulates three layers of defense:

- **DMZ** — externally exposed honeypot captures bots and scanners
- **Corporate network** — honeytoken (fake file) detects internal threats
- **OT network** — industrial honeypot detects lateral movement toward machines

##Real collected results

| Metric	| Value |
|---|---|
| Total attempts	| 2,996 |
| Collection period |	7 minutes |
| Most attacked port |	21/FTP — 1,393 attempts |
| Most attempted credential |	admin:password123 — 347 times |
| Unique IPs identified |	1 (local environment) |

**Top captured payloads:**

- `USER admin` — 347 attempts
- `USER root` — 280 attempts
- `GET /wp-admin` — 143 attempts
- `POST /admin` — 143 attempts

**Analysis conclusion:** 100% automated botnet traffic,
with no human interaction identified. Typical large-scale scanning pattern.

## Technologies used

- Python 3.11
- Paramiko — SSH protocol implementation
- Socket — low-level TCP server
- Threading — concurrency for multiple simultaneous connections
- JSON structured logging — structured logs for analysis

## How to run locally

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/ArthurAlmeidacg/honeypot-lab
cd honeypot-lab
pip install -r honeypot/requirements.txt
```
### Run

Terminal 1 — start the honeypot:

```bash id="j2k8p4"
python honeypot/honeypot.py
```

Terminal 2 — run the attack simulator:

```bash id="n7v3q1"
python simulation/simulator.py --intensity medium --duration 60
```

Terminal 3 — monitor logs in real time:

```bash id="r5m9t2"
# Windows
Get-Content honeypot_logs\honeypot_YYYYMMDD.json -Wait

# Linux/Mac
tail -f honeypot_logs/honeypot_YYYYMMDD.json
```

After data collection, generate the report:

```bash id="w4c6b8"
python analysis/analyze.py
```

## Project structure

```text id="p6d4s1"
honeypot-lab/
├── honeypot/
│   └── honeypot.py
├── simulation/
│   └── simulator.py
├── analysis/
│   └── analyze.py
├── playbooks/
│   ├── playbook_dmz.md
│   ├── playbook_honeytoken.md
│   └── playbook_ot.md
├── docs/
│   └── architecture.md
README.md
```


## What I learned

- How botnets behave in practice — automated scanning,
  credential wordlists, and target protocols
- The difference between external attacks and internal lateral movement
- How to structure incident response playbooks
- Why OT/IT separation is critical in industrial environments
- The importance of anonymizing data before publishing logs
