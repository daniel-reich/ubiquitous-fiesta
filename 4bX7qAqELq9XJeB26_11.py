
def to_camel_case(txt):
  return ''.join( '' if txt[i] in '_-' else txt[i].upper() if txt[i-1] in '_-' else txt[i] for i in range(len(txt )))

