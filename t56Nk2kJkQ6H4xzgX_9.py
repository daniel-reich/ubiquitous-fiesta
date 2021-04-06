
def swap_xy(txt):
  import re
  l=re.sub("[\(\),]","",txt).split()
  return re.sub("[\[\]]","",str([(int(l[i+1]),int(l[i])) for i in range(0,len(l),2)]))

