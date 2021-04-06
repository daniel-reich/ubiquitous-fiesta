
def is_ascending(s):
  for i in range(1, len(s)):
    lst = [s[i*n: i*n + i] for n in range(len(s) // i + 1)]
    lst = [int(e) for e in lst if e != '']
​
    if all(y - x == 1 for x, y in zip(lst, lst[1:])):
      return True
​
  return False

