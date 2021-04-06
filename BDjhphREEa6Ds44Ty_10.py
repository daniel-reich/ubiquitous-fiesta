
def bomb(lst):
  x = lambda a,b,i: round((a-i[0])**2 + (b-i[1])**2) == round((i[2]*.343)**2)
  for a in range(51):
    for b in range(51):
      if all(x(a,b,i) for i in lst): return (a,b)

