
import re
​
def strip_url_params(url, *params_to_strip):
  d = {}
  for i in [x.split('=') for x in re.findall("[a-z]=[0-9]", url)]:
    d[i[0]] = i[1] #url to dict
​
  if params_to_strip: #delete params
    [d.pop(i) for i in params_to_strip[0] if i in d]
​
  s = ''.join(sorted(['{}={}&'.format(i, d[i]) for i in d]))
  if s and s[-1] == '&': s = s[:-1] #from dict to url
​
  return re.sub('[a-z]=[0-9].*', s, url) #change url

