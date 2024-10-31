#!/usr/bin/python3
# Student Name: Edwin Chen
# Date: 10/22/2024

from geoip import geolite2
import os
import subprocess

curr_date = subprocess.run(['date'], capture_output=True, text=True)
date = curr_date.stdout.strip()

def main():
    print("\033[0;32mAttacker Report\033[0m - " + date)
    print("\033[31COUNT  IP ADDRESS  COUNTRY\033[0m")

if __name__ == "__main__":
    os.system("clear")
    main()