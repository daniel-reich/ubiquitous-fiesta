
def hours_passed(time1, time2):
  if time1 == time2: 
    return "no time passed"
  t1, ampm1 = time1.split()
  t1 = int(t1.split(':')[0])
  if ampm1 == "PM":
    t1 += 12
  t2, ampm2 = time2.split()
  t2 = int(t2.split(':')[0])
  if ampm2 == "PM":
    t2 += 12
  return str(t2 - t1) + " hours"

