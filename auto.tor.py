import time
import os
import subprocess

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
print('[!] python3 requests is installed')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed!')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] Tor is installed!')

# Function to get the IP address using Tor's SOCKS5 proxy
def ma_ip():
    url = 'http://checkip.amazonaws.com'
    get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050'))
    return get_ip.text

# Function to change the Tor IP
def change():
    os.system("service tor reload")  # Corrected spelling from 'relaod' to 'reload'
    print('[+] Your IP has been changed to: ' + str(ma_ip()))
    print('''\033[1;32;40m 
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
by iamgeo1
''')
    os.system("service tor start")
    time.sleep(3)
    print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050 \n")
    os.system('service tor start')

try:
    # Get user input for time interval and number of changes
    x = input("[+] Time to change IP in seconds [default = 60] >> ") or "60"
    lin = input("[+] How many times do you want to change your IP? Enter to infinite IP change >> ") or "0"

    # Convert inputs to integers
    x = int(x)
    lin = int(lin)

    if lin == 0:
        print("Starting infinite IP change. Press Ctrl+C to stop.")
        while True:
            try:
                time.sleep(x)  # Pause for specified time interval
                change()
            except KeyboardInterrupt:
                print('\nAuto IP changer is closed.')
                break
    else:
        print(f"Starting IP change {lin} times. Press Ctrl+C to stop.")
        for _ in range(lin):
            time.sleep(x)
            change()

except ValueError:
    print("Invalid input. Please enter a valid number.")
