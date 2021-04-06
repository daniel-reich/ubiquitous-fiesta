
def recaman_index(n):
  seq = [0]
  length = 1
  while True:
    r = seq[-1] - length
    if r < 0 or r in seq:
      r = seq[-1] + length
    
    if r == n:
      return len(seq)
    seq.append(r) 
          
    length += 1

