
def get_length(lst):
  return sum(get_length(i) if type(i)==list else 1 for i in lst)

