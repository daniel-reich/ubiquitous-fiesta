
def sun_loungers(beach):
  ret = 0
  beach = list(beach)
  if beach[0]=='0':
    if (len(beach)>1 and beach[1]!='1') or len(beach)==1:
      beach[0]='1'
      ret+=1
  if beach[-1]=='0':
    if beach[-2]!='1':
      beach[-1]='1'
      ret+=1
  for i in range(1,len(beach)-1):
    if beach[i]=='0' and beach[i-1]=='0' and beach[i+1]=='0':
      beach[i]='1'
      ret+=1
  return ret

