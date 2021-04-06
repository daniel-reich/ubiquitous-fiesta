
def complete_binary(s):
  if not len(s) % 8:
    return s
  return "0"*(8-len(str(s)) % 8) + str(s)

