from .device import Device, Additional, Comm_params

# Convert json to class device/additional/communicationbaseparameters
def json_objects(jsondata,dev,add,comm):
    dev = Device(jsondata["id"],jsondata["name"],jsondata["type"],jsondata["localip"],jsondata["publicip"],jsondata["port"],jsondata["haswifi"],jsondata["ttl"],jsondata["collapsekey"],jsondata["key"],jsondata["sender"],"","")
    add = Additional(jsondata["additional"]["iconUrl"],jsondata["additional"]["type"],jsondata["additional"]["canreceivefiles"],jsondata["additional"]["canReceiveNotifications"])
    comm = Comm_params(jsondata["communication_base_params"]["sender"],jsondata["communication_base_params"]["type"])
    dev.additional = add
    dev.communication_base_params = comm

    return dev, add, comm

# Function for making user defined json strings
def jdefault(o):
    return o.__dict__
