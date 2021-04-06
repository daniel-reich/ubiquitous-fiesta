
# Fix this broken code!
def check_equals(lst1, lst2):
  n =0
  for i in lst1:
    for j in lst2:
      if(i==j):
        n+=1
  if n==len(lst1) and len(lst2):
    return True
  else:
    return False

