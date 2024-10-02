#!/usr/bin/env python3
# Student Name: Edwin Chen
# Date: 10/02/2024

import os
import platform
import subprocess

def main():
    output = subprocess.run(['date'], capture_output=True, text=True)
    date = output.stdout.strip()

    print("\033[31m          System Report - " + date + "\033[0m")

    print("\n\033[1;32mDevice Information\033[0m")
    print("Hostname: ")
    print("Domain: ")

    print("\n\033[1;32mNetwork Information\033[0m")
    print("IP address: ")
    print("Gateway: ")
    print("Network Mask: ")
    print("DNS1: ")
    print("DNS2: ")

    print("\n\033[1;32mOS Information\033[0m")
    print("Operating System: ")
    print("Operating Version: ")
    print("Kernal Version: ")

    print("\n\033[1;32mStorage Information\033[0m")
    print("Hard Drive Capacity: ")
    print("Avaliable Space: ")

    print("\n\033[1;32mProcessor Information\033[0m")
    print("CPU Model: ")
    print("Number of processors: ")
    print("Number of cores: ")

    print("\n\033[1;32mMemory Information\033[0m")
    print("Total Ram: ")
    print("Avaliable Ram: ")
          

    return


if __name__ == "__main__":
    main()


