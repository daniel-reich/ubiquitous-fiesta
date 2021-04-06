
def replace(txt, r):
  return "".join(["#" if x in list(map(chr, range(ord(r[0]), ord(r[-1])+1)))  else x for x in txt])

