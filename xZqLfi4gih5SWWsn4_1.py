
import re
def license_plate(code, group):
  A=re.findall('\w', code)[::-1]
  B=[A[i:i+group][::-1] for i in range(0, len(A), group)][::-1]
  C=[''.join(x).upper() for x in B]
  return '-'.join(C)

