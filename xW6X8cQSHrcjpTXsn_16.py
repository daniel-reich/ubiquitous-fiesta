
def first_and_last(s):
  l=[c for c in s]
  first="".join(sorted(l))
  return [first,first[::-1]]

