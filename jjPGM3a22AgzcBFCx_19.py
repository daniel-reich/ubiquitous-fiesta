
def decrypt(lst):
  for i in range(1,27):
    if i not in lst:
      return chr(i+64)

