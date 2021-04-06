
def left_shift(lst, n):
  if n%len(lst)==0:
    return lst
  elif n<len(lst):
    return lst[n:len(lst)]+lst[0:n]
  else:
    return lst[n%len(lst):len(lst)]+lst[0:n%len(lst)]
​
def right_shift(lst, n):
  if n%len(lst)==0:
    return lst
  elif n<len(lst):
    return lst[-n:]+lst[0:len(lst)-n]
  else: 
    return lst[-n%len(lst):]+lst[0:len(lst)-n%len(lst)]

