
def triangle(perimeter,area):
  print(perimeter,area)
  result=[]
  for i in range(perimeter//2):
    a =i+1
    b_c = perimeter - a
    for j in range(b_c):
      b= j + 1
      c= b_c - b 
      
      P=a+b+c
      p=(P)/2
      A= (p*(p-a)*(p-b)*(p-c))**0.5
      if not(isinstance(A, complex )) and round(A,5) == area :
        r=[a,b,c]
        r.sort()
        if r not in result:
          result.append(r)
  if len(result)>1:
    result.sort(key = lambda x: x[0])
  return (result)

