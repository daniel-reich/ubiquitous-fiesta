
def validate_binary(b):
  return b[:-1].count('1')%2==int(b[-1])

