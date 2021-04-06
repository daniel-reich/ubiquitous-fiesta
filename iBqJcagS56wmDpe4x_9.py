
import math
def vol_shell(r1, r2):
     a=abs((4/3)*math.pi*((r1**3)-(r2**3)))
     return round(a,3)
print(vol_shell(3,3))

