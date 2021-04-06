
import requests
def content_type(url):
    r = requests.get('https://edabit.com/')
    return r.headers['content-type']

