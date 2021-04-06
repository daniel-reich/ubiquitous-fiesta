
def same_upsidedown(ntxt):
  return ntxt == ''.join('6' if c=='9' else '9' if c=='6' else '0' for c in ntxt)[::-1]

