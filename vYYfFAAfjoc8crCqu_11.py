
def tree(h):
  return [('#'*(2*i + 1)).join([' '*(h - 1 - i)]*2) for i in range(h)]

