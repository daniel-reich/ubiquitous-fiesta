
def replace_next_largest(lst):
  return [-1 if sorted(lst).index(intger) == len(lst) - 1 else sorted(lst)[sorted(lst).index(intger) + 1] for  intger in lst]

