
def modify(txt):
  txt = txt[::-1]
  num = ""
  for i in txt:
    num += str(ord(i)-96)
  num = int(str(bin(int(num)))[2:])
  return num

