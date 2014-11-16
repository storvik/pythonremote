import json

# Function that returns computer information
def load_computer():
    fd = open("autoremote.json", 'r')
    content = fd.read()
    fd.close()

    return json.loads(content)
