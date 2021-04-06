
def digital_division(n):
  number = n
  score = 0
  sum_digits = 0
  product_digits = 1
  digit_divisible = True
  
  while n > 0:
    digit = n % 10
    n = n // 10
    sum_digits += digit
    product_digits *= digit
    if digit_divisible and digit != 0 and number % digit != 0:
      digit_divisible = False
  
  if digit_divisible:
    score += 1
  for num in (sum_digits, product_digits):
    if num != 0 and number % num == 0:
      score += 1
  
  if score == 0:
    return 'Indivisible'
  elif score == 3:
    return 'Perfect'
  else:
    return score

