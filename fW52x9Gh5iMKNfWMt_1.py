
def recaman_index(n):
  blank = []
  lst = [0]
  for i in range(10000):
    if lst[-1] - len(lst)<0:
      number  = len(lst) + lst[-1]
      lst.append(number)
    elif lst[-1] - len(lst)>=0 and lst[-1] - len(lst)  in lst:
      new_number = len(lst)+lst[-1]
      lst.append(new_number)
    else:
      newest = lst[-1]-len(lst)
      lst.append(newest)
  return lst.index(n)

