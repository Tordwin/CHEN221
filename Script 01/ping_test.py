#!/usr/bin/env python3
# Student Name: Edwin Chen
# Date: 9/21/2024

import subprocess
import os

def get_default_gateway():
    p = subprocess.Popen(["ip r"], stdout=subprocess.PIPE, shell=True)
    out = p.stdout.read()
    print(out)

def test_local():
    return

def test_remote():
    return

def test_DNS():
    return

def main():
    os.system("clear")
    while True:
        print("Ping Test Menu")
        print("1. Display the default gateway")
        print("2. Test Local Connectivity")
        print("3. Test Remote Connectivity")
        print("4. Test DNS Resolution ")
        print("5. Exit/quit the script")

        option = input("Type the number of the option you would like to start: ")

        if option.isnumeric() == True:
            if option == "1":
                get_default_gateway()
            if option == "2":
                test_local()
            if option == "3":
                test_remote()
            if option == "4":
                test_DNS()
            if option == "5":
                print("Exiting")
                break
        else:
            print("\n'" + option + "' is not an option.\n")
            

    return


if __name__ == "__main__":
    main()