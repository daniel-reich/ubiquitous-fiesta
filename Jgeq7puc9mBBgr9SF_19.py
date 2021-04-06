
def complete_binary(s):
  return s if len(s)%8 == 0\
          else '0'*(8- len(s)) + s if len(s) < 8\
          else '0'*(8-len(s)%8) +s

