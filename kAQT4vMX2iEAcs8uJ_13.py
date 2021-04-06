
def longest_7segment_word(lst):
  a=len(lst)
  cnt=0
  newStr=""
  maxLen=0
  for i in range(0,a):
    b=lst[i]
    c=len(b)
    for j in range(0,c):
      d=b[j]
      if(d in "kmvwx"):
        cnt=1
    if(cnt==0):
      if(c>maxLen):
          maxLen=c
          newStr=b
    cnt=0
  return newStr

