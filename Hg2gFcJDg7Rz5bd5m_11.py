
def intersection(h1, h2):
  ret1 = {}
  ret2 = {}
  for i in h1.keys():
    if i in h2.keys():
      ret1[i]=h1[i]
  for i in h2.keys():
    if i in h1.keys():
      ret2[i]=h2[i]
  return [ret1,ret2]

