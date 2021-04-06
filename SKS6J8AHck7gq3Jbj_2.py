
def tidy_books(lst):
  return [i[0].strip().split(" - ") for i in lst]

