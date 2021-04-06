
def get_length(lst):
  count = 0
  for elem in lst:
    if type(elem) == list:
      count += get_length(elem)
    else:
      count += 1
  return count

