#!/usr/bin/env python3

import os
import sys
import threading
import time
import string
import argparse

import ar
import server

# Neat color function
red = "31"
yellow = "33"
green = "32"
def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"

# Print help information server view
def print_serverinfo():
    print(color(green,"Server is running."))
    print(color(yellow,"Supported commands:"))
    print(color(yellow,"\t\t- Send messages to devices \t- 'msg [device] [message]'"))
    print(color(yellow,"\t\t- Register new device      \t- 'registerdevice'"))
    print(color(yellow,"\t\t- List options             \t- 'help'"))
    print(color(yellow,"\t\t- Exit autoremote          \t- 'q / quit'"))
    print(color(yellow,"Registered devices:"))
    devlist = ar.load_device(config_path)
    for i in range(0, len(devlist)-1, 2):
        print(color(yellow,"\t\t- "+devlist[i]))

# Define variables
cnt = 1
config_path = os.path.realpath(__file__)[:-15]

if __name__ == '__main__':
    host_name = "https://autoremotejoaomgcd.appspot.com/"
    option = ""

    # ArgParser
    parser = argparse.ArgumentParser(
        description="Pythonremote, an autoremote implementation in python. If no command line arguments are specified the server will perform a normal startup.",
        epilog="Based on the autoremote C# program and autoremote android app by Joao Dias.",
        formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=45)) # Wider help text
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
    parser.add_argument('--message', nargs=2, metavar=('<device>','<message>'), help="send specified message to given device")
    parser.add_argument('--notification', nargs=3, metavar=('<device>', '<title>', '<message>'), help="send specified notification to given device (NOT WORKING YET)")
    parser.add_argument('--reset', help="resets pythonremote by deleting configuration files(keeps registered devices)", action="store_true")
    parser.add_argument('--resetdevice', help="resets registered devices by deleting device file", action="store_true")
    parser.add_argument('--regdevice', help="register new device and add it to device file", action="store_true")

    args = parser.parse_args()

    if len(sys.argv) > 1:
        if args.message:
            print("Message mode: Checking for configurations..")
            computer = ar.initcomputer(config_path)
            print("Found configurations. Sending message..")
            ar.message_send(config_path, sys.argv[1:])
            exit(-1)
        elif args.notification:
            print("Notification mode: Checking for configurations..")
            computer = ar.initcomputer(config_path)
            print("Found configurations. Sending message..")
            ar.notification_send(config_path, sys.argv[1:])
            exit(-1)
        elif args.reset:
            answr = input(color(yellow, "Are you sure you want to reset configurations? [y/n] "))
            if answr in ['y','yes','Y','YES']:
                os.remove(config_path + 'autoremote.json')
                print(color(green,"autoremote.json is deleted. Server reconfiguration required upon restart.."))
                print(color(green,"autoremotedevices.txt is deleted. Device reconfiguration required upon restart.."))
                exit(-1)
        elif args.resetdevice:
            answr = input(color(yellow, "Are you sure you want to reset devices? [y/n] "))
            if answr in ['y','yes','Y','YES']:
                os.remove(config_path + 'autoremotedevices.txt')
                print(color(green,"autoremotedevices.txt is deleted. Device reconfiguration required upon restart.."))
                exit(-1)
        elif args.regdevice:
            ar.register_device(config_path, host_name)
            ar.register_new_device(config_path, host_name)
        else:
            print(color(red,"Unknown input parameter.. 'pythonremote help' for options and usage!"))
            exit(-1)

    print(color(green,"Autoremote python plugin!!"))

    # At startup check if config file exist. If not, create it
    computer = ar.initcomputer(config_path)

    # Register new devices
    ar.register_device(config_path, host_name)

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
        indata = indata.split(" ")
        if indata[0] == "registerdevice":
            ar.register_newdevice(config_path, host_name)
        elif indata[0] == "msg":
            ar.message_send(config_path, indata)
        elif indata[0] in ["q","quit"]:
            print(time.asctime(), "Autoremote server stops - Port: %s" % (PORT_NUMBER))
            exit(-1)
