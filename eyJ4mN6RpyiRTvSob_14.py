
def is_palindrome_possible(txt):
  def is_even(n):
    return n%2==0
  
  s = list(set(txt))
  counts = []
  one = 0
  
  for item in s:
    c = txt.count(item)
    if c != 1:
      counts.append(c)
    if c == 1:
      one += 1
  
  if one > 1:
    return False
  
  for count in counts:
    if is_even(count) == False:
      return False
  return True

