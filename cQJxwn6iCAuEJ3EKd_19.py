
def digits_count(num):
  if type(num) == float and int(num) == 0:
    return 0
  elif type(num) == int and num == 0:
    return 1
  else:
    counter = 1
    counter += digits_count(num/10)
    return counter

