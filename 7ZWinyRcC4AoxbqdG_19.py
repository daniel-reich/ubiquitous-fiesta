
def fibo(n):
  
  if (n == 1) or (n == 2):
    return 1
  else:
    Sequence = [1,1]
    Steps = 2
    
    while (Steps < n):
      New = Sequence[-2] + Sequence[-1]
      Sequence.append(New)
      Sequence = Sequence[1:]
      Steps += 1
    
    return New

