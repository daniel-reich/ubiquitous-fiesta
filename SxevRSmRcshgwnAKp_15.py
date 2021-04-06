
def pricey_prod(d):
  lista, listb, listc = [], [], []
  for k,v in d.items():
    if v >= 500:
      lista.append([v]+[k])
​
  for n in lista:
    listb.append(int(n[0]))
    listb.sort(reverse=True)
  for x in listb:
    for y in lista:
      if y[0] == x:
        listc.append(y[1])
​
  return listc

