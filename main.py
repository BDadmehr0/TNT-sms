# Dadmher - Garfox

try:

    import platform
    import os

    from time import sleep
    from colorama import Fore as c
    from lib import Banner
    from lib import sms
except ImportError:
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


def sms_menu():
    print(c.WHITE+' ['+c.RED+'1'+c.WHITE+']'+c.RED+' SMS')
    print(c.WHITE+' ['+c.RED+'2'+c.WHITE+']'+c.RED+' Call')
    print(c.WHITE+' ['+c.RED+'3'+c.WHITE+']'+c.RED+' SMS & Call')
    print(c.WHITE+' ['+c.RED+'00'+c.WHITE+']'+c.RED+' Exit'+c.RESET+'\n')

    while True:
        menu_i = input('menu-$ ')
        if menu_i == '1':
            phone_number = input('Phone-Number$: ')
            range_n = input('Send-Reange$: ')

            sms.send(phone_number,range_n)
        elif menu_i == '2':
            print('Unknown')
        elif menu_i == '3':
            print('Unknown')
        elif menu_i == '00':
            exit()

def menu():
    print(c.WHITE+' ['+c.RED+'1'+c.WHITE+']'+c.RED+' Start')
    print(c.WHITE+' ['+c.RED+'2'+c.WHITE+']'+c.RED+' About')
    print(c.WHITE+' ['+c.RED+'U'+c.WHITE+']'+c.RED+' Update')
    print(c.WHITE+' ['+c.RED+'00'+c.WHITE+']'+c.RED+' Exit'+c.RESET+'\n')


def main():
    menu()
    about = 'TNT-sms is a program for Linux that will be transferred to Telegram bot and Termox in the future We want to extract many APIs from Iranian sites and use them to send SMS. Also, the important part of this issue is that the sites do not limit us, for which I have made other plans, such as changing the IP address or user agents.'
    while True:
        menu_i = input('menu-$ ')
        if menu_i == '1':
            os.system('clear')
            banner = Banner.banner()
            sms_menu()
        elif menu_i == '2':
            print(about)
        elif menu_i == 'U' or menu_i == 'u':
            # +_+_+_+ Update +_+_+_+
            pass
        elif menu_i == '00':
            exit()


if __name__ == "__main__":
    os.system('clear')
    banner = Banner.banner()

    install()
    sys_check()
    os.system('clear')

    banner = Banner.banner()
    main()
