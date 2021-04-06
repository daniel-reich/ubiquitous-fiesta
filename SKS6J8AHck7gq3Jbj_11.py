
def tidy_books(lst):
  for idx, x in enumerate(lst):
    lst[idx] = x[0].strip()
    lst[idx] = [lst[idx].split(' - ')[0], lst[idx].split(' - ')[1]]
  return lst

