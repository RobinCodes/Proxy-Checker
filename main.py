#cool script to download and test proxies

import requests
import os
import ctypes
import colorama # just makes UI look better
import time

def main():
    os.system('cls')
    print(colorama.Fore.LIGHTGREEN_EX + r'''
  ____                         ____ _               _             
 |  _ \ _ __ _____  ___   _   / ___| |__   ___  ___| | _____ _ __ 
 | |_) | '__/ _ \ \/ / | | | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 |  __/| | | (_) >  <| |_| | | |___| | | |  __/ (__|   <  __/ |   
 |_|   |_|  \___/_/\_\\__, |  \____|_| |_|\___|\___|_|\_\___|_|   
                      |___/                                       
''')

    print('''\n1> Scrape Proxies\n2> Check Proxies\n3> Help ''')

    question = input("\n" + os.getlogin( ) + "@root: ")

    if question == '1':
        scrape_proxies()

    else:
        if question == '2':
            check_proxies()

        else:
            if question == '3':
                help()

            else:
                main()

# fetch proxys from these URL's
def scrape_proxies():

    file = input("\nWould you like to save these proxies to a file (Y/N) ?: ")

    proxies = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt',' https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all','https://www.proxy-list.download/api/v1/get?type=http', 'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/https.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt']

    for proxy in proxies:
        response = requests.get(proxy)
            
        if response.status_code == 200:
            if file == 'Y':
                with open("proxies.txt", 'w') as file:
                    found_proxies = response.text
                    file.write(found_proxies)
                    input("\nPress any button to exit....")
                    main()
            else:
                if file == 'N':
                    print(response.text)

                    input("Press any button to exit....")
                    main()

                else:
                    scrape_proxies()
        else:
            print(f"Failed: {proxy}, Error: {response.status_code}")

def check_proxies():
    print("\nMake sure that you have saved the proxies you want to check into 'proxies.txt'\n")
    time.sleep(3) # so you can read text above
    #read proxies form 'proxies.txt'
    f = open("proxies.txt", "a") # makes sure file exists and makes it if it doesnt (for some reasons without this it says the file does not exist)

    with open("proxies.txt", 'r') as file:
        proxies = [line.strip() for line in file.readlines()]

    url = 'https://api.ipify.org/'  # Send a request to ipify API

    for proxy in proxies:
        proxy_directory = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }

        try:
            response = requests.get(url, proxies=proxy_directory, timeout=10) # use proxies to make requests
            results = input("Would you like to save the results to a file (Y/N) ?: ")

            if results == 'Y':
                with open("working_proxies.txt", 'w') as file:
                    working_proxies = response.text
                    file.write(working_proxies)
                    input("\nPress any button to exit....")
                    main()
            else:
                if results == 'N':
                    output = print(f"Proxy {proxy} works!")
                    input("\nPress any button to exit....")
                    main()

                else:
                    check_proxies()
        except requests.RequestException as e:
            print(f"Proxy {proxy} failed")

    input("\nPress any button to exit....")
    main()

def help():
    print("\nThe only problem you may face is that not all of the proxies may download, this is because you are most likely being rate limited. To bypass this just changed your IP (use a VPN, etc).\nAny other errors just join the discord: https://discord.com/invite/6pSR2Rcqeg")
    input("\nPress any button to exit....")
    main()

if __name__ == '__main__':
    title = "Proxy Checker | Made By: Robin"
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    main()