#!/usr/bin/env python3
# Student Name: Edwin Chen
# Date: 10/02/2024

import os
import platform
import subprocess

def main():
    # Date & Time
    date_run = subprocess.run(['date'], capture_output=True, text=True)
    date = date_run.stdout.strip()

    # Log File
    log = "/home/student/Scripts/script02/script02_system_report.log"

    # Clears the terminal screen when starting the script
    os.system("clear")

    # Prints date & time
    print("\033[31m          System Report - " + date + "\033[0m")
    
    # Opens log file and writes
    with open(log, 'w') as file:

        # Log file write
        def writer(message):
            print(message)
            file.write(message + '\n')
        
        # Printing and writing Hostname and Domain
        linux_hostname = subprocess.run(['hostname'], capture_output=True, text=True)
        linux_parts = linux_hostname.stdout.strip().split('.')
        hostname = linux_parts[0]
        domain = '.'.join(linux_parts[1:])

        writer("\n\033[1;32mDevice Information\033[0m")
        writer("Hostname: " + hostname + " ")
        writer("Domain: " + domain + " ")
        
        # Printing and writing ip, gateway, netmask, dsn1, and 2
        ip_run = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
        ip = ip_run.stdout.strip()
        gate_run = subprocess.run(['bash','-c', "ip route | awk '/default/ {print $3}'"], capture_output=True, text=True)
        gateway = gate_run.stdout.strip() 
        netmask = ""
        netmask_run = subprocess.run(['ifconfig'], capture_output=True, text=True)
        for line in netmask_run.stdout.splitlines():
            if 'broadcast' in line:
                parts = line.split()
                netmask = parts[3]
        dns_run = subprocess.run(['cat','/etc/resolv.conf'],capture_output=True, text=True)
        servers = [i.split()[1] for i in dns_run.stdout.splitlines() if i.startswith('nameserver')]
        dns1 = servers[0]
        dns2 = servers[1]
        
        writer("\n\033[1;32mNetwork Information\033[0m")
        writer("IP address: " + ip)
        writer("Gateway: " + gateway)
        writer("Network Mask: " + netmask)
        writer("DNS1: " + dns1)
        writer("DNS2: " + dns2)
        
        # Printing and writing Operating System, Version, and Kernal
        oper_sys = platform.system()

        writer("\n\033[1;32mOS Information\33[0m")
        writer("Operating System: " + oper_sys)

        with open('/etc/os-release', 'r') as f:
            for lines in f:
                if lines.startswith('VERSION_ID='):
                    osv = lines.strip().split('=')[1].replace('"','')
                    writer("Operating Version: " + osv)

        kernal = platform.release()
        writer("Kernal Version: " + kernal)
       
        # Printing and writing Disk Storage and Avaliable Storage
        disk = subprocess.run(['df','-h','/'], capture_output=True, text=True)
        disk_lines = disk.stdout.splitlines()
        info = disk_lines[1].split()
        storage = info[1]
        avaliable = info[3]
        
        writer("\n\033[1;32mStorage Information\033[0m")
        writer("Hard Drive Capacity: " + storage)
        writer("Avaliable Space: " + avaliable)
        
        # Printing and writing CPU Model, # of Processors, and # of Cores
        cpu = subprocess.run(['lscpu'], capture_output=True, text=True)
        cpu_data = cpu.stdout
        for line in cpu_data.splitlines():
            if line.startswith('Model name:'):
                cpu = line.split(':')[1].strip()
        cpu_proc = subprocess.run(['nproc'],capture_output=True, text=True)
        cpu_proc = cpu_proc.stdout.strip()
        cpu_core = subprocess.run(['lscpu'], capture_output=True, text=True)
        core_data = cpu_core.stdout
        for line in core_data.splitlines():
            if line.startswith('Core(s) per socket:'):
                cpu_core = line.split(':')[1].strip()
        
        writer("\n\033[1;32mProcessor Information\033[0m")
        writer("CPU Model: " + cpu)
        writer("Number of processors: " + cpu_proc)
        writer("Number of cores: " + cpu_core)
        
        # Printing and writing Total Ram and Avaliable Ram
        ram_info = subprocess.run(['free','-h'], capture_output=True, text=True)
        line = ram_info.stdout.splitlines()
        memory = line[1].split()
        tot_ram = memory[1]
        aval_ram = memory[6]
        
        writer("\n\033[1;32mMemory Information\033[0m")
        writer("Total Ram: " + tot_ram)
        writer("Avaliable Ram: " + aval_ram)

if __name__ == "__main__":
    main()


