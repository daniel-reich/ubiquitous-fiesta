
def is_shuffled_well(lst):
  return "11" not in "".join([str(abs(a-b)) for a,b in zip(lst,lst[1:])])

