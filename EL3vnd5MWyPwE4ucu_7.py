
class Fibonacci:
  
  def __init__(self):
    self.seq = [0, 1, 1]
  
  def advance_to(self, goal):
    while len(self.seq) <= goal:
      self.seq.append(self.seq[-2] + self.seq[-1])
    return True
  
  def number_yet_found(self, number):
    return number <= len(self.seq)
    
  def retrieve(self, index):
    return self.seq[index]
​
f = Fibonacci()
​
def fibonacci(n):
  if f.number_yet_found(n) == False:
    f.advance_to(n)
  return str(f.retrieve(n))

