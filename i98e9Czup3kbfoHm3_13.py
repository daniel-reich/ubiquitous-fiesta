
def text_to_number_binary(txt):
  d={'one':'1','zero':'0'}
  res = ''.join(d[x] for x in txt.lower().split() if x in d)
  return res[:-(len(res)%8)] if len(res)%8 else res

