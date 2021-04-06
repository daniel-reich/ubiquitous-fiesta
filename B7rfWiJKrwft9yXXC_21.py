
def sort_descending(num):
  lst = reversed(sorted([digit for digit in str(num)]))
  res = ""
  for ele in lst:
    res += ele
  return int(res)

