
def wrap_around(txt, o):
  return txt[o%len(txt):] + txt[:o%len(txt)]

