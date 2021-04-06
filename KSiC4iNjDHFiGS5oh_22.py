
import re
def is_super_d(n):
  for d in range(2,10):
    res = d*n**d
    temp = re.findall("("+str(d)+")"+"{"+str(d)+"}", str(res))
    if len(temp) != 0:
      return 'Super-'+str(d)+ ' Number'
  return 'Normal Number'

