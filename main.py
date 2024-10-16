import platform  # To get information about the system
import os  # To interact with the operating system
from time import sleep  # To introduce delays if necessary
from colorama import Fore as c  # To colorize terminal output
from termcolor import colored, cprint  # Another library for colored output
from requests import get  # To make HTTP requests

from lib.banner import *  # Importing banner function from a custom library
from lib.sms import send  # Importing send function for sending SMS


def sys_check():
    """
    Check the operating system type and return an appropriate message.
    
    Returns:
        str: A message indicating whether the system is accepted (Linux) or not.
    """
    os_name = platform.system()
    if os_name == 'Linux':
        return c.GREEN + 'System-Guard: Check and accepted'
    else:
        return c.RED + 'System_Guard: Check and not accepted'


def main():
    """
    Main function that displays the menu and handles user input for various features.
    """
    print(c.WHITE + ' [' + c.RED + '1' + c.WHITE + ']' + c.RED + ' SMS')
    print(c.WHITE + ' [' + c.RED + '2' + c.WHITE + ']' + c.RED + ' Call (coming soon)')
    print(c.WHITE + ' [' + c.RED + '3' + c.WHITE + ']' + c.RED + ' Email (coming soon)')
    print(c.WHITE + ' [' + c.RED + '00' + c.WHITE + ']' + c.RED + ' Exit' + c.RESET + '\n')

    username = platform.node()  # Get the username of the machine

    while True:
        # Prompt user for input
        menu_input = input(f'menu-{username} $ ')
        if menu_input == '1':
            # SMS option
            phone_number = input('\nPhone@Number ~$: ')
            range_n = int(input('Send@Range ~$: '))
            send(phone_number, r=range_n)  # Send SMS using the provided number and range
        elif menu_input == '2':
            # Call option (not implemented)
            print('Call feature is currently unavailable.')
        elif menu_input == '3':
            # Email option (not implemented)
            print('Email feature is currently unavailable.')
        elif menu_input == '00':
            # Exit the program
            exit()


if __name__ == "__main__":
    banner()  # Display the banner
    print(sys_check())  # Check the system and print the result
    main()  # Execute the main function
