
def isbn13(txt):
 size = len(txt)
 if size==10 or size==13:
  if isbn10(txt) and len(txt)==10:
   sum = 0
   if txt[9]=="X":
    sum += 10
   else:
    sum += int(txt[9])
   nTxt = "978"+txt
   indx = 0
   while indx<12:
    if indx%2:
     sum+=3*int(nTxt[indx])
    else:
     sum+=int(nTxt[indx])
    indx+=1
   lstd = sum%10
   if lstd:
    if nTxt[12] == "X":
     sum = sum-10
    else:
     sum = sum-int(nTxt[12])
    lstd = 10-sum%10
    nTxt = nTxt[:12] + str(lstd)
    return nTxt
   else:
    return nTxt
  else:
   if size==13:
    if txt[12]=="X":
     sum = 10
    else:
     sum = int(txt[12])
    indx = 0
    while indx<12:
     if indx%2:
      sum+=int(txt[indx])*3
     else:
      sum+=int(txt[indx])
     indx+=1
    lstd = sum%10
    if lstd:
     return "Invalid"
    else:
     return "Valid"    
   else:
    return "Invalid"
 else:
  return "Invalid"
​
def isbn10(txt):
 sum = 0
 i = 0
 while i<9:
  sum+=int(txt[i])*(i+1)
  i+=1
 if txt[9]=="X":
  sum += 100
 else:
  sum += int(txt[9])*10
 if sum%11==0:
  return True
 else:
  return False

