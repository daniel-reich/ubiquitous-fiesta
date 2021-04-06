
def remove_repeats(s):
  st = s[0]
  for i in s:
    if i != st[-1]:
      st += i
  return st

