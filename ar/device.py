# Class for additional info
class Additional:
    def __init__(self, iconUrl, type, canreceivefiles, canReceiveNotifications):
        self.iconUrl = iconUrl
        self.type = type
        self.canreceivefiles = canreceivefiles
        self.canReceiveNotifications = canReceiveNotifications

# Class for communication parameters
class Comm_params:
    def __init__(self, sender, type):
        self.sender = sender
        self.type = type

# Class for device information
class Device:
    def __init__(self, id, name, type, localip, publicip, port, haswifi, ttl, collapsekey, key, sender, additional, communication_base_params):
        self.id = id
        self.name = name
        self.type = type
        self.localip = localip
        self.publicip = publicip
        self.port = port
        self.haswifi = haswifi
        self.ttl = ttl
        self.collapsekey = collapsekey
        self.key = key
        self.sender = sender
        self.additional = additional
        self.communication_base_params = communication_base_params
