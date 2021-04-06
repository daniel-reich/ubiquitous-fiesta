
def dict_to_list(d):
  return list(map(lambda x: (x,d[x]),sorted(d.keys())))

