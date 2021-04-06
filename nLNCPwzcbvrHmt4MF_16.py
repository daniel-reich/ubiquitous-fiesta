
def fibonacci_sequence():
  fibbonacci = [0, 1]
  total = 0
  index = 1
​
  while fibbonacci[-1] < 233:
    total += fibbonacci[-1] + fibbonacci[-2]
    fibbonacci.append(total)
    total = 0
​
​
  return fibbonacci

