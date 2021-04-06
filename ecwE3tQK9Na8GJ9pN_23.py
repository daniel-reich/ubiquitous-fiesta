
def little_big(n):
  if n % 2 == 1:
    return 5 + n // 2
  else:
    return 50 * pow(2,n // 2)

