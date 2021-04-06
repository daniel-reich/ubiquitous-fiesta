
def centroid(x1, y1, x2, y2, x3, y3):
  try: 
    if x1/y1 == x2/y2 == x3/y3: return False
    else: return (round((x1 + x2 +x3)/3,2),round((y1 + y2 +y3)/3,2)) 
  except ZeroDivisionError:
    if x1 == x2 == x3 == 0 or y1 == y2 == y3 == 0: return False
    else: return (round((x1 + x2 +x3)/3,2),round((y1 + y2 +y3)/3,2))

