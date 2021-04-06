
def license_plate(code, group):
  code = ''.join([i for i in code.upper() if i!='-'])
  if len(code)<=group:
    return code
  return license_plate(code[:-group],group)+'-'+code[-group:]

