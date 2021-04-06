
def hours_passed(time1, time2):
  time1 = time1.replace("12:00 AM", '00:00 AM')
  
  t1 = int(time1[:time1.index(':')]) + 12 if time1[-2:] == 'PM' else int(time1[:time1.index(':')])
  t2 = int(time2[:time2.index(':')]) + 12 if time2[-2:] == 'PM' else int(time2[:time2.index(':')])
  
  return '{} hours'.format(t2-t1) if t2 - t1 != 0 else "no time passed"

