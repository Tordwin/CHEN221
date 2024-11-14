#!/usr/bin/python3
# Student Name: Edwin Chen
# Date: 10/22/2024

from geoip import geolite2
import os
import subprocess
import re

curr_date = subprocess.run(['date'], capture_output=True, text=True)
date = curr_date.stdout.strip()

def get_data(path):
    #dictionary for attempted attacks
    attempts = {}
    #list to store attacks and count it
    counter = []
    #pattern to identify ip addresses
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    #file opener
    with open(path, 'r') as f:
        for line in f:
            if "Failed" in line:
                pair = ip_pattern.search(line)
                if pair:
                    ip = pair.group()
                    attempts[ip] = attempts.get(ip, 0) + 1
    for ip, num in attempts.items():
        if num >= 10:
            counter.append((ip, num))
    return counter

#looks up countries based on ip address
def country(ip_addr):
    #assigns lookup function to a variable
    locate = geolite2.lookup(ip_addr)
    #if locate is used and has a country, return the country
    if locate:
        return locate.country
    #if locate does not have a country, return none
    return "N/A"


def main():
    log_path = "/home/student/Scripts/Script 04/syslog.log"
    attacker_data = get_data(log_path)
    print("\033[0;32mAttacker Report\033[0m - " + date)
    print("")
    print("\33[31mCOUNT  IP ADDRESS  COUNTRY\033[0m")
    
    for ip, attempts in attacker_data:
        location = country(ip)
        print("{:<5} {:<15} {}".format(attempts, ip, location))

if __name__ == "__main__":
    os.system("clear")
    main()
