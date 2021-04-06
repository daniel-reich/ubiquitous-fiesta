
def is_narcissistic(n):
  n = str(n)
  potencia = len(str(n))
  sum = 0
  for i in range(potencia):
    sum += pow(int(n[i]),potencia)
  return sum == int(n)

