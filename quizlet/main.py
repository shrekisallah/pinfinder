from colorama.ansi import Fore
import requests
import random
import string
import platform
from subprocess import call
from colorama import Fore

show_invalid = input('Show Invalids (y/n): ')

def cleartxt():
    open('valid.txt', 'w').close()

def clear():
    if platform.system() == 'Windows':
        call(['cls'], shell=True)
    elif platform.system() == 'Linux':
        call(['clear'], shell=True)
    elif platform.system() == 'Darwin':
        call(['clear'], shell=True)
    
def cleartxt():
    open('valid.txt', 'w').close()

cleartxt()

def main():
    clear()
    print(f'''
    ###################################
    #                                 #
    #       Quizlet Live Finder       #
    #                                 #
    ###################################
    ''')
    print(f'[{Fore.CYAN}-{Fore.RESET}] Finding Gaems\n')
    print(f'{Fore.RED} Ctrl + C to exit')
    while True:
        pin = ''.join((random.choice(string.digits) for i in range(6)))
        req = requests.get('https://quizlet.com/webapi/3.2/game-instances?filters={"gameCode":"{pin}","isInProgress":true,"isDeleted":false}&perPage=500')
        req.json()
        if req.status_code == 200:
            print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] gaem Found: {pin}')
            file = open('valid.txt', 'a')
            file.write(pin)
            file.write('\n')
            file.close
        if show_invalid == 'y':
            print (req.status_code)
            print(f'[{Fore.RED}-{Fore.RESET}] {pin}')
        else:
            pass
main()