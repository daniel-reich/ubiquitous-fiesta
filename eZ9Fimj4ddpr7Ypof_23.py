
def mumbling(s):
  return '-'.join((ch*i).capitalize() for ch, i in enumerate(s, start=1))

