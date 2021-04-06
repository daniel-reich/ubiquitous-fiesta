
def happy(n):
  while True:
    txt = str(n)
    temp = 0
    for x in range(len(txt)):
      temp += int(txt[x]) * int(txt[x])
    if temp == 1: return True
    elif temp < 10: return False
    n = temp

