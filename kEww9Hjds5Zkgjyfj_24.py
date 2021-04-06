
def replace_next_largest(lst):
  return [-1 if lst[i]==max(lst) else sorted(lst)[sorted(lst).index(lst[i]):][1] for i in range(len(lst))]

