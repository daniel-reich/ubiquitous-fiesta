
def find_sum(num):
  txt = str(num)
  total = 0
  for dig in txt:
    total += int(dig)
  return total
​
def is_equal(lst):
  return find_sum(lst[0]) == find_sum(lst[1])

