def load_device(config_path):
    f = open(config_path + 'autoremotedevices.txt','r')
    devlist = f.read().split("\n")
    f.close()

    return devlist
