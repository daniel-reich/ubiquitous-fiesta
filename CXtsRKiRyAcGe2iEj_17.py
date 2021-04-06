
def findChar(txt):
  count = 0
  for char in txt:
    if char != " ":
      count += 1
  return count
​
def time_to_finish(full, part):
  fcount = findChar(full)
  pcount = findChar(part)
  return (fcount-pcount)/2

