
def order_people(lst, people):
  fl = []
  fltemp = []
  if people > lst[0]*lst[1]:
    return 'overcrowded'
  else: 
    l = [i+1 for i in range(people)] + [0]*(lst[0]*lst[1]-people)
    for j in range(lst[0]):
      for k in range(lst[1]):
        fltemp.append(l[j*lst[1]+k])
      fl.append(fltemp)
      fltemp = []
  return [fl[i][::-1] if i%2 ==1 else fl[i] for i in range(len(fl))]

