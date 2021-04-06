
def strip_url_params(url, params_to_strip = []):
  if '?' not in url:
    return url
  ind = url.index('?')
  end = url[ind+1:]
  pts = end.split('&')
  left = {}
  for pt in pts:
    if pt[0] not in params_to_strip:
      left[pt[0]] = pt[-1]
  l = [k + '=' + v for k,v in left.items()]
  l.sort()
  s = '&'.join(l)
  lr = url[:ind+1] + s
  return lr

