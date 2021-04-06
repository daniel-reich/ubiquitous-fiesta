
def min_miss_pos(lst):
  for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
​
  for i in range(lst[0], lst[-1] + 2):
    if i not in lst and i != 0 and i > 0:
      return i

