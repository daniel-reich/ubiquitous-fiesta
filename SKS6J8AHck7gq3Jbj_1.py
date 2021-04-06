
def tidy_books(lst):
  return [[names.strip() for names in item[0].split('-')] for item in lst]

