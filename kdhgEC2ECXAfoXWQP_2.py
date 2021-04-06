
def transpose_matrix(mtx):
 output=''
 i=0
 while i < len(mtx[0]):
  for k in range(0,len(mtx)):
   output+=mtx[k][i]
   if i != len(mtx[0])-1 or k != len(mtx)-1:
    output+=' '
  i+=1
 return output

