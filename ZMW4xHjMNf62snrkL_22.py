
def second_largest(lst):
  lst.remove(max(lst))
  return max(lst)

