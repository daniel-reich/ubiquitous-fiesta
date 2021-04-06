
def increment_string(n):
  if(n[len(n)-1]>='0' and n[len(n)-1]<='9'):
    num=''
    j=0
    for i in range(len(n)-1,0,-1):
      if(n[i].lower()>='a' and n[i].lower()<='z'):
        break
      else:
        num=n[i]+num
        j=i
    count=0
    while(num[0]=='0'):
      count+=1
      num=num[1:]
    num=int(num)+1
    if(len(str(num))<len(n[j:])):
      return n[0:j]+"0"*count+str(num)
    else:
      return n[0:j]+str(num)
  else:
    return n+"1"

