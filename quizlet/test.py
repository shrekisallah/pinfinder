from colorama.ansi import Fore
import requests
import random
import string

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://quizlet.com/webapi/3.2/game-instances?filters={"gameCode":"{pin}","isInProgress":true,"isDeleted":false}&perPage=500'

def main():
    while True:
        pin = ''.join((random.choice(string.digits) for i in range(6)))
        r = requests.get(url, headers=headers)
        dcode = r.json()
        if 'id' in dcode:
            print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {pin}')
        else:
            print(f'[{Fore.RED}-{Fore.RESET}] {pin}')

main()