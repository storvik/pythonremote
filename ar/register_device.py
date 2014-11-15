import os
import requests
import urllib

from .gcm import Gcm_req

# Neat color function
red = "31"
yellow = "33"
green = "32"
def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"

# Register new device to autoremotedevices.txt
def register_device(host_name, dev, jsondata):
    # Checking for devices in autoremotedevices.txt
    # This file contains all registered devices (phone,tablet,etc)
    if os.path.isfile("autoremotedevices.txt"):
        print(color(green,"Found registered devices. Continuing server startup.."))
    else:
        print(color(yellow,"Did not find any devices."))
        answr = input(color(yellow,"You want to add a device? [y/n] "))
        if answr in ['y','yes','Y','YES']:
            register_newdevice(host_name,dev,jsondata)
                
        else:
            print(color(red,"autoremote is useless with no devices registered. Aborting..."))
            exit(-1)

# Register new device
def register_newdevice(host_name, dev, jsondata):
    fd = open("autoremotedevices.txt", "a+")                    # Opening device file
    # Todo: Check for existing name or key
    name = input("Enter name for new device: ")
    key = input("Enter personal key: ")
    
    gcm = Gcm_req(key, dev.sender, jsondata)                   # GCM register device message
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post("https://autoremotejoaomgcd.appspot.com/sendrequest", data=urllib.parse.urlencode(gcm.__dict__), headers=headers)
    
    fd.write(name+"\n"+key+"\n")                
    fd.close
    print(color(green,"Successfully added "+name+" to device list.."))
    answr = input(color(yellow,"You want to add another device? [y/n] "))
    if answr in ['y','yes','Y','YES']:
        register_newdevice(host_name,dev,jsondata)

def register_sendtodevice(key, sender, jsondata):
    gcm = Gcm_req(key, sender, jsondata)                   # GCM register device message
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post("https://autoremotejoaomgcd.appspot.com/sendrequest", data=urllib.parse.urlencode(gcm.__dict__), headers=headers)
    
    if r.text == "OK":                                         # If message is sent
        print(color(green,"Register device request successfully sent to device!"))
    else:
        print(color(red,"Couldn't send request. Aborting..."))
        exit(-1)
