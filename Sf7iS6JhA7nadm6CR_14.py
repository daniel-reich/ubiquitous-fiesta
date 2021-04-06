
SEQ = [1, 10, 9, 12, 3, 4] * 3
​
def seq_p_sum(n):
  tot = 0
  
  for a, b in (zip(list(map(int, str(n)))[::-1], SEQ)):
    tot += a * b
​
  return tot
​
def divisibility_rule(n):
  while n != seq_p_sum(n):
    n = seq_p_sum(n)
​
  return n

