import string
import urllib
import requests

from .notification import Notification
from .load_device import load_device
from .load_computer import load_computer
from .color import color, green, red, yellow

def notification_send(config_path, indata):
    print("Trying to send notification..")

    computer = load_computer(config_path)
    devlist = load_device(config_path)
    if indata[1] in devlist:
        key = devlist[devlist.index(indata[1]) + 1]

        title = indata[2]
        ntfy_text = " ".join(indata[3:])
        ntfy = Notification(key, computer["id"], title, ntfy_text)                   # GCM register device message
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post('https://autoremotejoaomgcd.appspot.com/sendnotification', data=urllib.parse.urlencode(ntfy.__dict__), headers=headers)

        if r.text == "OK":                                         # If message is sent
            print(color(green,"Notification successfully sent to device!"))
        else:
            print(color(red,"Couldn't send notification. Aborting..."))
            exit(-1)
