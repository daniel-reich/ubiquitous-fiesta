
def matrix_mult(m1, m2):
  arr=[]
  temp=[]
  temp.append(m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0])
  temp.append(m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1])
  arr.append(temp)
  temp=[]
  temp.append(m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0])
  temp.append(m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1])
  arr.append(temp) 
  return arr

