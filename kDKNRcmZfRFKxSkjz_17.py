
def unmix(txt):
  arr = []
  for i in range(0,len(txt),2):
    arr.append(txt[i:i+2][::-1])
  return "".join(arr)

