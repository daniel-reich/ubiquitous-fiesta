
def clear_ordering(lst):
  return len(set(i[0] for i in lst))==len(lst) and len(set(i[1] for i in lst))==len(lst)

