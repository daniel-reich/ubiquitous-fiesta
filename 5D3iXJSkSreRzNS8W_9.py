
def news_at_ten(txt, n):
  k = n * ' ' + txt + n * ' '
  return list(map(lambda x: k[x:x+n],range(0,len(k)-n+1)))

