# Dadmher - Garfox

try:
    import platform
    import os
    from time import sleep
    from colorama import Fore as c
except:
    print('Missing Library')

def install():
    try:
        #install form req.txt in lib dic
        os.system('pip install -r ./lib/requirements.txt')
    except:
        print(c.RED+'Installion Failed')


def sys_check():
    os_n = platform.system()
    if os_n == 'Linux':
        print(c.GREEN+'System-Guard: Cehck and accepted')
        sleep(3)
    else:
        print(c.RED+'System_Guard: Check and not accepted')
        sleep(3)
        exit()

def banner():

    print(c.RED+'@@@@@@'+c.WHITE+' @@@  @@'+c.RED+' @@@@@@'+c.WHITE+'  @@@@@@ @@@@@@@@@@   @@@@@@')
    print(c.RED+'  @@! '+c.WHITE+' @@!@!@@'+c.RED+'   @@! '+c.WHITE+' !@@     @@! @@! @@! !@@')
    print(c.RED+'  @!! '+c.WHITE+' @!@@!!@'+c.RED+'   @!! '+c.WHITE+'  !@@!!  @!! !!@ @!@  !@@!!  | https://github.com/BDadmehr0')
    print(c.RED+'  !!: '+c.WHITE+' !!:  !!'+c.RED+'   !!: '+c.WHITE+'     !:! !!:     !!:     !:! | TNTsms Call, SMS Spamer IR')
    print(c.RED+'   :  '+c.WHITE+' ::    : '+c.RED+'    :  '+c.WHITE+' ::.: :   :      :   ::.: :  | By BDadmehr0')

    sleep(2)

def main_menu():
    pass

def menu():
    print(c.WHITE+' ['+c.RED+'1'+c.WHITE+']'+c.RED+' Start')
    print(c.WHITE+' ['+c.RED+'2'+c.WHITE+']'+c.RED+' About')
    print(c.WHITE+' ['+c.RED+'U'+c.WHITE+']'+c.RED+' Update')
    print(c.WHITE+' ['+c.RED+'00'+c.WHITE+']'+c.RED+' Exit')


def main():
    menu()
    while True:
        menu_i = input('menu-$ ')
        if menu_i == '1':
            main_menu()
        elif menu_i == '2':
            about()
        elif menu_i == 'U' or menu_i == 'u':
            os.system("cd && rm -rf TNT-sms && git clone https://github.com/BDadmehr0/TNT-sms && cd TNT-sms && python3 main.py")
        elif menu_i == '00':
            exit()


if __name__ == "__main__":
    os.system('clear')
    banner()

    install()
    sys_check()
    os.system('clear')

    banner()
    main()
