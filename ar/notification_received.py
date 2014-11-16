import sys
import subprocess

from .color import color, green, red, yellow

def notification_received(received):
    print(color(yellow,"Notification received"))
    # Check OS
    if sys.platform.startswith('linux'):
        # Linux-specific code here...
        print("Linux support is comming soon..")
    elif sys.platform.startswith('win'):
        # Windows
        print("Windows not supperted..")
    elif sys.platform.startswith('darwin'):
        # Mac OS X
        notifi = ["terminal-notifier","-title",received["title"],"-subtitle","Pythonremote by Storvik","-message", received["text"],"-appIcon","https://lh5.ggpht.com/fQGeFGOUahclDOUsKU0d6F-Odg9D2jUB7xVnrH5KdeV1m8TcX_wdkbHTvKY2ZoIMgWj2=w300"]
        if "icon" in received:
            notifi.append("-contentImage")
            notifi.append(received["icon"].replace("\\",""))
            if "url" in received:
                notifi.append("-open")
                notifi.append(received["url"].replace("\\",""))

        subprocess.call(notifi)
    else:
        print(color(red,"OS not supported.."))
