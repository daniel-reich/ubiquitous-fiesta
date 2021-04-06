
def tidy_books(lst):
  return [[i[0].split(' - ')[0].lstrip(), i[0].split(' - ')[1].rstrip()] for i in lst]

