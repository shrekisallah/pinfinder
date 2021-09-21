from colorama.ansi import Fore
import requests
import random
import string
import platform
from subprocess import call

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
    #       Quizizz Code Finder       #
    #                                 #
    ###################################
    ''')
    print(f'[{Fore.CYAN}-{Fore.RESET}] Finding Codes')
    print(f'{Fore.RED}Ctrl + C to exit{Fore.RESET}')
    while True:
        pin = ''.join((random.choice(string.digits) for i in range(6)))
        r = requests.post('https://game.quizizz.com/play-api/v5/checkRoom', json={"roomCode":"{pin}"})
        dcode = r.json()
        if 'room' in dcode:
            print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {pin}')
            file = open('valid.txt', 'a')
            file.write(pin)
            file.write('\n')
            file.close
        else:
            if show_invalid == 'y':
                print(f'[{Fore.RED}-{Fore.RESET}] {pin}')

main()