
def spiral_order(matrix):
  el,out,go=len(matrix)*len(matrix[0]),[],1
  while len(out)!=el:
    if (go%4==1):
      for i in matrix[0]:
        out.append(i)
      del matrix[0]
    elif (go%4==2):
      for i in matrix:
        out.append(i[-1])
        del i[-1]
    elif (go%4==3):
      for i in matrix[-1][::-1]:
        out.append(i)
      del matrix[-1]
    elif (go%4==0):
      for i in matrix[::-1]:
        out.append(i[0])
        del i[0]
    go+=1
  return out

