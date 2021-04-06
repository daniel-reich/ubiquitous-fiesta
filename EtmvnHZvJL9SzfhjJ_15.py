
from collections import OrderedDict
​
def strip_url_params(url, params_to_strip=[]):
  try:
    params_start = url.index('?')
  except ValueError:
    return url
  url_raw = url[:params_start]
  params = OrderedDict([pp.split('=') for pp in url[params_start+1:].split('&')])
  for param in params_to_strip:
    try:
      del params[param]
    except KeyError:
      pass
  if params:
    return url_raw + '?' + '&'.join([k+'='+v for k, v in params.items()])
  else:
    return url_raw

