
def simon_says(lst1, lst2):
  aux=0
  tam=len(lst1)
  for i in range(tam-1):
    if lst1[i]!=lst2[i+1]:
      return False
  return True

