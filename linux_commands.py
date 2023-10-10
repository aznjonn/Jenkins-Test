#!/usr/bin/env python3

import subprocess

# Function to run a command and capture its output
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result.stdout

# Run the first command: Display system information
print("System Information:")
print(run_command("uname -a"))
print("----------------------------------")

# Run the second command: List files in the home directory
print("Files in the Home Directory:")
print(run_command("ls -l ~"))
print("----------------------------------")

# Run the third command: Display system uptime
print("System Uptime:")
print(run_command("uptime"))
print("----------------------------------")

