
def edabit_in_string(txt):
  strn,cur = "edabit",0
  for x in txt:
    if x == strn[cur]:cur += 1
    if cur == len(strn):return "YES"
  return "NO"

