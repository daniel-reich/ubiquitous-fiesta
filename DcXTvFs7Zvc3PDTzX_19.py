
def validate_binary(b):
  return (b.endswith('0'), b.endswith('1'))[b[:-1].count('1') % 2]

