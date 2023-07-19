# BDadmehr0-Garfox
#    _____ _  _ _____            
#   |_   _| \| |_   _|___ __  ___
#     | | | .` | | |(_-< '  \(_-<
#     |_| |_|\_| |_|/__/_|_|_/__/

import platform
import os
from time import sleep
from colorama import Fore as c
from termcolor import colored, cprint
from requests import get

from lib.Banner import *
from lib.sms import send
   

def sys_check():
    os_n = platform.system()
    if os_n == 'Linux':
        print(c.GREEN+'System-Guard: Check and accepted')
        sleep(3)
    else:
        print(c.RED+'System_Guard: Check and not accepted')
        sleep(3)
        exit()

def main():
    print(c.WHITE+' ['+c.RED+'1'+c.WHITE+']'+c.RED+' SMS')
    print(c.WHITE+' ['+c.RED+'2'+c.WHITE+']'+c.RED+' Call')
    print(c.WHITE+' ['+c.RED+'3'+c.WHITE+']'+c.RED+' Email')
    print(c.WHITE+' ['+c.RED+'00'+c.WHITE+']'+c.RED+' Exit'+c.RESET+'\n')

    username = platform.node()

    while True:
        menu_i = input(f'menu-{username} $ ')
        if menu_i == '1':
            phone_number = input('\nPhone-Number$: ')
            range_n = input('Send-Range$: ')
            send(phone_number)
        elif menu_i == '2':
            print('Call feature is currently unknown.')
        elif menu_i == '3':
            print('SMS & Call feature is currently unknown.')
        elif menu_i == '00':
            exit()


if __name__ == "__main__":
    banner()
    sys_check()
    main()