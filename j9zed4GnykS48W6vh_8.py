
def digits(number):
  
  n_digits = 0
  so_far = 1
  length = 0
​
  while True:
    if so_far >= number:
      n_digits += length * (number - int(so_far/10))
      break
    else:
      n_digits += length * (so_far - int(so_far/10))
      length += 1
      so_far = so_far * 10
  
  return n_digits

