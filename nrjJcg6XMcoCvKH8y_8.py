
def validate_subsets(subsets, my_set):
  a=subsets
  b=my_set
  c=[]
  for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][j] in b:
        c.append(1)
      else:
        c.append(0)
  return all(c)

