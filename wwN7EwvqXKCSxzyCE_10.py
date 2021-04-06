
def reorder_digits(lst, direction):
  return [int(''.join(sorted(list(str(i)),reverse=True))) if direction=="desc" else int(''.join(sorted(list(str(i))))) for i in lst]

