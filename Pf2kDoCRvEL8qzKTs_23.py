
def order_people(lst, people):
  if lst[0] * lst[1] < people:
    return "overcrowded"
  else:
    newlst = list(range(1,people + 1))
    if lst[0] * lst[1] > people:
      newlst.extend([0 for i in range(0,lst[0]*lst[1]-people)])
    new = list(map(lambda x: newlst[x:x+lst[1]],range(0,len(newlst),lst[1])))
    for i in range(1,len(new),2):
      new[i].reverse()
      
    return new

