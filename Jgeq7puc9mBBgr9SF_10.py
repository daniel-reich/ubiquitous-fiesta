
def complete_binary(s):
  return s[:len(s)%8].zfill(8) + s[len(s)%8:] if len(s)%8 else s

