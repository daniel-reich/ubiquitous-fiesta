
def split(n):
  pos = [i for i in range(1, n + 1)]
  res = [(n / i) ** i for i in pos]
  return (round(max(res), 1))

