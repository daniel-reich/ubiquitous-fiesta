
def current_streak(today, lst):
  counter, count = 0, 0 
  for dates in lst:
    if dates["date"] == today:
      count += 1
      x = "".join(dates["date"].split("-"))
      y = lst.index(dates)
      while True:
        if int(x) - 1 == int("".join(lst[y - 1]["date"].split("-"))):
          counter += 1
          x = "".join(lst[y - 1]["date"].split("-"))
          y -= 1
        else: return counter + 1
  if count == 0: return 0

