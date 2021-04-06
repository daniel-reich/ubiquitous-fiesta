
def identify(*cube):
  a=[len(i) for i in cube]
  if len(set(a))==1 and len(cube)==len(cube[0]):
    return "Full"
  elif len(set(a))==1 and len(cube)!=len(cube[0]):
    return "Non-Full"
  else:
    other=sum([i for i in a if i != max(a)])
    return "Missing {}".format(max(a)*len(a)-other-max(a)*a.count(max(a)))

