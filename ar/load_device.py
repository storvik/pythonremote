def load_device():
    f = open("autoremotedevices.txt","r")
    devlist = f.read().split("\n")
    f.close()
    return devlist
