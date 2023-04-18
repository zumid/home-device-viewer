#!/usr/bin/env python3

import subprocess
import json
import time

def load_settings():
    with open('settings.json') as f:
        jsn = json.load(f)
    return jsn

def get_arp():    
    result = subprocess.run(['arp'], capture_output=True, text=True).stdout

    return result

def ping():
    for num in range(101,201):
        ip = "192.168.10."+str(num)
        subprocess.Popen(['ping','-c','1','-w','1',ip], stdout=subprocess.DEVNULL)
    time.sleep(1)
    

def main():
    settings = load_settings()
    ping()
    arp_data = get_arp()
    
    for device in settings["devices"]:
        if device['mac'].lower() in arp_data:
            print(f'{device["name"]} 接続中')
        else:
            print(f'{device["name"]} 接続なし')
    
    print(arp_data)

if __name__ == '__main__':
    main()




