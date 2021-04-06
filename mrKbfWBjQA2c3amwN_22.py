
def mult_table(n):
  lst = [list(range(1,n+1))]
  for i in range(2,n+1):
    lst.append(list(range(i,n*i+1,i)))
  return lst

