import datetime
import json
from collections import Counter

def analyze_logs(log_file):
    ip_analysis = {}
    hourly_attacks = {}
    port_analysis = {}
    payloads = []

    with open(log_file, 'r') as f:
        for line in f:
            try:
                activity = json.loads(line)
                timestamp = datetime.datetime.fromisoformat(activity['timestamp'])
                ip = activity['remote_ip']        # campo correto
                port = activity['port']
                data = activity['data'].strip()

                if ip not in ip_analysis:
                    ip_analysis[ip] = {
                        'total_attempts': 0,
                        'first_seen': timestamp,
                        'last_seen': timestamp,
                        'targeted_ports': set(),
                    }

                ip_analysis[ip]['total_attempts'] += 1
                ip_analysis[ip]['last_seen'] = timestamp
                ip_analysis[ip]['targeted_ports'].add(port)

                hour = timestamp.hour
                hourly_attacks[hour] = hourly_attacks.get(hour, 0) + 1

                port_analysis[port] = port_analysis.get(port, 0) + 1

                if data:
                    payloads.append(data)

            except (json.JSONDecodeError, KeyError):
                continue

    total = sum(hourly_attacks.values())
    print("\n=== Honeypot Analysis Report ===")
    print(f"\nTotal de tentativas: {total}")

    print("\nTop 10 IPs mais ativos:")
    for ip, stats in sorted(ip_analysis.items(),
                            key=lambda x: x[1]['total_attempts'],
                            reverse=True)[:10]:
        duration = stats['last_seen'] - stats['first_seen']
        print(f"  {ip} — {stats['total_attempts']} tentativas — portas: {stats['targeted_ports']} — duração: {duration}")

    print("\nPortas mais atacadas:")
    for port, count in sorted(port_analysis.items(), key=lambda x: x[1], reverse=True):
        print(f"  porta {port}: {count} tentativas")

    print("\nTop 10 payloads mais comuns:")
    for payload, count in Counter(payloads).most_common(10):
        resumo = payload[:60].replace('\r\n', ' ')
        print(f"  {count:4d}x  {resumo}")

    print("\nDistribuição por hora:")
    max_val = max(hourly_attacks.values()) if hourly_attacks else 1
    for hour in sorted(hourly_attacks.keys()):
        bar = "#" * (hourly_attacks[hour] * 20 // max_val)
        print(f"  {hour:02d}h {bar} {hourly_attacks[hour]}")

if __name__ == "__main__":
    today = datetime.datetime.now().strftime("%Y%m%d")
    analyze_logs(f"honeypot_logs/honeypot_{today}.json")