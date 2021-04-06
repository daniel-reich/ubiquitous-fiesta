
def validate_binary(b):
  return b.endswith('1' if b[:-1].count('1') % 2 else '0')

