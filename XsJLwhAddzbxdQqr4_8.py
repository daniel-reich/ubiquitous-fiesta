
def difference_max_min(lst):
  max = lst[0]
  min = lst[0]
  for num in lst:
    if (num > max): max = num
    elif (num < min): min = num
  return max - min

