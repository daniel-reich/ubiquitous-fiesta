
def strip_url_params(url, params_to_strip=''):
  if url.endswith('.com'): return url
  
  x = url.split('?')
  y = x[1].split('&')
  temp = [i for i in y if i[0] not in params_to_strip]
  tmp_1 = [x for x in temp for y in temp
      if x[0] == y[0] and int(x[2]) > int(y[2])
                and x is not y]
  if not tmp_1:
    string = '&'.join(temp)
    return x[0] + '?' + string
  
  if tmp_1:
    lst = []
    for i in temp:
      if (i[0] == tmp_1[0][0] and
        int(i[2]) < int(tmp_1[0][2])):
        lst.append(tmp_1[0])
      elif i not in lst:
        lst.append(i)
    string = '&'.join(lst)
    return x[0] + '?' + string

