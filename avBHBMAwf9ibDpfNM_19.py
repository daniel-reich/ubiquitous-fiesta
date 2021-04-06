
import requests
def content_type(url):
  return requests.head(url).headers.get('content-type')

