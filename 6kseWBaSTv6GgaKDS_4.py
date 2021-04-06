
def next_letters(w):
  if w=="": return "A"
  lst=[ord(i)-64 for i in w]
  lst[-1]=lst[-1]+1
  for i in range(-1,-(len(lst)+1),-1):
   if lst[i]>26:
     try:lst[i-1]=lst[i-1]+1
     except:
      lst.insert(i, 0)
      lst[i - 1] = lst[i - 1] + 1
​
  return "".join([chr(i+64) if i <27 else chr((i%26)+64) for i in lst])

