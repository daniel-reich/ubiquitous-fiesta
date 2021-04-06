
def daily_streak(l):
  return len(max("".join(map(str, l)).split("False"), key=len)) // 4

