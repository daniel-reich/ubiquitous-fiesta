
def meme_sum(a, b):
  sa, sb = str(a), str(b)
  if len(sa) > len(sb):
    sb = '0' * (len(sa) - len(sb)) + sb
  elif len(sb) > len(sa):
    sa = '0' * (len(sb) - len(sa)) + sa
  res = ''
  for i, j in zip(sa, sb):
    res += str(int(i) + int(j))
  return int(res)

