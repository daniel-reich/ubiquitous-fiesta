
def sort_it(lst):
  k={}
  j=[]
  for i in lst:
    if type(i) is int:
      k.update({i:i})
      j.append(i)
    else:
      k.update({i[0]:i})
      j.append(i[0])
  j = sorted(j)
  return [k[i] for i in j]

