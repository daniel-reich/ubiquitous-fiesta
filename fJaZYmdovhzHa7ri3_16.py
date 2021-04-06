
def max_collatz(num):
  seq = []
  while num != 1:
    seq.append(num)
    num = num // 2 if num % 2 == 0 else num * 3 + 1
  return max(seq) if seq else 1

