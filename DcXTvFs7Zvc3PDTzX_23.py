
def validate_binary(b):
  n = list(b[:-1]).count('1')
  if n % 2 == 0 and b[-1] == '0':
    return True
  elif n % 2 == 1 and b[-1] == '1':
    return True
  else:
    return False

