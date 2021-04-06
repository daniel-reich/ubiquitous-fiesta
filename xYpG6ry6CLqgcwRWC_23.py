
def sum_two_smallest_nums(lst):
  lst.sort()
  positives = []
  for number in lst:
    if number > 0:
      positives.append(number)
  return positives[0] + positives[1]

