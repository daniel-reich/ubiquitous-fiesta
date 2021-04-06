
def factorial(num):
  if num > 1:
    result = num * factorial(num-1)
  else: 
    result = 1
  return result

