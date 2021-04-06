
def longest_zero(s):
  zero_counter = 0
  counter_lst = []
  
  for digit in s:
    if digit == '0':
      zero_counter += 1
      counter_lst.append(zero_counter)
    else:
      zero_counter = 0
  
  return '0' * max(counter_lst) if len(counter_lst) >= 1 else ""

