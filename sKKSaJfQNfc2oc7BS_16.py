
def sle(m):
  det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
  xdet = m[0][2]*m[1][1]-m[0][1]*m[1][2]
  ydet = m[0][0]*m[1][2]-m[0][2]*m[1][0]
  try: return (xdet/det,ydet/det)
  except: return False

