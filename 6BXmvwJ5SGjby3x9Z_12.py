
def hours_passed(time1, time2):
  if time1 == time2:
    return "no time passed"
  time1 = time1 if time1 != "12:00 AM" else "0:00 AM"
  time2 = time2 if time2 != "12:00 AM" else "0:00 AM"
  hour1 = int(time1.split(":")[0]) if time1[len(time1) - 2] == "A" else int(time1.split(":")[0]) + 12
  hour2 = int(time2.split(":")[0]) if time2[len(time2) - 2] == "A" else int(time2.split(":")[0]) + 12
  return str(hour2 - hour1) + " hours"

