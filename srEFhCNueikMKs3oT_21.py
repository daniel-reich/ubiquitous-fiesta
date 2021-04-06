
def consecutive_sum(n):
  if n % 2 == 1:
    return True
  else:
    factors_two = 0
    copy_n = n
    while copy_n > 1:
      if copy_n % 2 == 0:
        factors_two += 1
      copy_n = copy_n // 2
    if pow(2,factors_two) == n:
      return False
    else:
      return True

