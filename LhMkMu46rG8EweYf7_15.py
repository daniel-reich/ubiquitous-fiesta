
def sort_by_letter(lst):
  return sorted(lst, key=lambda i: [l for l in i if l.isalpha()][0])

