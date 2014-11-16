#!/usr/local/bin/python3

import sys
import threading
import time
import json
import string

import ar
import server


# Neat color function
red = "31"
yellow = "33"
green = "32"
def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"

# Print help information
def print_help():
    print("Autoremote python plugin by Storvik")
    print("Usage:\tautoremoteserver\t[optional arguments]")
    print("\t\t\t\t- help                                   \t- Write help information")
    print("\t\t\t\t- msg [device] [message]                 \t- Send a message to device")
    print("\t\t\t\t- notification [device] [title] [message]\t- Send a notification to device")
    print("\t\t\t\t- regdevice                              \t- Register new device(s)")
    print("\t\t\t\t- reset                                  \t- Delete config files(autoremote.json & autoremotedevices.txt")
    print("\t\t\t\t- resetdevice                            \t- Delete devices file(autoremotedevices.txt)\n")
    print("This is a python autoremote plugin. it is based on the autoremote c# program and autoremote android app by Joao Dias. \nThanks to:")
    print("\t- Joao Dias for some much needed help with development")
    print("")

# Print help information server view
def print_serverinfo():
    print(color(green,"Server is running."))
    print(color(yellow,"Supported commands:"))
    print(color(yellow,"\t\t- Send messages to devices \t- 'msg [device] [message]'"))
    print(color(yellow,"\t\t- Register new device      \t- 'registerdevice'"))
    print(color(yellow,"\t\t- List options             \t- 'help'"))
    print(color(yellow,"\t\t- Exit autoremote          \t- 'q / quit'"))
    print(color(yellow,"Registered devices:"))
    devlist = ar.load_device()
    for i in range(0, len(devlist)-1, 2):
        print(color(yellow,"\t\t- "+devlist[i]))


cnt = 1 # counter to get the right http post request

if __name__ == '__main__':
    host_name = "https://autoremotejoaomgcd.appspot.com/"
    option = ""

    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "help":
            print_help()
            exit(-1)
            
        elif option == "msg":
            # If message mode
            print("Message mode: Checking for configurations..")
            computer = ar.initcomputer()
            print("Found configurations. Sending message..")
            ar.message_send(sys.argv[1:])
            exit(-1)

        elif option == "reset":
            answr = input(color(yellow, "Are you sure you want to reset configurations? [y/n] "))
            if answr in ['y','yes','Y','YES']:
                subprocess.call(["rm","autoremote.json"])
                print(color(green,"autoremote.json is deleted. Server reconfiguration required upon restart.."))
                print(color(green,"autoremotedevices.txt is deleted. Device reconfiguration required upon restart.."))
            exit(-1)
            
        elif option == "resetdevice":
            answr = input(color(yellow, "Are you sure you want to reset devices? [y/n] "))
            if answr in ['y','yes','Y','YES']:
                subprocess.call(["rm","autoremotedevices.txt"])
                print(color(green,"autoremotedevices.txt is deleted. Device reconfiguration required upon restart.."))
            exit(-1)

        else:
            print(color(red,"Unknown input parameter.. 'autoremoteserver help' for options and usage!"))
            exit(-1)

    # Regdevice will be checked for further down. 
    # This because it depends on other key data

    print(color(green,"Autoremote python plugin!!"))

    # At startup check if config file exist. If not, create it
    computer = ar.initcomputer()

    # Register new devices
    ar.register_device(host_name)
    if option == "regdevice":
        ar.register_new_device(host_name)
    
    HOST_NAME = ''
    PORT_NUMBER = int(computer["port"])
    
    # Make a thread for the http server
    t = threading.Thread(target=server.http_server, args = (HOST_NAME,PORT_NUMBER))
    t.daemon = True
    t.start()
    # Wait for server to start
    time.sleep(3)

    while 1:
        print_serverinfo()
    
        indata = input("")
        indata = indata.split(' ')
        if indata[0] == "registerdevice":
            ar.register_newdevice(host_name)
        elif indata[0] == "msg":
            ar.message_send(indata)
        elif indata[0] in ["q","quit"]:
            print(time.asctime(), "Autoremote server stops - Port: %s" % (PORT_NUMBER))
            exit(-1)
