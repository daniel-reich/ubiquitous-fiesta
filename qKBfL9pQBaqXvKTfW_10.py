
def sum_of_slices(lst):
  temp = []
  result = []
  for x in lst:
    if sum(temp) + x <= 100:
      temp.append(x)
    else:
      result.append(sum(temp))
      temp.clear()
      temp.append(x)
  result.append(sum(temp))
  return result

