
def reverse_case(txt):
  return ''.join(map(lambda x: x.upper() if x.islower() else x.lower(), txt))

