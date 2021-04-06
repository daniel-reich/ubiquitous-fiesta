
def perrin(n):
  def sequence(n):
    
    seq = [3, 0, 2]
    
    for num in range(0, n):
      n1 = seq[-3]
      n2 = seq[-2]
      
      s = n1 + n2
      seq.append(s)
    
    return seq
  
  seq = sequence(n)
  
  return seq[n]

