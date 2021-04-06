
import re
def license_plate(s, n):
  A=re.findall('\w', s)[::-1]
  B=[''.join(A[i:i+n])[::-1] for i in range(0, len(A), n)][::-1]
  C=[x.upper() for x in B]
  return '-'.join(C)

