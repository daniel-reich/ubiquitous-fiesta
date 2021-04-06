
def check(grid,row,col,word,index=0,dirrow=0,dircol=0):
  if row >= 8 or col >= 8 or index >= len(word):
    return False
  else:
    if grid[row][col] != word[index]:
      return False
    else:
      if index == len(word)-1:
        return True
      elif dirrow == 0 and dircol == 0:
        return check(grid,row-1,col-1,word,index+1,-1,-1) or check(grid,row-1,col,word,index+1,-1,0) or check(grid,row-1,col+1,word,index+1,-1,1) or check(grid,row,col-1,word,index+1,0,-1) or check(grid,row,col+1,word,index+1,0,1) or check(grid,row+1,col-1,word,index+1,1,-1) or check(grid,row+1,col,word,index+1,1,0) or check(grid,row+1,col+1,word,index+1,1,1)
      else:
        return check(grid,row+dirrow,col+dircol,word,index+1,dirrow,dircol)
​
def word_search(letters, words):
  grid = list(map(lambda x: list(letters[x:x+8]), range(0,64,8)))
  found = []
  for row in range(8):
    for col in range(8):
      for word in words:
        if word not in found:
          if check(grid,row,col,word.upper()):
            found.append(word)
  return len(found) == len(words)

