
def mystery_func(num):
  result = 1
  digits = [int(x) for x in str(num)]
  for i in digits:
    result = result * i 
  return result

