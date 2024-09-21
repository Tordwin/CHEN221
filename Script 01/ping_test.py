#!/usr/bin/env python3
# Student Name: Edwin Chen
# Date: 9/21/2024

import os

# default gateway function
def get_default_gateway():
    print()
    # Writes in terminal the command and runs it
    os.system("ip r | grep default | awk '{print $3}'")

# Pings local server
def test_local():
    print()
    try:
        # Writes in terminal the command
        os.system('ping -c 4 127.0.0.1')
    except Exception as e:
        print("An error has occured: " + str(e))
    print()

# Pings RIT's DNS server
def test_remote():
    print()
    try:
        # Writes in terminal the command and runs it
        os.system('ping -c 4 129.21.3.17')
    except Exception as e:
        print("An error has occured: " + str(e))
    print()

def test_DNS():
    print()
    try:
        # Writes in terminal the command and runs it
        os.system('ping -c 4 google.com')
    except Exception as e:
        print("An error has occured: " + str(e))
    print()

def main():
    # Clears the terminal
    os.system("clear")
    # While loop keeps the user options displayed after
    # it is run or until option 5 is selected.
    while True:
        # User Options
        print("Ping Test Menu")
        print("1. Display the default gateway")
        print("2. Test Local Connectivity")
        print("3. Test Remote Connectivity")
        print("4. Test DNS Resolution ")
        print("5. Exit/quit the script")
        # Prompts the user with the question and grabs it as an input
        option = input("Type the number of the option you would like to start: ")
        # Checks if it is a number and only allows 1-5
        if option.isnumeric() == True and 0 < int(option) < 6:
            if option == "1":
                get_default_gateway()
                print()
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

if __name__ == "__main__":
    main()
