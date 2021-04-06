
def cards_needed(n):
  
  if n < 0:
    return 'invalid'
    
  seq = [0]
  dif = 2
  current_step = 0
​
  while current_step < n and current_step < 1000:
    seq.append(seq[-1] + dif)
    dif += 3
    current_step += 1
​
  return seq[-1]

