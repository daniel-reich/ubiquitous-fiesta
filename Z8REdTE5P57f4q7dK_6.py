
def collatz(n):
  seq = [n]
  while n != 1:
    if not n % 2:
      n *= 0.5
    else: n = n * 3 + 1
    seq.append(n)
  return (len(seq), max(seq))

