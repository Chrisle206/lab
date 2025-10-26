log = ["2025-10-22T19:15:43Z INFO  User login successful: user_id=1234", "2025-10-22T19:15:44Z ERROR Database connection failed", "2025-10-22T19:15:45Z WARN  Slow response: 1200ms"]


def reader(log):
  count = 0
  num_error = 0
  perc_error = 0
  for line in log:
    count += 1
    if "ERROR" in line:
      num_error += 1
  
  print(f"Total log lines: {count}")
  print(f"Error count: {num_error}")

  perc_error = num_error / count
  print(f"Error rate: {round(perc_error * 100, 2)}%")
  if perc_error > 0.05:
    print(f"Alert: Error rate exceeds 5%")

reader(log)