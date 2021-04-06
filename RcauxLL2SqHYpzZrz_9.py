
def true_equations(lst):
  l=[]
  for i in lst:
    index=i.index('=')
    if eval(i[:index])==int(i[index+1:]):
      l.append(i)
  return l

