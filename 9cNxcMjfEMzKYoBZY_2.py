
def num_type(n):
  x_sum = sum([d for d in range(1, n) if n % d == 0])
  if x_sum == n:
    return 'Perfect'
  else:
    y_sum = sum([d for d in range(1, x_sum) if x_sum % d == 0])
    if y_sum == n:
      return 'Amicable'
    else:
      return 'Neither'

