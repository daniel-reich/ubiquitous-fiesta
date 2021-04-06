
def circular_shift(lst1, lst2, n):
  if n>0:
    for x in range (n):
      ele=lst2.pop()
      lst2.insert(0,ele)
    return lst1==lst2
  else:
    for x in range (abs(n)):
      ele=lst2.pop(0)
      lst2.append(ele)
    return lst1==lst2

