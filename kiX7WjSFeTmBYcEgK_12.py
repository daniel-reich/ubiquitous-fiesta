
def major_sum(lst):
  zeros = lst.count(0)
  positive = sum(i for i in lst if i > 0)
  negative = sum(i for i in lst if i < 0)
  highest = max(zeros,positive,-negative)
  if highest == -negative:
    return negative
  return highest

