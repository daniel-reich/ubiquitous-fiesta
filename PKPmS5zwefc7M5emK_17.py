
def missing_angle(angle1, angle2):
 if 180-angle1-angle2>90:
         i = "obtuse"
 elif (180-angle1-angle2)<90:
         i = "acute"
 else:
         i = "right"
 return i

