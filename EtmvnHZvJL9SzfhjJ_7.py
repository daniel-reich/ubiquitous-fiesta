
def strip_url_params(url, params_to_strip=[]):
  if url.find('?') == -1:
    return url
  param_string = url[url.find('?')+1:]
  params = {}
  while len(param_string) > 0:
    eq = param_string.find('=')
    amp = param_string.find('&')
    key = param_string[:eq]
    if amp == -1:
      value = param_string[eq+1:]
      param_string = ''
    else:
      value = param_string[eq+1:amp]
      param_string = param_string[amp+1:]
    params[key] = value
  for item in params_to_strip:
    params.pop(item, None)
  new_url = url[:url.find('?')+1]
  for key in sorted(params):
    new_url += (key + '=' + params[key] + '&')
  return new_url[:-1]

