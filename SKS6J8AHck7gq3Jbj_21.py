
def tidy_books(lst):
  return [[i.strip() for i in x[0].split('-')] for x in lst]

