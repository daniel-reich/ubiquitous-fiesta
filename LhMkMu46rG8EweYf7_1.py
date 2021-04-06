
def sort_by_letter(lst):
  return sorted(lst,key=lambda x: [l for l in x if l.isalpha()])

