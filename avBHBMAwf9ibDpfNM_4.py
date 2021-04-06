
import requests
content_type=lambda u:requests.get(u).headers['content-type']

