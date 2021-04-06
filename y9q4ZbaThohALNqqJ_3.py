
def squares_sum(n):
  return any(
    (n - k ** 2) ** 0.5 % 1 == 0
    for k in range(int(n ** 0.5) + 1)
  )

