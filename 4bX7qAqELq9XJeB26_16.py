
import re
def to_camel_case(txt):
  A=re.split('[-_]', txt)
  B=[x.capitalize() for x in A[1:]]
  C=[A[0]]+B
  return ''.join(C)

