
import re
def color_conversion(h):
  if type(h)==str:
    if 'g' not in h:
      if h[0]=='#' and len(h)==7:
        A=['0x'+h[1:][i:i+2] for i in range(0,len(h[1:]),2)]
      elif h[0]!='#' and len(h)==6:
        A=['0x'+h[i:i+2] for i in range(0,len(h),2)]
      else:
        return "Invalid input!"
      d={'r':int(A[0],16), 'g':int(A[1],16), 'b':int(A[2],16)}
      return d
    else:
      return "Invalid input!"
  else:
    if all(0<=h[x]<=255 for x in h):
      return '#{}{}{}'.format(hex(h['r'])[2:].zfill(2), hex(h['g'])[2:].zfill(2), hex(h['b'])[2:].zfill(2))
    else:
      return "Invalid input!"

