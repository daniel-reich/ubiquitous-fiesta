
def is_repeated(st):
  s=(st+st).find(st, 1, -1)
  return 24/s if s!=-1 else False

