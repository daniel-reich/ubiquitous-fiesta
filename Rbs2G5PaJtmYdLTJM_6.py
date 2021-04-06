
def is_heteromecic(n, guess=0):
  if guess * guess > n:
    return False
  elif guess * (guess + 1) == n:
    return True
  return is_heteromecic(n, guess + 1)

