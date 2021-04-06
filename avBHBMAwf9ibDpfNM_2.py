
import requests
def content_type(url):
  response = requests.get('https://edabit.com/')
  return response.headers['content-type']

