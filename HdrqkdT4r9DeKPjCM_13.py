
def is_polygonal(n):
​
  class Polygonal:
​
    def __init__(self, sides):
      self.s = sides
    
    def centered(self, num):
​
      seq = [1]
      c = 0
      pl = 1
​
      while max(seq) < num+1 and c < 1000:
        c += 1
        to_add = max(seq) + (self.s * pl)
        seq.append(to_add)
        pl += 1
      
      if num not in seq:
        return False
      
      for n in range(len(seq)):
        t = seq[n]
        if t == num:
          return n
  
  if n == 1:
    return '0th of all'
    
  shapes = {}
​
  for num in range(3, 71110):
    shapes[num] = Polygonal(num)
  
  correct_shapes = []
​
  for side in shapes.keys():
    shape = shapes[side]
    test = shape.centered(n)
    if test != False:
      correct_shapes.append([side, test])
​
  if len(correct_shapes) == 0:
    return False
​
  exceptions = {1: 'st', 2: 'nd', 3: 'rd', 21: 'st'}
  correct_wordings = []
​
  for shape in correct_shapes:
    index = int(shape[1])
    gonal = int(shape[0])
​
    if index in exceptions.keys():
      cw = '{}{} {}-gonal number'.format(index, exceptions[index], gonal)
    else:
      cw = '{}th {}-gonal number'.format(index, gonal)
    
    correct_wordings.append(cw)
  
  return correct_wordings

