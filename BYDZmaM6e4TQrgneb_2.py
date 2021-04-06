
def fibFast(num):
  lst = [0,1]
  while len(lst)<=num:
    lst.append(lst[-2]+lst[-1])
  return lst[num]

