
def hours_passed(time1, time2):
  x = int(time1.split(':')[0]) + 12 if time1[-2] == 'P' else 0 if int(time1.split(':')[0]) == 12 else int(time1.split(':')[0])
  y = int(time2.split(':')[0]) + 12 if time2[-2] == 'P' else int(time2.split(':')[0])
  return str(y - x) + " hours" if y - x != 0 else "no time passed"

