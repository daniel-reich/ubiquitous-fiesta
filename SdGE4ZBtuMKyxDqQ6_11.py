
def first_repeat(chars):
  unique = []
  for n in chars:
    if n not in unique:
      unique.append(n)
    else:
      return n
  return '-1'

