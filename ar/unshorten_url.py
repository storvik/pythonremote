import http.client
import urllib.parse

# Returns unshortened URL if succesfull 
def unshorten_url(url):
    parsed = urllib.parse.urlparse(url)
    h = http.client.HTTPConnection(parsed.netloc)
    resource = parsed.path
    if parsed.query != "":
        resource += "?" + parsed.query
    h.request('HEAD', resource )
    response = h.getresponse()
    if response.status == 301 and response.getheader('Location'):
        return unshorten_url(response.getheader('Location'))
    else:
        return url
