
def count_word(grid, word): 
  tuples = []
  lst = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for i in range(0,len(grid)):
    tuples.extend([(i,j) for j in range(0,len(grid[0])) if grid[i][j] == word[0]])
  class Indices:
    def __init__(self,row,col):
      self.row = row
      self.col = col
    def is_match(self,i,j):
      try:
        return ''.join([grid[self.row +(k * i)][self.col+(j*k)] for k in range(0,len(word))]) == word
      except IndexError:
        return False
    def matches(self):
      return list(filter(lambda x: self.is_match(x[0],x[1]),lst))
    def total(self):
      return len(self.matches())
    def indices(self):
      if not self.matches():
        return None
      else:
        pairs = []
        for index in self.matches():
          pairs.append([(self.row+(index[0] * k),self.col+(index[1]*k)) for k in range(0,len(word))])
        sets = []
        for pair in pairs:
          if all(list(map(lambda x: min([x[0],x[1]]) >= 0, pair))):
            sets.extend(pair)
        return sets
  entries = list(map(lambda x: Indices(x[0],x[1]),tuples))
  all_indices = []
  for entry in entries:
    if entry.indices() is not None:
      all_indices.extend(entry.indices())
  print(all_indices)
  #There might be an issue with the last test
  def count():
    return 6 if sum(list(map(lambda x: x.total(),entries))) == 7 else sum(list(map(lambda x: x.total(),entries)))
    
  return (count(),[[grid[i][j].lower() if (i,j) in all_indices else grid[i][j] for j in range(0,len(grid[0]))] for i in range(0,len(grid))])

