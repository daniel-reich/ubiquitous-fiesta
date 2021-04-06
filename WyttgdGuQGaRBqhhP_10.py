
def min_palindrome_steps(txt):
  for i in range(len(txt)):
    check = txt + txt[:i][::-1]
    if check == check[::-1]:
      return i

