
def ecg_seq_index(n):
  seq = [1,2]
  while n not in seq:
    i = 0
    while True:
      if i not in seq:
        if get_factors(i) & get_factors(seq[-1]):
          seq.append(i)
          break
      i += 1
  return len(seq)-1
​
def get_factors(n):
  s = {n}
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      s.add(i); s.add(n//i)
  return s

