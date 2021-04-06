
import requests
​
def content_type(url):
  return requests.get(url).headers["content-type"]

