
def count_ones(lst):
  new_lst = " ".join([str(x) for x in lst]).split("0")
  return len([x for x in new_lst if x.count("1")> 1])

