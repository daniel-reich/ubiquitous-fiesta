
def trace_word_path(word, grid):
  indices = [[] for k in range(len(word))]
  def neighbors(i,j):
    lst = []
    for a,b in zip([i-1,i,i,i+1],[j,j-1,j+1,j]):
      if min(a,b) >= 0 and a < len(grid) and b < len(grid[0]):
        lst.append((a,b))
    return lst
  def letters(i,j):
    return list(map(lambda x: grid[x[0]][x[1]],neighbors(i,j)))
  def is_valid(i,j,k):
    if k > 0 and not word[k-1] in letters(i,j):
        return False
    else:
      try:
        return word[k+1] in letters(i,j)
      except IndexError:
        return True
  #loop through to find valid indices 
  for k in range(len(word)):
    for i in range(len(grid)):
      for j in range (len(grid[0])):
        if grid[i][j] == word[k]:
          if is_valid(i,j,k):
            indices[k].append((i,j))
    if len(indices[k]) == 0:
      return 'Not present'
    elif len(indices[k]) == 1:
      indices[k] = indices[k][0]
  #check for duplicates 
  for k in range(0,len(word)):
    if isinstance(indices[k],list):
      indices[k] = list(filter(lambda x: not x in indices,indices[k]))      
      if len(indices[k]) == 1:
        indices[k] = indices[k][0]
      elif len(indices[k]) == 0:
        return 'Not present'
  #remaining indices
  for k in range(1,len(word)-1):
    if isinstance(indices[k],list):
      if isinstance(indices[k-1],tuple) and isinstance(indices[k+1],tuple):
        if (indices[k-1][0],indices[k+1][1]) in indices[k]:
          indices[k] = (indices[k-1][0],indices[k+1][1])
        elif (indices[k+1][0],indices[k-1][1]) in indices[k]:
          indices[k] = (indices[k+1][0],indices[k-1][1])
        elif indices[k+1][0] == indices[k-1][0]:
          indices[k] = (indices[k+1][0],(indices[k-1][1] + indices[k+1][1])//2)
        elif indices[k+1][1] == indices[k-1][1]:
          indices[k] = ((indices[k-1][0] + indices[k+1][0])//2,indices[k+1][1])
        else:
          return 'Not present'
  #check for duplicates again
  for k in range(0,len(word)):
    if isinstance(indices[k],list):
      indices[k] = list(filter(lambda x: not x in indices,indices[k]))      
      if len(indices[k]) == 1:
        indices[k] = indices[k][0]
      elif len(indices[k]) == 0:
        return 'Not present'
  return indices

