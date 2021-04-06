
def decrypt(lst):
  alpa = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  return ''.join(alpa[x] for x in range(1, 26) if x not in lst)

