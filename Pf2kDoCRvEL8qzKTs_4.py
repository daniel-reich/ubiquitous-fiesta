
def order_people(lst, people):
  if people>lst[0]*lst[1]:return  "overcrowded"
  l=list(range(1,people+1))
  for i in range(0,(lst[0]*lst[1])-people):l.append(0)
  m=[l[i:i+lst[1]] for i in range(0,len(l),lst[1])]
  return [m[i] if i%2==0 else m[i][::-1] for i in range(len(m))]

