
def nearest_element(n, lst):
  min_value, result, index_result = 10000000, 0, 0
  for index, item in enumerate(lst):
    if abs(item - n) < min_value:
      result, min_value, index_result = item, abs(item - n), index
    elif abs(item - n) == min_value:
      if item > result:
        result, index_result = item, index
  return index_result

