
def hours_passed(time1, time2):
  if time1==time2: return 'no time passed'
  a=[int(time1[:-6]),int(time2[:-6])]
  if "PM" in time1:a[0]+=12
  if "PM" in time2:a[1]+=12
  if time1=="12:00 AM":a[0]=0 
  return str(a[1]-a[0])+' hours'

