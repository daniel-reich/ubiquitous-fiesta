
def reorder_digits(lst, direction):
  a = []
  for i in lst:
    num = ''.join(sorted(str(i)))
    if direction == "asc":
      a.append(int(num))
    if direction == "desc":
      a.append(int(num[::-1]))
  return a

