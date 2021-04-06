
import re
def hours_passed(time1, time2):
  t1=re.split('[:\s]', time1)
  t2=re.split('[:\s]', time2)
  delta=int(t2[0])-int(t1[0]) if t1[-1]==t2[-1] else int(t2[0])-int(t1[0])+12
  if delta:
    return "{} hours".format(delta)
  return  "no time passed"

