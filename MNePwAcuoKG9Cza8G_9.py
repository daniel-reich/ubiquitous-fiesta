
def build_staircase(height, block):
  lst = []
  for i in range(1, height+1):
    lst.append(i*block + (height-i)*"_")
  lst2 = []
  for i in range(0, len(lst)):
    lst2.append(list(lst[i]))
  return lst2

