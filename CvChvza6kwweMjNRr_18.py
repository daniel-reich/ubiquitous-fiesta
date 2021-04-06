
def split_code(item):
  l = ""
  d = ""
  for i in item:
    if i.isalpha():
      l += i
    if i.isdigit():
      d += i
  return [l, int(d)]

