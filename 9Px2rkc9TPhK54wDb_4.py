
def ecg_seq_index(n):
  seq = [1, 2]
  while n not in seq:
    i = min(seq)
    while i in seq or all(f not in fact(seq[-1]) for f in fact(i)):
      i += 1
    seq += [i]
  return len(seq) - 1
  
def fact(n):
  return [i for i in range(2, n+1) if not n % i]

