
def reverse_and_not(i):
  str1 = str(i)
  str1length = len(str1)
  str2 = str1[str1length::-1]
  i2 = int(str2+str1)
  return i2

