
def combine(lst):
  d = dict()
  for x in lst:
    try :
      d[x[0]] += [x[2]]
    except : d[x[0]] = [x[2]]
  return d

