from collections import Counter
alerts_a = ["CPU_HIGH", "MEMORY_HIGH", "DISK_LOW"]
alerts_b = ["DISK_LOW", "NETWORK_DOWN", "CPU_HIGH"]

combined = set(alerts_a) | set(alerts_b)
print(sorted(combined))

alerts_sources = {
    "prometheus": ["CPU_HIGH", "MEMORY_HIGH", "DISK_LOW"],
    "datadog": ["DISK_LOW", "NETWORK_DOWN", "CPU_HIGH"],
    "grafana": ["CPU_HIGH", "MEMORY_HIGH", "CPU_HIGH"]
}

unique_alerts = set()
for source, alerts in alerts_sources.items():
  print(f"{source} -> {alerts}")
  unique_alerts.update(alerts)

print("\nUnique alerts across systems:")
print(sorted(unique_alerts))

all_alerts = alerts_a + alerts_b
alert_counts = Counter(all_alerts)

for alert, count in alert_counts.items():
  print(f"{alert}: {count}")
