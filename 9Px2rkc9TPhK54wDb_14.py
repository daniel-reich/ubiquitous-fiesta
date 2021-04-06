
def ecg_seq_index(n):
  seq = [1, 2]
  
  while n not in seq:
    
    a, b = 3, seq[-1]
    
    while not any(a%i==0==b%i for i in range(2, min(a, b)+1)) or a in seq:
      a += 1
    seq.append(a)
    
  return seq.index(n)

