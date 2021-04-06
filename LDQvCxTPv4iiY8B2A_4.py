
def same_upsidedown(ntxt):
  flipped = ''.join('9' if x=='6' else '6' if x=='9' else x for x in ntxt)
  return flipped==ntxt[::-1]

