
def complete_binary(s):
  t = len(s) % 8
  return s if t == 0 else s.zfill(len(s) + 8 - t)

