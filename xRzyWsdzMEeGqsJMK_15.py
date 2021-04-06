
def maskify(str):
  return (len(str) - 4) * '#' + str[-4::] if len(str) > 4 else str

