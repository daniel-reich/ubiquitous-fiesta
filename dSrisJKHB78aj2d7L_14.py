
def triangle(perimeter,area):
  B=[]
  for i in range(1,perimeter-1):
    for j in range(1,perimeter-1):
      if type(((perimeter/2)*((perimeter/2)-i)*((perimeter/2)-j)*((perimeter/2)-(perimeter-i-j)))
**(1/2))!=complex and round(((perimeter/2)*((perimeter/2)-i)*((perimeter/2)-j)*((perimeter/
2)-(perimeter-i-j)))**(1/2), 5)==area:
        if sorted([i,j,perimeter-i-j]) not in B and perimeter-i-j>0:
          B.append(sorted([i,j,perimeter-i-j]))
  return B

