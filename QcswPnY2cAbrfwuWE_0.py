
def filter_factorials(numbers):
  factorials=[1]
  n=max(numbers)
  temp=1
  for i in range(1,n+1):
      temp*=i
      factorials.append(temp)
  return [i for i in numbers if i in factorials]

