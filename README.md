pythonremote
============

Python port of Autoremote plugin by João Dias.
This python script tries to utilize autoremote android app in every platform.
The script is made to work with python 3.4 and tested on a MacBook Pro Yosemite.

[AutoApps (joaoapps.com)](http://joaoapps.com/)

[AutoRemote for Android (Google PlayStore)](https://play.google.com/store/apps/details?id=com.joaomgcd.autoremote&hl=de)

Requirements
------------

The following must be installed via pip3 install:
- requests
- urllib
- http.server

Mac OSX:
[terminal-notifier](https://github.com/alloy/terminal-notifier).
```sh
$ gem install terminal-notifier
```

Install
-------
Clone git repository.
```sh
$ git clone git@github.com:storsnik/pythonremote.git
```
Create symlink to somewhere in your path.
```sh
$ ln -s /path/to/pythonremote.py /path/to/PATH/pythonremote
```

Usage
-----
```sh
$ pythonremote [optional arguments]
```

|Arguments                                | Description                                                  |
|-----------------------------------------|--------------------------------------------------------------|
| help                                    | Write help information                                       |
| msg [recipient] [message]               | Send message to registered device                            |
| notification [recipient] [title] [text] | Send notification to registered device                       |
| regdevice                               | Register new device(s)                                       |
| reset                                   | Delete config files(autoremote.json & autoremotedevices.txt  |
| resetdevice                             | Delete devices file(autoremotedevices.txt)                   |

Pythonremote will divide incoming requests in **notifications** and **messages**.

### Messages
Messages containing `shellcommand [command]` will be excecuted on the pythonremote computer.
Response of the shell command well be returned to autoremote device as `shellresponse=:=[response]`.
Yet to come: a way to add own actions for specified messages.

### Notifications
Notification support only for Mac OS X, other systems coming soon.
Notifications are displayed as system notifications and must contain title and text.
Optional fields: Icon and URL, whereas the specified URL will be opened upon notification click.

Project status
--------------

What does it do:
- Asks user for needed data on initial run. This is saved in a json config file.
- If json config file exists => read file and check if ip adresses have to be updated.
- Asks user for a device if autoremotedevices.txt doesn't exist.
- Starts the server.
- Prints autoremote requests to screen when received.
- Registers with notification support.
- Notifications must have title and text. URL and icon is optional.
- Supports registering of multiple devices.
- Send message to registered devices.
- Send notifications to registered devices.

What must be improved/fixed/added:
- If autoremote request doesn't contain message a nasty error is printed.
- System for responding/reacting to a given message and adding/removing such actions.

Thanks to
=========

João Dia for some much needed help with development.
