
def ecg_seq_index(n):
  def factor(n):
​
    factors = []
    for num in range(1, n + 1):
      r = n % num
​
      if r == 0:
        factors.append(num)
    
    return factors
  
  seq = [1, 2]
​
  while int(seq[-1]) != n:
   
    n1 = int(seq[-1])
​
    factor_goal = factor(n1)
​
    for number in range(2, 1000000000000000):
      if number in seq:
        continue
      factor_test = factor(number)
​
      correct = False
​
      for item in factor_test:
        if item in factor_goal:
          if item != 1:
            correct = True
            break
      
      if correct == True:
        seq.append(number)
        break
    
  return len(seq) - 1

