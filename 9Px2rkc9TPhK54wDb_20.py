
def ecg_seq_index(n):
  seq,rem = [1,2],[]
  i = 3
  while seq[-1] != n:
    br = False
    for k in rem:
      if not coprime(k,seq[-1]):
        seq.append(k)
        rem.remove(k)
        br = True
        break
    if not br:
      while coprime(i,seq[-1]):
        rem.append(i)
        i += 1
      seq.append(i)
      i += 1
  return len(seq)-1
  
def coprime(a,b):
  while b:
    a,b = b,a%b
  return a == 1

