
def min_palindrome_steps(txt):
  for i in range(len(txt)):
    tmp = txt[i:]
    if tmp == tmp[::-1]:
      return i

