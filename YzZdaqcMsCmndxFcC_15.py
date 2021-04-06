
def centroid(x1, y1, x2, y2, x3, y3):
  return (round((x1+x2+x3)/3,2),round((y1+y2+y3)/3,2)) if (y3+y2)/(x3+x2)!=(y1+y3)/(x1+x3) else False

