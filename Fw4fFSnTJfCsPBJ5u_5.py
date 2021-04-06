
def how_many_missing(lst):
  try:
    return len([i for i in range(min(lst), max(lst) +1)]) - len(lst)
  except ValueError:
    return 0

