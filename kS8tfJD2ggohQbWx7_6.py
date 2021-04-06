
def last_name_lensort(names):
  names =[i.split() for i in names]
  d = {i[1]:i[0] for i in names}
  last = sorted(sorted(d.keys()),key=len)
  return [d.get(i) + ' ' + i for i in last]

