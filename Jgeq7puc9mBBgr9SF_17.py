
def complete_binary(s):
  return '0' * (8 - len(s) % 8 if len(s) % 8 > 0 else 0) + s

