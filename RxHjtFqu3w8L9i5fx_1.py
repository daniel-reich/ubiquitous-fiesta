
def bell(n):
  lst = [[1]]
  while len(lst) <= n:
    temp = [lst[-1][-1]]
    while len(lst[-1]) >= len(temp):
      temp.append(temp[-1]+lst[-1][len(temp)-1])
    lst.append(temp)
  return lst[n][0]

