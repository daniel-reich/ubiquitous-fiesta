
def to_list(num):
  return list(map(int, str(num)))
​
def to_number(lst):
  return int(''.join(str(s) for s in lst))

