# BDadmehr0 - Garfox

import platform
from time import sleep
import os

def install_update():
    os.system('sudo pip install -r requirements.txt')
    #try:
        # install requstes
    #    os.system('pip install requstes')
    #except:
        


def sys_check():
    os_n = platform.system()
    print(os_n)

def banner():
    asci = '''
 @@@@@@@ @@@  @@@ @@@@@@@       @@@@@@ @@@@@@@@@@   @@@@@@
   @@!   @@!@!@@@   @@!        !@@     @@! @@! @@! !@@
   @!!   @!@@!!@!   @!!         !@@!!  @!! !!@ @!@  !@@!!  | https://github.com/BDadmehr0
   !!:   !!:  !!!   !!:            !:! !!:     !!:     !:! | TNTsms Call & SMS Spamer (IR number)
    :    ::    :     :         ::.: :   :      :   ::.: :  | By Dadmehr with Coffee'''
    sleep(3)


def main():
    pass
if __name__ == "__main__":
    install_update()
    #menu()
    #main()
