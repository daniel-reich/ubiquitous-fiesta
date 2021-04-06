
def decrypt(lst):
  return [chr(i + 96).upper() for i in range(1, 27) if i not in lst][0]

