
def sort_it(lst):
  return sorted(lst, key=lambda i:i if isinstance(i,int) else i[0])

