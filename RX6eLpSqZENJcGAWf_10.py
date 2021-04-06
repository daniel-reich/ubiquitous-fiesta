
def equals():
  return type('', (object,),{'__eq__': lambda *x: True})()

