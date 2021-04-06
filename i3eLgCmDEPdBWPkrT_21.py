
def limit_number(n, l, h):
  if l <= n <= h:
    return n
  elif n < l:
    return l
  elif n > h:
    return h

