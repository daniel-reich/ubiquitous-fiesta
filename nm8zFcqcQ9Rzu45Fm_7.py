
def bridge_shuffle(lst1, lst2):
  if len(lst1) > len(lst2):
      for _ in range(len(lst1)-len(lst2)):
          lst2.append(0)
  else:
      for _ in range(len(lst2)-len(lst1)):
          lst1.append(0)
  a = zip(lst1, lst2)
  c = []
  z = list(a)
  for x in z:
      for b in x:
          c.append(b)
  return [v for v in c if v !=0]

