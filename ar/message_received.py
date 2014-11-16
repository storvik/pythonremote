import subprocess

from .message_send import message_send
from .load_computer import load_computer
from .color import color, green, red, yellow

# If massage, check for saved response
def message_received(received, ardevice):
    print(color(yellow,"Received message. Checking for saved response."))
    message = received['message']
    
    computer = load_computer()
    
    option = message.split(" ")
    if option[0] == "shellcommand":
        cmd = option[1:]
        response = "msg "+ardevice+" pythonremoteshellresp=:="+(subprocess.check_output(cmd, universal_newlines=True))
        message_send(response)
        print(response)
    ####
    # Todo add rules for message received
    ####
    #fd = open("commands.txt", 'r+')
    #commands = fd.read().split("\n")
    #Some code
    #fd.seek(0)
    #fd.write(text)
    #fd.truncate()
    #fd.close()
