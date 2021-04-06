
from requests import get
​
def content_type(url):
  return get(url).headers['content-type']

