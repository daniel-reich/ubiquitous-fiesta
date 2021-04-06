
def is_ord_sub(s, b):
  for i in s:
    if i in b:
      b = b[b.index(i)+1:]
    else:
      return False
  return True

