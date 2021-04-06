
def count_missing_nums(lst):
  digits = [int(i) for i in lst if i.isnumeric()]
  return len(list(range(min(digits),max(digits)+1))) - len(digits)

