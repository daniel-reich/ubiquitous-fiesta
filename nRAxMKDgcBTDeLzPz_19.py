
def circular_shift(lst1, lst2, n):
  if n==0: return lst1==lst2
  elif n>0:
    return lst1[0:len(lst1)-n]==lst2[n:]
  else:
    n=n*-1
    return lst2[0:len(lst2)-n]==lst1[n:]

