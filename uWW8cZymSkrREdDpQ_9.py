
def sums_up(lst):
  pairs = []
  for index_a, number_a in enumerate(lst):
    for index_b, number_b in enumerate(lst[index_a + 1:], start=index_a + 1):
      if number_a + number_b == 8:
        element = [index_b, sorted([number_a, number_b])]
        pairs.append(element)
  pairs = [item[1] for item in sorted(pairs)]
  return {'pairs': pairs}

