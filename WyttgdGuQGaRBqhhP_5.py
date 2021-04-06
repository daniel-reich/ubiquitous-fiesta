
def min_palindrome_steps(txt):
  i=0
  while txt+txt[:i][::-1]!=(txt+txt[:i][::-1])[::-1]:
    i+=1
  return i

