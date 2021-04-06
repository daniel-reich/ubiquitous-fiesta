
def tallest_skyscraper(lst):
  result = []
​
  for row in lst:
    for i, floor in enumerate(row):
      if i < len(result):
        result[i] += floor
      else:
        result.insert(i , floor)
​
  result.sort(reverse=True)
​
  return result[0]

