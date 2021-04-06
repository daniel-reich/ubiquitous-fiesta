
def josephus(people):
  p_2 = [2 ** i for i in range(7)]
  for i in p_2:
    if people < i:
      power = i
      ind = p_2.index(i) - 1
      break
  diff = people - p_2[ind]
  return 1 + diff * 2

