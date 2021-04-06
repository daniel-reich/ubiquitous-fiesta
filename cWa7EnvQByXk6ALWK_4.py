
def golden_ratio():
  it = 100
  it, root5, n = 100, 0, 5
  a, d = 2, 2
  for _ in range(100):
      root5 = 10 * root5 + d
      n = (n - a * d) * 100
      a = root5 * 20
      d = n // a
      if (a + d + 1) * (d + 1) <= n:
          d += 1
      a += d
  return "1.6" + str(root5 // 2)[2:]

