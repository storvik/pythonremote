import re
import cgi
import json
import http.server

import ar

from pythonremote import cnt

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Pythonremote</title></head>")
        s.wfile.write("<p> This is index of python autoremote server made by Storvik. Nothing can be done here, go play some other place! </p>")
        s.wfile.write("</body></html>")
        pprint (vars(s))
    def do_POST(self):
        if None != re.search('/', self.path):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.get('content-length'))
                data = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)

                # For some reason a http post req results in four requests
                # Extract one of them
                global cnt
                if cnt == 4:
                    #print(data) # print raw data
                    regex = re.compile("\{b'([^;]+)\':")
                    data = regex.findall(str(data))
                    data = data[0].replace('""', '"Null"') # This to avoid those nasty unicode strings in empty fields
                    ar.request_received(json.loads(data))
                    cnt = 1
                else:
                    cnt = cnt + 1
                    
            else:
                data = {}
 
                self.send_response(200)
                self.end_headers()
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
