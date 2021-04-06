
def complete_binary(s):
  return s.rjust(len(s)+8-len(s)%8, '0') if len(s)%8 else s

