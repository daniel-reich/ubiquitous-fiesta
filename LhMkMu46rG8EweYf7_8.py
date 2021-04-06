
def sort_by_letter(lst):
  return sorted(lst, key=lambda x:[i for i in x if i.isalpha()][0])

