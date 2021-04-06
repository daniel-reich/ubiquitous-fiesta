
def sort_by_letter(lst):
  return sorted(lst, key=lambda x: sorted(x)[-1])

