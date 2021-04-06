
def validate_binary(b):
  if b[-1] == '0':
    return not b[:-1].count('1') % 2
  return bool(b[:-1].count('1') % 2)

