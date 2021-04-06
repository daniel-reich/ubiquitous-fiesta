
def decrypt(lst):
  m = [i for i in range(1,26+1) if i not in lst]
  return chr(64 + m[0])

