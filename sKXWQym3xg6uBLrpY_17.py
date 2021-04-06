
def iqr(lst):
  def get_median_index(numbers):
    return (len(numbers) - 1) / 2.0
  
  def get_new_list(numbers, midpoint):
    if midpoint % 1 == 0:
      return {'lower': numbers[:int(midpoint)],
              'higher': numbers[int(midpoint + 1):]}
    else:
      return {'lower': numbers[:int(midpoint) + 1],
              'higher': numbers[int(midpoint) + 1:]}
  
  def get_median_value(numbers, midpoint):
    if midpoint % 1 == 0:
      return numbers[int(midpoint)]
    else:
      return (numbers[int(midpoint)] + numbers[int(midpoint) + 1]) / 2.0
​
  lst = sorted(lst)
  median = get_median_index(lst)
  lower = get_new_list(lst, median)['lower']
  higher = get_new_list(lst, median)['higher']
  q1_index = get_median_index(lower)
  q3_index = get_median_index(higher)
  q1_value = get_median_value(lower, q1_index)
  q3_value = get_median_value(higher, q3_index)
  return q3_value - q1_value

