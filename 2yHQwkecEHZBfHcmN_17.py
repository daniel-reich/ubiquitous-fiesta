
def progress_days(runs):
 cnt=0
 for i in range(1,len(runs)):
   if runs[i-1]<runs[i]:
     cnt+=1
 return cnt

