
def mumbling(s):
  return '-'.join("{0}{1}".format(i, i.lower() * idx) for idx, i in enumerate(s.upper()))

