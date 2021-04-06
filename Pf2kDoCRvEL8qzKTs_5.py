
def order_people(lst, people):
  ordered = [[0 for x in range(lst[1])] for y in range(lst[0])]
  num = 1
  for i in range(lst[0]):
    for j in range(lst[1]):
      if i % 2 == 1:
        ordered[i][-j - 1] = num
      else:
        ordered[i][j] = num
      if num >= people:
        return ordered
      elif num >= lst[0] * lst[1]:
        return "overcrowded"
      num += 1

