
def is_harshad(n):
  n_str = str(n)
  digit_sum = 0
  for i in range(0, len(n_str)):
    digit_sum = digit_sum + int(n_str[i])
  if n % digit_sum == 0:
    return True
  else:
    return False

