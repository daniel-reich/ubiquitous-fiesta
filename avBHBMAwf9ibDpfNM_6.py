
import requests
​
def content_type(url):
    r = requests.get(url)
    return r.headers['Content-Type']

