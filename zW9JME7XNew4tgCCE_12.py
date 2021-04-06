
def reversible_inclusive_list(start, stop):
  return list(range(start, stop + 1)) or \
    list(range(stop, start + 1))[::-1]

