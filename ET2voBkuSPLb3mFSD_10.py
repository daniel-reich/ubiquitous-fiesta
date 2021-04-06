
def sum_every_nth(numbers, n):
  l = len(numbers)
  index_list = []
  for i in range(l):
    k = i+1
    if k % n == 0:
      index_list.append(i)
  count = 0
  for location in index_list:
    count += int(numbers[location])
  return(count)

