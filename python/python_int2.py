from collections import Counter
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3", "10.0.0.2"]

def find_duplicates(ips):
  seen = set()
  duplicates = set()

  for ip in ips:
    if ip in seen:
      duplicates.add(ip)
    else:
      seen.add(ip)
  return sorted(list(duplicates))

counts = Counter(ips)
dupes = {ip: count for ip, count in counts.items() if count > 1}
print(dupes)
print(find_duplicates(ips))
