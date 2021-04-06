
def get_slope(pt1,pt2):
  (pt1x , pt1y) = pt1
  (pt2x , pt2y) = pt2
  if (pt2y - pt1y) == 0:
    return 1
  slope = (pt2x - pt1x)/(pt2y - pt1y)
  return slope
​
def is_midpt_90_deg(pt1,pt2,pt3):
  slope1 = get_slope(pt1,pt2)
  slope2 = get_slope(pt2,pt3)
  if slope1 is None or slope2 is None:
    return False
  if  (slope1 == 1 and slope2 == 0)  \
      or (slope1 == 0 and slope2 == 1):
    return True
  if (slope2 != 0 and slope1 == 1/-(slope2)) \
    or (slope1 != 0 and slope2 == 1/-(slope1)):
    return True
  return False
​
def getPoint(value):
  try:
    pt_temp = value.replace("(","") \
                      .replace(")","")  \
                      .replace(" ","") \
                      .split(',')
    pt = (int(pt_temp[0]) , int(pt_temp[1]))
    return pt
  except:
    return None
    
def is_rectangle(coordinates):
  if len(coordinates) < 4:
    return False
  points = []
  for coord in coordinates:
      tempPt = getPoint(coord)
      if tempPt is None:
        return False
      points.append(tempPt)
  i = 0
  if is_midpt_90_deg(points[i],points[i+1],points[i+2]) \
    and is_midpt_90_deg(points[i+1],points[i+2],points[i+3]) \
    and is_midpt_90_deg(points[i+2],points[i+3],points[i]):
      return True
  return False

