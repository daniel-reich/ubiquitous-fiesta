
def count_missing_nums(lst):
  lst = [int(i) for i in lst if i.isdigit()]
  return sum(i not in lst for i in range(min(lst),max(lst)))

