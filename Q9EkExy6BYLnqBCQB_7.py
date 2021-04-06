
def wrap_around(string, offset):
  s=len(string)
  o=abs(offset)%s
  if offset>=0:
    return string[o:]+string[:o]
  else:
    return string[(-1)*o:]+string[:(-1)*o]

