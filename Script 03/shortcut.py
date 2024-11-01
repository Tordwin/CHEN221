#!/usr/bin/python3
#Edwin Chen
#10/31/2024

import os
import subprocess
from pathlib import Path

def create_link():
    #Usr enters path for where to place symbolic link
    path = input("Enter the location where you would like to create a shortcut. ")
    
    #Finds the path by utilizing subprocess  using find command and captures output 
    file_path = subprocess.run(["find", "/", "-name", path], capture_output=True, text=True)
    final_path = file_path.stdout.strip()
    
    #Usr enters shortcut name for link
    shortcut = input("Enter the name of the shortcut. ")
    #Joining path
    link_path = Path.home().joinpath("Desktop", shortcut)

    try:
        print("\nCreating shortcut link...")
        os.symlink(final_path, link_path)
        print("Linked shortcut has been created!\n")
    except FileExistsError:
        print("This shortcut already exists.")
    except FileNotFoundError:
        print("The path does not exist.")
    except Exception as e:
        print("An error has occured " + e + ".")


def delete_link():
    #Usr enters shortcut name
    shortcut = input("Enter the name of the shortcut. ")
    #Creates a path with the shortcut name to find where it is located
    link_path = Path.home().joinpath("Desktop", shortcut)

    try:
        #Checks if it is a symbolic link
        if link_path.is_symlink():
            print("\nDeleting shortcut link...")
            #Deletes link and shortcut
            link_path.unlink()
            print("Linked shortcut deleted!\n")
        else:
            print("Filepath not found. ")
    except Exception as e:
        print("An error has occured " + e + ".")

def locate_link():
    #Joining path
    path = Path.home().joinpath("Desktop")
    #List for filepaths that are symbolic
    filepaths = []
    #Loop that checks for symbolic links and appends to filepaths list
    for i in path.iterdir():
        if i.is_symlink():
            filepaths.append(i)
    
    #Prints symbolic links, locations, and how many links there is
    if filepaths:
        print("\nSymbolic links:\n")
        for files in filepaths:
            print(files.name + " -> " + str(files.resolve()) + "\n")
        print("There is/are " + str(len(filepaths)) + " symbolic links.\n")
    else:
        print("\nNo symbolic links found.\n")


def main():
    while (True):
        print("Welcome to Shortcut Creator")
        print("Select an option below!")
        print("1. Create a shortcut.")
        print("2. Delete a shortcut.")
        print("3. Find a shortcut.")
        print("Type 'quit' to exit this program.")
        
        usr_input = input("\nWhich option do you choose? ")
        if usr_input == "1":
            create_link()
        elif usr_input == "2":
            delete_link()
        elif usr_input == "3":
            locate_link()
        elif usr_input == "quit":
            os.system("clear")
            print("Quitting...")
            break
        else:
            print("\nPlease input a valid choice between 1 and 3. ")


if __name__ == "__main__":
    os.system("clear")
    main()
