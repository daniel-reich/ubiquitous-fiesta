
def count_missing_nums(lst):
  lst = [int(i) for i in lst if i.isdigit()]
  return len([i for i in range(min(lst), max(lst)) if i not in lst])

