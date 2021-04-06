
def calc(s):
 lst = []
 total = 0
 total2 = 0
 for x in s:
  lst.append(str(ord(x)))
 for z in ''.join(lst):
  total += int(z)
 for t in ''.join(lst).replace('7','1'):
  total2 += int(t)
 return abs(total - total2)

