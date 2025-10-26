#!/usr/bin/env python3
import subprocess
import platform
import time

# List of critical hosts or services
hosts = ["8.8.8.8", "1.1.1.1", "google.com", "ibm.com"]

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

while True:
    for host in hosts:
        status = "✅ UP" if ping(host) else "❌ DOWN"
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {host} is {status}")
    time.sleep(60)
