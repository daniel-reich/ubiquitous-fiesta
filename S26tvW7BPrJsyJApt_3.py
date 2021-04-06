
def next_in_line(l, n):
  l.append(n)
  l.pop(0)
  return l if l else "No list has been selected"

