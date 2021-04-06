
def reorder_digits(lst, direction):
  return [int(y) for y in [''.join(sorted(str(x),reverse=direction=='desc')) for x in lst]]

