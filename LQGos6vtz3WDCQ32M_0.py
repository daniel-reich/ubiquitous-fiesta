
def Kaprekar(n):
  
  class Number:
​
    def __init__(self, value):
      self.v = value
      self.l = [int(digit) for digit in str(self.v)]
      
      self.iterations = {0: self.v}
      self.num_of_iterations = 0
​
      self.repdigit = len(list(set(self.l))) == 1 and len(self.l) == 4
    
    def iterate(self):
​
      key = max(list(self.iterations.keys())) + 1
      lst = sorted(self.l)
​
      while len(lst) < 4:
        lst = [0] + lst
      
      minnum = ''.join([str(i) for i in lst])
      maxnum = ''.join([str(i) for i in list(reversed(lst))])
​
      iteration = int(maxnum) - int(minnum)
      striteration = str(iteration)
​
      while len(striteration) < 4:
        striteration = '0' + striteration
​
      self.iterations[key] = '{} - {} = {}'.format(maxnum, minnum, striteration)
      self.num_of_iterations += 1
      self.v = iteration
      self.l = [int(digit) for digit in str(self.v)]
​
      if self.v == 6174:
        return True
      else:
        return False
​
    def print(self):
​
      tr = '\n---------- The Mysterious Number 6174 ----------\n\nNumber of iterations: {}'.format(self.num_of_iterations) + '\n\nIterations:\n\n'
​
      for key in self.iterations.keys():
        if key != 0:
          tr += 'Iteration Nr. {}: {}\n'.format(key, self.iterations[key])
      
      tr += '\n------------------------------------------------'
​
      return tr
​
  number = Number(n)
  is_6174 = number.v == 6174
  repdigit = number.repdigit
​
  if repdigit == True:
    return "\n---------- The Mysterious Number 6174 ----------\n\nError, n cannot be a repdigit.\n\n------------------------------------------------"
​
  while is_6174 == False:
    is_6174 = number.iterate()
  
  return number.print()

