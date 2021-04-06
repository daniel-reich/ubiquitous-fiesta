
def spiral_order(matrix):
  outputlist=[]
  cleared=0
  end=len(matrix)
  while any(matrix):
    outputlist.extend(matrix[cleared])
    matrix[cleared].clear()
    cleared+=1
    n=1
    while n<end:
      outputlist.append(matrix[n].pop())
      n+=1
    while matrix[end-1]:
      outputlist.append(matrix[end-1].pop())
    n-=1
    while n>=1:
      outputlist.extend(matrix[n])
      n-=1
    return outputlist

