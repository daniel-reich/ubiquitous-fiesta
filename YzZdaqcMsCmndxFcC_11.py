
def centroid(x1, y1, x2, y2, x3, y3):
  try: 
    if ((y2-y1)/(x2-x1)) == ((y3-y1)/(x3-x1)): return False
  except: pass
  return round((x1+x2+x3)/3, 2), round((y1+y2+y3)/3, 2)

