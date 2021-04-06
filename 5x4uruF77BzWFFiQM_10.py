
import math
def pH_name(pH):
  if 0<=math.floor(pH)<7 :
     return 'acidic'
  elif  math.floor(pH)==7:
     return 'neutral'
  elif 7<math.floor(pH)<14:
     return'alkaline'
  elif math.floor(pH)<0 or math.floor(pH)>0:
     return 'invalid'

