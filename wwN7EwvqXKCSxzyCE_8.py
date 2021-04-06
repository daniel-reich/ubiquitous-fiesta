
def reorder_digits(lst, direction):
  return [int("".join(sorted(str(n), reverse=direction == "desc"))) for n in lst]

