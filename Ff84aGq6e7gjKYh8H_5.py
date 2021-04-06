
def minutes_to_seconds(time):
  import re
  x=re.sub(':','',time)
  if  int(x[-2:])>=60:
    return False
  else:
    return int(x[:-2:])*60+int(x[-2:])

