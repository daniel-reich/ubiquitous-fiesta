
def fib_str(n, txt):
  
  Sequence = []
  Sequence.append(txt[-2])
  Sequence.append(txt[-1])
  
  String = txt[0] + ", " + txt[1]
  Steps = 2
  
  while (Steps < n):
    New = Sequence[-1] + Sequence[-2]
    Sequence.append(New)
    String = String + ", " + New
    Sequence = Sequence[1:]
    Steps += 1
    
  return String

