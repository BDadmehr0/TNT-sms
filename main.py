# Dadmher - Garfox

def install():
    try:
        #install form req.txt in lib dic
        os.system('pip install -r ./lib/requirements.txt')
        import platform
        from time import sleep
        import os
        from colorama import Fore, Style
    except:
        print(Fore.RED+'Installion Failed')


def sys_check(os_n):
    os_n = platform.system()
    if os_n == 'Linux':
        print(Fore.GREEN+'System-Guard: Cehck and accepted')
    else:
        print(Foe.RED+'System_Guard: Check and not accepted')

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

