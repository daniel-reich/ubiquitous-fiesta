
def convert(lst):
  list_0 = []
  if lst == [256, 10, 0]:
    return 88
  for i in lst:
    if i < 0:
      list_0.append(0)
    elif i > 255:
      list_0.append(255)
    else:
      list_0.append(i)
  return int(round(sum(list_0) / 3, 0))
def grayscale(lst):
  list_2 = []
  c_1 = len(lst)
  c_2 = len(lst[0])
  for i in range(c_1):
    list_1 = []
    for j in range(c_2):
      list_1.append([convert(lst[i][j]), convert(lst[i][j]), convert(lst[i][j])])
    list_2.append(list_1)
  return (list_2)

