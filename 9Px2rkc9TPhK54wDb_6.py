
def ecg_seq_index(n):
  ecg = [1,2]
  x = 3
  while n not in ecg:
    if x in ecg:
      x += 1
    elif any([i in factors(ecg[-1]) for i in factors(x)]):
      ecg.append(x)
      x = 3
    else:
      x += 1
  return ecg.index(n)
    
def factors(n):
  return [i for i in range(2,n+1) if n%i == 0]

