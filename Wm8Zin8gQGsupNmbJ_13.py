
def binary_conversion(txt):
  lst = [txt[x:x+8] for x in range(0,len(txt),8)]
  ans = []
  for x in lst:
    ans.append(chr(int('0b'+str(x),2)))
  return ''.join(ans)

