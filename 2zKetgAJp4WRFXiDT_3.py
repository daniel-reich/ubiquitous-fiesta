
def number_length(num):
  count = 0
  if num == 0:
    return 1
  else:
    while num != 0:
      num//=10
      count += 1
    return count

