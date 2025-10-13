logs = [
    "2025-10-07 08:01:12 INFO User login successful",
    "2025-10-07 08:01:13 ERROR Database connection failed",
    "2025-10-07 08:01:15 ERROR Timeout contacting API",
    "2025-10-07 08:01:16 INFO Health check passed",
    "2025-10-07 08:01:18 ERROR Disk full",
    "2025-10-07 08:01:19 WARNING High memory usage detected"
]

def alerts(logs):
  counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

  for line in logs:
    if "ERROR" in line:
      counts["ERROR"] += 1
    elif "WARNING" in line:
      counts["WARNING"] += 1
    elif "INFO" in line:
      counts["INFO"] += 1
    
  for level, count in counts.items():
    print(f"{level}: {count}")
  
  if counts["ERROR"] >= 3:
    print("ALERT: High error rate detected!")

alerts(logs)
