
def complete_binary(s):
  
  return '0' * (8 - (len(s) % 8)) + s if len(s) % 8 != 0 else s

