import os
import json

from .getip import get_lanip, get_pubip
from .register_device import register_updatedevice
from .load_computer import load_computer
from .color import color, green, red, yellow

# Function for creating server data 
def initcomputer(config_path):
    if os.path.isfile("autoremote.json"):
        print(color(green,"Autoremote config json file exists. Continuing server startup.."))
        
        computer = load_computer(config_path)
        
        lanip = get_lanip()
        pubip = get_pubip()
        change = "false"

        if computer["localip"] == lanip:
            print(color(green,"LAN IP is up to date.."))
        else:
            print(color(yellow,"LAN IP is being updpated"))
            computer["localip"] = lanip
            change = "true"

        if computer["publicip"] == pubip:
            print(color(green,"Public IP is up to date.."))
        else:
            print(color(yellow,"Public IP is being updated"))
            computer["publicip"] = pubip
            change = "true"

        # Write json to file
        if change == "true":
            try: 
                fd = open(config_path + 'autoremote.json', 'w+')
                fd.write(json.dumps(computer, default=jdefault, indent=4))
                fd.close()
            except:
                print(color(red,"ERROR writing autoremote.json..."))
                exit(-1)
            register_updatedevice()

    else:
        print(color(yellow,"Autoremote config json file doesnt exist."))
        answr = input(color(yellow, "Do you want to configure this device? [y/n] "))
        if answr in ['y','yes','Y','YES']:
            computer = json.loads('{"type":"plugin","port":"1820","haswifi":"True","ttl":"null","collapsekey":"null","additional":{"iconUrl":"http://icons.iconarchive.com/icons/osullivanluke/orb-os-x/512/OSX-icon.png","type":"PythonPlugin by Storvik","canreceivefiles":"True","canReceiveNotification":"True"},"communication_base_parameters":{"type":"RequestSendRegistration"}}')
            # Ask for needed parameters
            computer["id"] = input("Id: ")
            computer["name"] = input("Name: ")
            computer["localip"] = get_lan_ip()
            computer["publicip"] = get_pub_ip()
            computer["sender"] = input("Sender: ")
            computer["key"] = keygen(30)
        
            computer["communication_base_param"]["sender"] = computer["sender"]
                
            # Write json to file
            try: 
                fd = open(config_path + 'autoremote.json', 'w')
                fd.write(json.dumps(computer, default=jdefault, indent=4))
                fd.close()
            except:
                print(color(red,"ERROR writing autoremote.json..."))
                exit(-1)
                
    return computer
