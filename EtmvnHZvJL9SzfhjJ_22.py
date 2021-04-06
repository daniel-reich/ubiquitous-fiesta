
def strip_url_params(url, params_to_strip = []):
  if url.count("?") < 1:
    return url
  params = url.split("?")[1].split("&")
  returnparams = {}
  returnkeys = []
  for param in params:
    key, value = param.split("=")
    if key in params_to_strip:
      continue
    if key in returnkeys:
      returnparams[key] = value
    else:
      returnkeys.append(key)
      returnparams[key] = value
  returnurl = url.split("?")[0] + "?"
  for key in returnkeys:
    returnurl += key + "=" + returnparams[key] + "&"
  returnurl = returnurl[:-1]
  return returnurl

