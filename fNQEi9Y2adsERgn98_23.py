
def perimeter(lst):
  x=pow((lst[0][0]-lst[1][0])**2+(lst[0][1]-lst[1][1])**2,0.5)
  y=pow((lst[0][0]-lst[2][0])**2+(lst[0][1]-lst[2][1])**2,0.5)
  z=pow((lst[1][0]-lst[2][0])**2+(lst[1][1]-lst[2][1])**2,0.5)
  return round(x+y+z,2)

