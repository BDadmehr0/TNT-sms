
from termcolor import colored, cprint

from colorama import Fore as c
from requests import get

def banner():
   versioan = get('https://raw.githubusercontent.com/BDadmehr0/TNT-sms/main/lib/V').text
   bomb = """
      ,--.!,  
   ,d08b.-*-   
   0088MM |    
   `9MMP'"""
   
   #   _____ _  _ _____            
   #  |_   _| \| |_   _|___ __  ___
   #    | | | .` | | |(_-< '  \(_-<
   #    |_| |_|\_| |_|/__/_|_|_/__/
                           

   print(c.RED+' _____'+c.WHITE+' _  _ '+c.RED+'_____ '+c.WHITE+'                ,--.'+c.YELLOW+'!,  ')
   print(c.RED+'|_   _'+c.WHITE+'| \| |'+c.RED+'_   _|'+c.WHITE+'___ __  ___ '+c.WHITE+' ,d08b.'+c.YELLOW+'-'+c.RED+'*'+c.YELLOW+'-   ')
   print(c.RED+"  | | "+c.WHITE+"| .` |"+c.RED+" | |"+c.WHITE+"(_-< '  \(_-< "+c.WHITE+" 0088MM "+c.YELLOW+"|"+c.WHITE+" | TNTsms Call & SMS Spamer IR")
   print(c.RED+'  |_| '+c.WHITE+'|_|\_|'+c.RED+' |_|'+c.WHITE+'/__/_|_|_/__/ '+c.WHITE+' `9MMP '+c.WHITE+'   | By BDadmehr0 & V {}\n'.format(versioan))
   # cprint('Bomb Shop Open', 'black', 'on_light_red', ['reverse', 'blink'])
