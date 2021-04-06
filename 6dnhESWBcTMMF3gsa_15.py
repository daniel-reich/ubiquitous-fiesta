
def stupid_addition(a, b):
  return str(a)+str(b) if type(a)==type(b) and type(a)==int else int(a)+int(b) if type(a)==type(b) and type(a)==str else None

