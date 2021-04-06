
def count_missing_nums(lst):
  digits = set('0123456789')
  nums = [int(x) for x in lst if set(x) < digits]
  seq = range(min(nums)+1, max(nums))
  return len(set(seq) - set(nums))

