
def validate_binary(b):
  return not bool(sum(int(i) for i in b)%2)

