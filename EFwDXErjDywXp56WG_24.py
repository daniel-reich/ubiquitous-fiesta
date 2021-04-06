
def is_in_order(txt):
  x = ''
  for i in sorted(txt):
    x += i
  return True if x == txt else False

