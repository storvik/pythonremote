import json

# Function that returns computer information
def load_computer(config_path):
    fd = open(config_path + 'autoremote.json', 'r')
    content = fd.read()
    fd.close()

    return json.loads(content)
