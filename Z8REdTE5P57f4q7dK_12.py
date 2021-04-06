
def collatz(n):
  sequence = [n]
  if n < 1:
    return []
  while n > 1:
    if not n % 2:
      n /= 2
    else:
      n = n * 3 + 1
    sequence.append(int(n))
  return (len(sequence), max(sequence))

