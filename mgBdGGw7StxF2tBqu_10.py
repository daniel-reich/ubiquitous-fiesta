
def duplicates(txt):
  
  s = set(txt)
  
  count = 0
  
  for char in s:
    count += txt.count(char) - 1
  
  return count

