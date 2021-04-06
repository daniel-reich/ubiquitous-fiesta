
def sort_by_letter(lst):
  return sorted(lst, key=lambda x: [c for c in x if c.isalpha()])

