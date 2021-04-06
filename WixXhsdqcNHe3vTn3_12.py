
def how_bad(n):
  l = ["Evil", "Odious", "Pernicious"]
  s = str(bin(n)).count('1')
  prime = all(n % x != 0 for x in range(2, n - 1))
  prime_s = all(s % x != 0 for x in range(2, s - 1)) if s >1 else False
  i = []
  if prime or prime_s: i.append(2)
  if s%2 == 0: i .append(0)
  if s%2 ==1: i.append(1)
  return [l[x] for x in sorted(i)]

