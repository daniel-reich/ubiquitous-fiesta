
def min_palindrome_steps(txt):
  for i in range(len(txt)):
    tmp = txt[:i]
    if txt + tmp[::-1] == tmp + txt[::-1]:
      return i

