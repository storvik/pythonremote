import os
import json

from .json_objects import json_objects, jdefault
from .getip import get_lanip, get_pubip
from .color import color, green, red, yellow

# Function for creating server data 
def initcomputer(dev, add, comm):
    if os.path.isfile("autoremote.json"):
        print(color(green,"Autoremote config json file exists. Continuing server startup.."))
        jsondata = {}
        
        fd = open("autoremote.json", 'r')
        content = fd.read()
        fd.close()

        jsondata = json.loads(content)
        dev, add, comm = json_objects(jsondata,dev,add,comm)

        lanip = get_lanip()
        pubip = get_pubip()
        change = "false"

        if dev.localip == lanip:
            print(color(green,"LAN IP is up to date.."))
        else:
            print(color(yellow,"LAN IP is being updpated"))
            dev.localip = lanip
            change = "true"

        if dev.publicip == pubip:
            print(color(green,"Public IP is up to date.."))
        else:
            print(color(yellow,"Public IP is being updated"))
            dev.publicip = pubip
            change = "true"

        # Write json to file
        if change == "true":
            try: 
                fd = open('autoremote.json', 'w+')
                fd.write(json.dumps(dev, default=jdefault, indent=4))
                fd.close()
            except:
                print(color(red,"ERROR writing autoremote.json..."))
                exit(-1)
            #register_device("https://autoremotejoaomgcd.appspot.com/", dev, jsondata)

    else:
        print(color(yellow,"Autoremote config json file doesnt exist."))
        answr = input(color(yellow, "Do you want to configure this device? [y/n] "))
        if answr in ['y','yes','Y','YES']:

            # Ask for needed parameters
            dev.id = input("Id: ")
            dev.name = input("Name: ")
            dev.type = "plugin"
            dev.localip = get_lan_ip()
            dev.publicip = get_pub_ip()
            dev.port = "1820"
            dev.haswifi = "True"
            dev.ttl = input("TTL: ")
            dev.collapsekey = input("Collapsekey: ")
            dev.sender = input("Sender: ")
            dev.key = keygen(30)
        
            add.iconUrl = input("Icon URL: ")
            add.type = "PythonPlugin by Storvik"
            add.canreceivefiles = "True"
            add.canReceiveNotifications = "True"
        
            comm.sender = dev.sender
            comm.type = "RequestSendRegistration"
    
            dev.additional = add    
            dev.communication_base_params = comm
            
            # Convert objects/classes to json format
            jsondata = (json.dumps(dev, default=jdefault, indent=4))

            # Write json to file
            try: 
                fd = open("autoremote.json", "w")
                fd.write(jsondata)
                fd.close()
            except:
                print(color(red,"ERROR writing autoremote.json..."))
                exit(-1)
                
    return jsondata, dev, add, comm
