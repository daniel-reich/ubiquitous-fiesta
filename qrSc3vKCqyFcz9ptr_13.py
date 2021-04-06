
def sum_round(num):
  num = list(map(int, str(num)))[::-1]
  return ' '.join(str(n*10**i) for i, n in enumerate(num) if n)

