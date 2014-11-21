import os
import requests
import urllib

from .gcm import Gcm_req
from .color import color, green, red, yellow
from .load_device import load_device
from .load_computer import load_computer

# Register new device to autoremotedevices.txt
def register_device(config_path, host_name):
    if os.path.isfile(config_path + 'autoremotedevices.txt'):
        print(color(green,"Found registered devices. Continuing server startup.."))
    else:
        print(color(yellow,"Did not find any devices."))
        answr = input(color(yellow,"You want to add a device? [y/n] "))
        if answr in ['y','yes','Y','YES']:
            register_newdevice(config_path, host_name)
                
        else:
            print(color(red,"autoremote is useless with no devices registered. Aborting..."))
            exit(-1)

# Register new device
def register_newdevice(config_path, host_name):
    fd = open(config_path + 'autoremotedevices.txt', 'a+')                    # Opening device file
    # Todo: Check for existing name or key
    name = input("Enter name for new device: ")
    key = input("Enter personal key: ")

    
    register_sendtodevice(key)
    
    fd.write(name+"\n"+key+"\n")                
    fd.close
    print(color(green,"Successfully added "+name+" to device list.."))
    answr = input(color(yellow,"You want to add another device? [y/n] "))
    if answr in ['y','yes','Y','YES']:
        register_newdevice(host_name)

# Register computer on device
def register_sendtodevice(config_path, key):
    computer = load_computer(config_path)
    
    gcm = Gcm_req(key, computer["sender"], computer)                   # GCM register device message
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post("https://autoremotejoaomgcd.appspot.com/sendrequest", data=urllib.parse.urlencode(gcm.__dict__), headers=headers)
    
    if r.text == "OK":                                         # If message is sent
        print(color(green,"Register device request successfully sent to device!"))
    else:
        print(color(red,"Couldn't send request. Aborting..."))
        exit(-1)

def register_updatedevice(config_path):
    if os.path.isfile('autoremotedevices.txt'):
        devlist = ar.load_device(config_path)
        for i in range(1, len(devlist)-1, 2):
            register_sendtodevice(devlist[i])
        print(color(green,"Updated information on devices.."))
    else:
        print(color(yellow,"No 'autoremotedevices.txt', nothing done.."))
