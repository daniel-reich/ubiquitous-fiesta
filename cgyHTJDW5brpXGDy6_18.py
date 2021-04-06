
def hours_passed(time1, time2):
  if time1==time2:
    return "no time passed"
  time1_split = time1.split(':')
  time2_split = time2.split(':')
  if time1_split[1]==time2_split[1]:
    return str(int(time2_split[0])-int(time1_split[0]))+" hours"
  else:
    return str(int(time2_split[0])-int(time1_split[0])+12)+" hours"

