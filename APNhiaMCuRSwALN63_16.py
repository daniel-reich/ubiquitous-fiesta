
def almost_palindrome(txt):
  new_txt=txt[::-1]
  print(txt)
  print(new_txt)
  count=0
  for i in range(len(txt)):
    if txt[i]!=new_txt[i]: count+=1
  return count==2

