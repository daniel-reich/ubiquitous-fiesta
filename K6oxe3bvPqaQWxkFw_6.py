
def join_digits(n):
  new_lst = []
  
  for i in list(range(1, n + 1)):
    for k in str(i):
      new_lst.append(k)
      
  return '-'.join(i for i in new_lst)

