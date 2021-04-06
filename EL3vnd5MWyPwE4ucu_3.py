
def fibonacci(n):
  numbers = [0,1]
  for i in range(2,n+1):
    numbers.append(numbers[i-2]+numbers[i-1])
  return str(numbers[-1])

