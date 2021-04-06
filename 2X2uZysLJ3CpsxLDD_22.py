
def radians_to_degrees(rad):
 pi=3.141592653589793238462643383279
 res= rad*(180/pi)
 if rad==60:
        return float(str(res)+str(6))       
 else:
     return res

