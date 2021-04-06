
def hours_passed(time1, time2):
  t1, t2 = int(time1[:-6]), int(time2[:-6])
  return 'no time passed' if time1==time2 else str(t2-t1)+' hours' if time1[-2:]==time2[-2:] else str(12 + t2-t1)+' hours'

