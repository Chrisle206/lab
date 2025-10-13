servers = [
    {"name": "web01", "status": "up", "cpu": 45},
    {"name": "web02", "status": "down", "cpu": 0},
    {"name": "db01", "status": "up", "cpu": 67},
    {"name": "cache01", "status": "up", "cpu": 55},
]

def get_down_servers(servers):
    down_servers = [s["name"] for s in servers if s["status"] == "down"]
    return down_servers

def get_average_cpu(servers):
    up_servers = [s for s in servers if s["status"] == "up"]
    if not up_servers:   # handle division by zero if no up servers
        return 0
    avg_cpu = sum(s["cpu"] for s in up_servers) / len(up_servers)
    return avg_cpu

down = get_down_servers(servers)
avg = get_average_cpu(servers)

print(f"Down servers: {down}")
print(f"Average CPU: {avg:.2f}%")
