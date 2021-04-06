
def validate_swaps(lst, txt):
  a=[]
  for i in lst:
      x=0
      for j in zip(i,txt):
          print((set(j)))
          if len(set(j)) != 1:
              x=x+1
      a.append(x==2 and len(i)==len(txt))
  return (a)

