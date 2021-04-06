
def special_reverse_string(txt):
  rev=txt[::-1]
  print(txt)
  print(rev)
  ans=""
  j=0
  i=0
  while(i<len(txt)):
    print(txt[i])
    if(rev[j]==" "):
      j+=1
      continue
    if(txt[i].isupper()):
      ans=ans+rev[j].upper()
      j+=1
    elif(txt[i].islower()):
      ans=ans+rev[j].lower()
      j+=1
    elif(txt[i]==" "):
      ans=ans+" "
    else:
      ans=ans+rev[j].lower()
      j+=1
    i+=1
  print(ans)
  return ans

