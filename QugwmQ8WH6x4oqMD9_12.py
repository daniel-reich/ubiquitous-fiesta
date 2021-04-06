
def count_identical_lists(*lists):
  counter = 0
  for lst in lists:
    counter = max(lists.count(lst),counter)
  return counter if counter > 1 else 0

