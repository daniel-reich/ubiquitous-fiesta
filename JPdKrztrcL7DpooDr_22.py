
def collatz(n):
  seq = [n]
  while n != 1:
    if n % 2:
      n = (n * 3) + 1
    else:
      n /= 2
    seq.append(n)
  return [len(seq) - 1, max(seq)]

