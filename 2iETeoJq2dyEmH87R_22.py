
squares=[0]
def count_digits(n, d):
  global squares
  if len(squares)<n:
    for i in range(len(squares),n+1):
      squares.append(i**2)
  return "".join(map(str,squares[:n+1])).count(str(d))

