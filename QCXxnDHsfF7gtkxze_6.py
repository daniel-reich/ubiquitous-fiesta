
def mystery_func(num):
  a = [(int(x)) for x in str(num)]
  result = 1
  for i in a:
    result = result * i
  return result

