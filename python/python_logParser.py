#!/usr/bin/env python3
import re

logfile = "/var/log/syslog"  # or any app log
pattern = re.compile(r"ERROR|CRITICAL|Exception", re.IGNORECASE)

with open(logfile) as f:
    for line in f:
        if pattern.search(line):
            print(line.strip())
