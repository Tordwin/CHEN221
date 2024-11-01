#!/usr/bin/python3
#Edwin Chen
#10/31/2024

import os
import subprocess
from pathlib import Path

def create_link():
    path = input("Enter the location where you would like to create a shortcut. ")

    file_path = subprocess.run(["find", "/", "-name", path], capture_output=True, text=True)
    final_path = file_path.stdout.strip()
    
    shortcut = input("Enter the name of the shortcut. ")
    link_path = Path.home() / "Desktop" / shortcut

    try:
        os.symlink(final_path, link_path)
    except FileExistsError:
        print("This shortcut already exists.")
    except FileNotFoundError:
        print("The path does not exist.")
    except Exception as e:
        print("An error has occured " + e + ".")


def delete_link():
    shortcut = input("Enter the name of the shortcut. ")
    link_path = Path.home() / "Desktop" / shortcut

    try:
        if link_path.is_symlink():
            link_path.unlink()
            print("Path has been unlinked.")
        else:
            print("Filepath not found. ")
    except Exception as e:
        print("An error has occured " + e + ".")

def locate_link():
    return


def main():
    while (True):
        print("Welcome to Shortcut Creator")
        print("Select an option below!")
        print("1. Create a shortcut.")
        print("2. Delete a shortcut.")
        print("3. Find a shortcut.")
        print("Type 'quit' to exit this program.")
        
        usr_input = input("Which option do you choose? ")
        if usr_input == "1":
            create_link()
        elif usr_input == "2":
            delete_link()
        elif usr_input == "3":
            locate_link()
        elif usr_input == "quit":
            print("Quitting...")
            break
        else:
            print("Please input a valid choice between 1 and 3. ")


if __name__ == "__main__":
    os.system("clear")
    main()
