
def mini_peaks(lst):
 output=[]
 for i in range(1,len(lst)-1):
  if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
   output.append(lst[i])
 return output

