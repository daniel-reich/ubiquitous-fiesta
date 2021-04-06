
def count_ones(num):
  count = 0
  for i in bin(num):
    if i == '1':
      count += 1
  return count

