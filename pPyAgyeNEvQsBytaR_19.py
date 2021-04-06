
def factorial(n):
  counter = n
  counter2 = n
  if n == 0:
    return 1
  for x in range (counter2):
    counter = counter - 1
    if x < n and counter > 0:
      n = n * counter
    else:
      n = n
  return n

