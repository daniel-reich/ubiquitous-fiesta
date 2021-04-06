
def is_heteromecic(n):
  if n == 0:
      return True
  else:
      for number in range(n):
          if number * (number + 1) == n:
              return True
      return False

