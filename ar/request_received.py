import string

from .message_received import message_received
from .notification_received import notification_received
from .color import color, green, red, yellow

# Function for processing a request
def request_received(config_path, received):
    f = open(config_path + "autoremotedevices.txt","r")
    devlist = f.read().split("\n")

    #Check if known and respond
    if received["sender"] in devlist:
        print(color(yellow,"You just reveiced something from "+devlist[devlist.index(received["sender"])-1]+"!"))
        if received["communication_base_params"]["type"] == "Notification":
            notification_received(received)
        elif received["communication_base_params"]["type"] == "Message":
            message_received(config_path, received, devlist[devlist.index(received["sender"])-1])
    else:
        print(color(red,"You just received something from unknown device!!"))
        print(color(red,"Device key: "+received["sender"]))
                
    f.close()
    print(received)
