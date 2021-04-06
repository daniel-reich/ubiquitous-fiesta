
def semiprimes(n):
  semi = []
  semi_nonsq = []
  for num in range(4, n):
    total = 0
    for f in range(2, num):
      if f*f > num:
        if total == 1:
          semi_nonsq.append(num)
          semi.append(num)
        break
      if num % f == 0:
        if f*f == num:
          semi.append(num)
          break
        if num % (f*f) == 0:
          break
        total += 1
        if total > 1:
          break
  return semi, semi_nonsq

