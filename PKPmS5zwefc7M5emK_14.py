
def missing_angle(a1, a2):
  b=(a1+a2)
  a3=180-b
  if a3>90:
   return "obtuse"
  elif a3<90:
   return "acute"
  return "right"

