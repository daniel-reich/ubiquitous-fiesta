
def strip_url_params(*args):
  url = args[0]
  if len(args) == 2:
    params_to_strip = args[1]
  else:
    params_to_strip = []
  lst = url.split('?')
  if len(lst) == 1:
    return url
  else:
    params_string, dct, var = lst[1], {}, []
    items = params_string.split('&')
    for item in items:
      lst1 = item.split('=')
      dct[lst1[0]] = lst1[1]
      if lst1[0] not in params_to_strip and lst1[0] not in var:
        var.append(lst1[0])
    return lst[0] + "?" + "&".join([variable + "=" + dct[variable] for variable in var])

