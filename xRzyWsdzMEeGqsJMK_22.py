
def maskify(txt):
  hashes = len(txt[:-4])
  return ''.join(['#'*len(txt[:-4]),txt[-4:]])

