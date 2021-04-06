
def number_length(num):
  num_length = 0
  num_str = str(num)
  for digit in num_str:
    num_length += 1
  
  return num_length

