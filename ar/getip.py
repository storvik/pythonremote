import os
import requests
import socket

# Check for os
if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

# Get local ip
def get_lanip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

def get_pubip():
    ip = {}
    try: 
        r = requests.get("http://ip.42.pl/raw")
        ip = r.text
    except:
        print(color(red,"ERROR could not get public ip..."))
        exit(-1)
    return ip

if __name__ == '__main__':
    print("Todo: Make this happen")
