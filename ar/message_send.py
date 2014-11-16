import string
import urllib
import requests

from .message import Message
from .load_device import load_device
from .load_computer import load_computer
from .color import color, green, red, yellow

def message_send(indata):
    print("Trying to send message..")

    computer = load_computer()
    indata = indata.split(" ")
    devlist = load_device()
    if indata[1] in devlist:
        key = devlist[devlist.index(indata[1])+1]

        msg_text = " ".join(indata[2:])
        msg = Message(key, computer["id"], msg_text)                   # GCM register device message
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post("https://autoremotejoaomgcd.appspot.com/sendmessage", data=urllib.parse.urlencode(msg.__dict__), headers=headers)
    
        if r.text == "OK":                                         # If message is sent
            print(color(green,"Message successfully sent to device!"))
        else:
            print(color(red,"Couldn't send message. Aborting..."))
            exit(-1)
