
def boxes(weights):
  count = 0
​
  i, temp = 0, 0
  while i in range(len(weights)):
    if temp + weights[i] <= 10:
      temp += weights[i]
      i += 1
    else:
      count += 1
      temp = 0
  if temp:
    count += 1
  return count

