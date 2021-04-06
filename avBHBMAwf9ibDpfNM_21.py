
import requests
​
def content_type(url):
  
  r = requests.get(url, auth=('user', 'pass'))
  Answer = r.headers['content-type']
  
  return Answer

