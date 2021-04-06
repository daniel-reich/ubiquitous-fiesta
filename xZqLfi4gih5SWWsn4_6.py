
import re
def license_plate(code, n):
  code = code.upper()
  code = re.sub('-','',code)
  if len(code)<=n:
    return code
  return license_plate(code[:-n],n) + '-' +code[-n:]

