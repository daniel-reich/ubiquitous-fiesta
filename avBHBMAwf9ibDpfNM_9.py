
import requests
def content_type(url):
  a = requests.get("https://edabit.com")
  return a.headers['Content-Type']

