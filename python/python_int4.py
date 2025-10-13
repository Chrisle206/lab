data = {
    "cluster": "prod-west",
    "nodes": [
        {"name": "node01", "status": "up", "cpu": 55, "memory": 70},
        {"name": "node02", "status": "down", "cpu": 0, "memory": 0},
        {"name": "node03", "status": "up", "cpu": 65, "memory": 80},
        {"name": "node04", "status": "up", "cpu": 40, "memory": 50}
    ]
}


def anaylze_cluster(data):
  down_nodes = []
  total_cpu = 0
  up_count = 0

  for node in data["nodes"]:
    if node["status"] == "down":
      down_nodes.append(node["name"])
    elif node["status"] == "up":
      total_cpu += node["cpu"]
      up_count += 1
  avg_cpu = total_cpu / up_count if up_count > 0 else 0 
  
  print("Down nodes:", down_nodes)
  print(f"Average CPU (up nodes): {avg_cpu:.2f}%")

anaylze_cluster(data)
