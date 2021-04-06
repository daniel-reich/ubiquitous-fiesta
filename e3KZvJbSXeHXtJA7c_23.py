
def sum_missing_numbers(lst):
  return sum(i for i in range(min(lst),max(lst),1) if i not in lst)

