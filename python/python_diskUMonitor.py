#!/usr/bin/env python3
import shutil
import time

THRESHOLD = 80  # percent
PATHS = ["/", "/var", "/home"]

def check_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    percent_used = used / total * 100
    return percent_used

while True:
    for path in PATHS:
        usage = check_disk_usage(path)
        status = "⚠️ ALERT" if usage > THRESHOLD else "✅ OK"
        print(f"{time.strftime('%H:%M:%S')} {path}: {usage:.1f}% used - {status}")
    time.sleep(300)
