
def collect(s, n):
  
  Blocks = []
  
  Start = 0
  Finish = n
  Length = len(s)
  
  while (Finish <= Length):
    Batch = s[Start:Finish]
    Blocks.append(Batch)
    Start += n
    Finish += n
  
  Answer = sorted(Blocks)
  return Answer

