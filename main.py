# Dadmher - Garfox

try:
    import platform
    import os
    from time import sleep
    from colorama import Fore
    from lib import configs
except:
    print('Missing Library')

def install():
    try:
        #install form req.txt in lib dic
        os.system('pip install -r ./lib/requirements.txt')
    except:
        print(Fore.RED+'Installion Failed')


def sys_check():
    os_n = platform.system()
    if os_n == 'Linux':
        print(Fore.GREEN+'System-Guard: Cehck and accepted')
    else:
        print(Foe.RED+'System_Guard: Check and not accepted')
        exit()

def banner():
    asci = '''
 @@@@@@@ @@@  @@@ @@@@@@@       @@@@@@ @@@@@@@@@@   @@@@@@
   @@!   @@!@!@@@   @@!        !@@     @@! @@! @@! !@@
   @!!   @!@@!!@!   @!!         !@@!!  @!! !!@ @!@  !@@!!  | https://github.com/BDadmehr0
   !!:   !!:  !!!   !!:            !:! !!:     !!:     !:! | TNTsms Call & SMS Spamer (IR number)
    :    ::    :     :         ::.: :   :      :   ::.: :  | By Dadmehr with Coffee'''
    sleep(3)


def main():
    banner = configs.banner()

if __name__ == "__main__":
    install()
    os.system('clear')
    sys_check()
    main()
