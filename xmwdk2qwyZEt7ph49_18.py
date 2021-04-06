
def get_length(lst):
  count = 0
  for x in lst:
    if type(x) == list:
      count += get_length(x)
    else:
      count += 1
  return count

