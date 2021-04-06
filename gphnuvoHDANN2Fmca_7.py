
def odd_sort(lst):
  odds = [num for num in lst if num % 2 > 0]
  odds.sort()
  for odd in odds:
    lst[lst.index(odd)] = '{}'
  lst = [str(num) for num in lst]
  lst = [int(num) for num in ','.join(lst).format(*odds).split(',')]
  return lst

