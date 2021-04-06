
def complete_binary(s):
  return "{}{}".format((0 if len(s)%8==0 else 8-len(s)%8)*"0",s)

