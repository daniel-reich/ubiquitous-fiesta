
def left_side(lst):
  result = []
  for i in range(len(lst)):
    count = 0
    for num in lst[:i]:
      if lst[i] > num:
        count += 1
    result.append(count)
  return result
​
def right_side(lst):
  lst = lst[::-1]
  result = []
  for i in range(len(lst)):
    count = 0
    for num in lst[:i]:
      if lst[i] > num:
        count += 1
    result.append(count)
  return result[::-1]

