
def p(c,g):
  return c if len(c)<=g else p(c[0:len(c)-g],g)+'-'+c[len(c)-g:]
def license_plate(code,group):
  codep=code.replace('-','').upper()
  return p(codep,group)

