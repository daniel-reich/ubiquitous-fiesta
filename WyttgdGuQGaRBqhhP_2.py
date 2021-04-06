
def min_palindrome_steps(txt):
  for i in range(len(txt)):
    if txt[i:] == txt[i:][::-1]:
      return i

