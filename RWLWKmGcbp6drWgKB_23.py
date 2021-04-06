
def chosen_wine(wines):
  dic = {}
  for wine in wines:
    dic[wine['name']] = wine['price']
  l = sorted(dic.values())
  if len(l) == 0: return None
  else:
    if len(l) == 1: x = l[0]
    if len(l) > 1: x = l[1]
  for k,v in dic.items():
    if v == x: return k

