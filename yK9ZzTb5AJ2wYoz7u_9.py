
def floyd(up_to = None, n_row = None):
  i, lst = 1, []
​
  while True:
    lst.append([n for n in range(i, i + len(lst) + 1)])
    i = lst[-1][-1] + 1
​
    if (up_to and up_to < i) or (n_row and len(lst) == n_row):
      return lst

