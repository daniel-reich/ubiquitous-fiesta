
from collections import OrderedDict 
​
def extract_params(param):
  key_value = param.split("=")
  return (key_value[0], key_value[1])
​
def strip_url_params(url, params_to_strip=[]):
  parts = url.split('?')
  if len(parts) == 1:
    return url
  url = parts[0]
  parameters = parts[1]
  params_map = OrderedDict(map(extract_params, parameters.split("&")))
  params_string = ["=".join([key, val]) for (key, val) in params_map.items() if key not in params_to_strip]
  return url + "?" + "&".join(params_string)

