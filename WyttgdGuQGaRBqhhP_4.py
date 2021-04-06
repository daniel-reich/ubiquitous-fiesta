
def min_palindrome_steps(txt):
  add = 0
  pal = txt
  while pal != pal[::-1]:
    add += 1
    pal = txt + txt[:add][::-1]
  return add

