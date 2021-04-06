
def count_missing_nums(lst):
  numbers = sorted(int(x) for x in lst if x.isdigit())
  return 1 + numbers[-1] - numbers[0] - len(numbers)

