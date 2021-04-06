
def news_at_ten(txt, n):
  txt, size = " "*n + txt + " "*n, len(txt) + n
  return [txt[i:i+n] for i in range(size+1)]

