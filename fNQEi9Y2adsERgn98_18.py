
def perimeter(lst):
  [x1,y1],[x2,y2],[x3,y3]=lst
  return round(((x2-x1)**2+(y2-y1)**2)**.5+((x3-x1)**2+(y3-y1)**2)**.5+((x3-x2)**2+(y3-y2)**2)**.5,2)

