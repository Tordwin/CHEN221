#!/usr/bin/env python3
# Student Name: Edwin Chen
# Date: 10/02/2024

import os
import platform
import subprocess

def run_command(com):
    run = subprocess.run(com, capture_output=True, text=True)
    return run.stdout.strip()

def main():
    # Date & Time
    date = run_command('date')

    # Log File
    log = "/home/student/Scripts/script02_system_report.log"

    # Clears the terminal screen when starting the script
    os.system("clear")

    # Prints date & time
    print("\033[31m          System Report - " + date + "\033[0m")

    with open(log, 'w') as file:
        
        def writer(message):
            print(message)
            file.write(message)

        linux_hostname = subprocess.check_output("hostname -f", shell=True).decode().strip()
        hostname = linux_hostname.split('.')[0]
        domain = '.'.join(linux_hostname.split('.')[1:])
        writer("\n\033[1;32mDevice Information\033[0m")
        writer("Hostname: " + hostname)
        writer("Domain: " + domain)
        
        ip = ""
        gateway = ""
        netmask = ""
        dns1 = ""
        dns2 = ""
        writer("\n\033[1;32mNetwork Information\033[0m")
        writer("IP address: ")
        writer("Gateway: ")
        writer("Network Mask: ")
        writer("DNS1: ")
        writer("DNS2: ")

        oper_sys = ""
        osv = ""
        kernal = ""
        writer("\n\033[1;32mOS Information\033[0m")
        writer("Operating System: ")
        writer("Operating Version: ")
        writer("Kernal Version: ")
        
        storage = ""
        aval_space = ""
        writer("\n\033[1;32mStorage Information\033[0m")
        writer("Hard Drive Capacity: ")
        writer("Avaliable Space: ")

        cpu = ""
        cpu_proc = ""
        cpu_core = ""
        writer("\n\033[1;32mProcessor Information\033[0m")
        writer("CPU Model: ")
        writer("Number of processors: ")
        writer("Number of cores: ")
        
        tot_ram = ""
        aval_ram = ""
        writer("\n\033[1;32mMemory Information\033[0m")
        writer("Total Ram: ")
        writer("Avaliable Ram: ")

if __name__ == "__main__":
    main()


