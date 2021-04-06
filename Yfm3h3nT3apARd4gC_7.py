
def rolls(lst):
  y=0
  for x in range(len(lst)):
    if lst[x]==1 and x!=len(lst)-1:
      y+=1
      y-=lst[x+1]
    elif lst[x]==6 and x!=len(lst)-1:
      y+=6+lst[x+1]
    else:
      y+=lst[x]
  return y

