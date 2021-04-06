
def simon_says(lst1, lst2):
  len_lst1 = len(lst1)
  for i in range(len_lst1-1):
    if lst1[i] != lst2[i+1]: return False
  return True

