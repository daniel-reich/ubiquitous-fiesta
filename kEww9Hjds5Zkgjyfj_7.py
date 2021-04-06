
def replace_next_largest(lst):
  return [-1 if elem == max(sorted(lst)) else sorted(lst)[sorted(lst).index(elem) + 1] for elem in lst]

