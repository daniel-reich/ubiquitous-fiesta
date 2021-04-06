
def complete_square(lst): 
  M = max(len(lst),len(lst[0]))
  L = []
  addd = [0 for u in range(M-len(lst[0]))]
  if len(lst) <M:
    for i in range(M-len(lst)):
      lst.append([0 for i in range(M)])
  elif len(lst[0])<M:
    for i in range(len(lst)):
      lst[i]+=addd
  return lst

