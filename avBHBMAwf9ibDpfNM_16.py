
def content_type(url):
    import requests
    x=requests.get(url)
    return x.headers['content-type']

