
import re
def sun_loungers(beach):
  if beach == "0":
    return 1
  n = 0
  if beach[:2] == "00":
    beach = "1" + beach[1:]
    n += 1
  if beach[-2:] == "00":
    beach = beach[:-1] + "1"
    n += 1
  res = sum([ (len(x)-1)//2  for x in re.findall(r"(0+)",beach)])
  return res +n

