#!/usr/bin/python

import subprocess

power_mode = subprocess.run(["cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"], capture_output=True, encoding="utf8")

print(power_mode.stdout)

if power_mode.stdout.strip() != "performance":
    subprocess.run(["echo", "performance", "|", "sudo", "tee", "/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"])
