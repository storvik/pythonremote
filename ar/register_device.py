import os
import string
import requests
import urllib

from .gcm import Gcm_req
from .color import color, green, red, yellow
from .load_device import load_device
from .load_computer import load_computer
from .unshorten_url import unshorten_url

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
    key = input("Enter personal key or characters after goo.gl/: ")

    if len(key) > 5:
        key_raw = unshorten_url('https://goo.gl/' + key)
        if key_raw == key:
            print(color(red,"Could not unshorten URL. Try with regular key if problem continues.."))
            answr = input(color(yellow,"You want to try again? [y/n] "))
        else:
            key = key_raw.split("key=")[1]
            register_sendtodevice(config_path, key)
            fd.write(name+"\n"+key+"\n")
            print(color(green,"Successfully added "+name+" to device list.."))
            answr = input(color(yellow,"You want to add another device? [y/n] "))

    else:
        register_sendtodevice(config_path, key)
        fd.write(name+"\n"+key+"\n")
        print(color(green,"Successfully added "+name+" to device list.."))
        answr = input(color(yellow,"You want to add another device? [y/n] "))

    fd.close
    if answr in ['y','yes','Y','YES']:
        register_newdevice(config_path, host_name)

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
