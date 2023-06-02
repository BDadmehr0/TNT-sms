import platform
from time import sleep
import os
from lib import color

C = color.c_s()

def install_update():
    try:
        #install requstes
        os.system('pip install requstes')
    except:
        print(C.RED+'Installion Failed')
        


    os_n = platform.system()
    print(C.RED+""+os_n)

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
    ###os.system('clear')
    #menu()
    #main()

