import http.server
import time

from .httpclass import MyHandler

def http_server(HOST_NAME, PORT_NUMBER):
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Autoremote server starts - Port: %s" % (PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
