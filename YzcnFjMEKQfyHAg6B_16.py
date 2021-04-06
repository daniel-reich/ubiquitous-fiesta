
def simon_says(lst1, lst2):
  if lst1[0] == lst2[0] or lst1[0] == lst2[1] or lst1[1] == lst2[0] or lst1[1] == lst2[1]:
    return True
  else:
    return False

