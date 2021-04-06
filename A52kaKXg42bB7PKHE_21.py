
def num_then_char(lst):
  s = sum(lst)
  c = sum([[i] if type(i) == str else [] for i in s])
  n = sum([[i] if type(i) != str else [] for i in s])
  s = sorted(n) + sorted(c)
  j = 0
  for i in lst:
    for k in range(len(i)):
      i[k] = s[j]
      j += 1
  return lst
​
def sum(lst):
  s = []
  for i in lst: s += i
  return s

