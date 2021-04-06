
def hours_passed(time1, time2):
  amt1, pmt1, amt2, pmt2 = time1[-2:] == "AM", time1[-2:] == "PM", time2[-2:] == "AM", time2[-2:] == "PM"
  t1, t2 = 0 if int(time1.split(":")[0]) == 12 and amt1 else int(time1.split(":")[0]), int(time2.split(":")[0])
  return "no time passed" if time1 == time2 else \
    str(t2 - t1 if amt2 or (pmt1 and pmt2) else (t2 + 12) - t1) + " hours"

