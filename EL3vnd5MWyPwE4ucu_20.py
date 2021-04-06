
def fibonacci(n):
  
  Steps = 2
  
  Sequence = [1,1]
  
  while (Steps < n):
    New = Sequence[0] + Sequence[1]
    Sequence.append(New)
    Sequence = Sequence[1:]
    Steps += 1
  
  return str(New)

