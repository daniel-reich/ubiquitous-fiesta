
def largest_gap(lst):
  return max(sorted(lst)[x + 1] - sorted(lst)[x] for x in range(len(lst) - 1))

