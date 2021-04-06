
def odd_sort(lst):
  odds = sorted([num for num in lst if num%2])
  return [odds.pop(0) if num%2 else num for num in lst]

