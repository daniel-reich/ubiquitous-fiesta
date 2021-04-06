
def minutes_to_seconds(time):
 res=(time).split(':',2)
 m=int(res[0])*60
 if int(res[1])>=60:
  return False
 return m+int(res[1])

