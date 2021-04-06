
def highest_digit(num):
  lst = []
  for i in str(num):
    lst.append(int(i))
  return max(lst)

