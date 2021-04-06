
def binary_conversion(txt):
  txt=[txt[i:i+8] for i in range(0, len(txt),8)]
  ans=[]
  for i in txt:
    ans.append(chr(int(i,2)))
  return ''.join(ans)

