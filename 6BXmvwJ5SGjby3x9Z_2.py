
from datetime import datetime
​
def hours_passed(time1, time2):
  d = datetime.strptime(time2, "%I:%M %p") - datetime.strptime(time1, "%I:%M %p")
  d = d.seconds // 3600
  return "%d hours" % d if d else "no time passed"

