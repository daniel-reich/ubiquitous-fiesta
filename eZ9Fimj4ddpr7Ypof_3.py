
def mumbling(s):
  return '-'.join((s[i] * (i + 1)).capitalize() for i in range(len(s)))

