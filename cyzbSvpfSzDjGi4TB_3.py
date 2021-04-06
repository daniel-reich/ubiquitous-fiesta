
def harmonic(n):
  not_answer = 0
  for i in range(1, n + 1):
    not_answer += 1 / i
  return round(not_answer, 3)

