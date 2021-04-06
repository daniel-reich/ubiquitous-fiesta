
def strip_url_params(url, params_to_strip=None):
  if '?' not in url:
    return url
  q = url.index('?')
  mod = url[q+1:]
  param = mod.split('&')
  newparam = []
  for i in reversed(param):
    if not i[0] in [j[0] for j in newparam]:
      newparam.append(i)
  if params_to_strip:
    for i in params_to_strip:
      newparam = list(filter(lambda x:i not in x,newparam))
  return url[:q+1]+"&".join(sorted(newparam))

