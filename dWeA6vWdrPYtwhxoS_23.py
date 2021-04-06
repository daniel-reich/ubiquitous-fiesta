
def count_number(lst):
  lst = str(lst).split(',')
  return sum(any(x.isdigit() for x in word) for word in lst)

