
#num=5
def diamond(num):
  array=[]
  matrix=[]
  if num%2==0:
      k=int(num/2)-1
      l=int(num/2)
      m=0
      for i in range(num-1):
          row=[]
          if m!=0:
              if i<int(num/2):
                  k-=1
                  l+=1
              else:
                  k+=1
                  l-=1
          m=1
​
          for j in range(num):
              if j==k or j==l:
                  row.append(1)
              else:
                  row.append(0)
          matrix.append(row)
      #print(matrix)
​
  if num%2!=0:
      k=int(num/2)
      l=int(num/2)
      for i in range(num):
          row=[]
          for j in range(num):
              if j==k or j==l:
                  row.append(1)
              else:
                  row.append(0)
​
          if i<int(num/2):
              k-=1
              l+=1
          else:
              k+=1
              l-=1
          matrix.append(row)
​
  if sum(matrix[0])>1:
      array.append(matrix)
      array.append('good cut')
  elif sum(matrix[0])==1:
      array.append(matrix)
      array.append('perfect cut')
  return array

