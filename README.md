pythonremote
============

Python port of Autoremote plugin by João Dias. 
This python script tries to utilize autoremote android app in every platform. 
The script is made to work with python 2.7.6 and tested on a MacBook Pro Yosemite. 

[AutoApps (joaoapps.com)](http://joaoapps.com/)

[AutoRemote for Android (Google PlayStore)](https://play.google.com/store/apps/details?id=com.joaomgcd.autoremote&hl=de)

Notification support for Mac OS X.
Notifications are displayed as system notifications and must contain title and text.
Optional fields: Icon and URL.

Requirements
============

This script requires the following installed:
- simplejson
- requests
- urllib
- BaseHTTPServer

Mac OSX:
- [terminal-notifier](https://github.com/alloy/terminal-notifier). Install via gem install. 


Usage
=====
$autoremoteserver [optional arguments]

Arguments:
- help          - Write help information
- regdevice     - Register new device(s)
- reset         - Delete config files(autoremote.json & autoremotedevices.txt NOT WORKING YET
- resetdevice   - Delete devices file(autoremotedevices.txt) NOT WORKING YET

Thanks to
=========

João Dia for some much needed help with development.


Project status
==============

What does it do:
- Asks user for needed data on initial run. This is saved in a json config file.
- If json config file exists => read file and check if ip adresses have to be updated.
- Asks user for a device if autoremotedevices.txt doesn't exist. 
- Starts the server.
- Prints autoremote requests to screen when received.
- Registers with notification support.
- Notifications must have title and text. URL and icon is optional.
- Supports registering of multiple devices.

What must be improved/fixed/added:
- If autoremote request doesn't contain message a nasty error is printed.
- Add sending message to device. 
- System for responding/reacting to a given message and adding/removing such actions.
- Implement google API url shortener when registering a new device.
