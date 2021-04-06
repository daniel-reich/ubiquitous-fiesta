
def reorder_digits(lst, direction):
  return [int("".join(sorted(list(str(num)),reverse={"asc":False,"desc":True}[direction]))) for num in lst]

