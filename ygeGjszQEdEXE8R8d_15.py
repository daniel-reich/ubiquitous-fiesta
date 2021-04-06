
def row_1(m):
  return [i for i in range(len(m)) if 1 in m[i]][-1]
​
def move(mat):
  
  def clo(step):
    nonlocal mat
    r = len(mat)
    c = len(mat[0])
​
    if step in 'updown':
      i = row_1(mat)
      p = (i - 1, i + 1)[step == 'down']
      temp_row = mat[p % r]
      mat[p % r], mat[i] = mat[i], mat[p % r]
​
    if step in 'leftright':
      mat = list(zip(*mat))
      i = row_1(mat)
      p = (i - 1, i + 1)[step == 'right']
      temp_row = mat[p % c]
      mat[p % c], mat[i] = mat[i], mat[p % c]
      mat = list(list(r) for r in zip(*mat))
​
    return mat if step == 'stop' else clo
  
  return clo

