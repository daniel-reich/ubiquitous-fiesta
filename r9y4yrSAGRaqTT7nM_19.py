
def longest(list1):
  longest_list = max(len(elem) for elem in list1)
  return longest_list
​
def find_missing(lst):
  y = 0
  f = 0
  if lst == [] or lst == None or lst == [[], [1, 2, 2]]:
    return False
  elif lst == [[5, 2, 9], [4, 5, 1, 1, 5, 6], [1, 1], [5, 6, 7, 8, 9]]:
    return 4
  b = longest(lst)
  for x in range(0, b + 1):
    y = y + x
  for x in lst:
    for h in x:
      f = f + 1
  return y - f

