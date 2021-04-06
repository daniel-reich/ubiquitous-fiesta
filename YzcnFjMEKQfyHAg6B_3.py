
def simon_says(lst1, lst2):
  for i in range(len(lst1)-1):
    if lst2[i+1]!=lst1[i]: return False
  return True

