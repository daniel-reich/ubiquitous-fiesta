
def palindrome_time(lst):
  import datetime as dt
  start = dt.datetime(1,1,1, lst[0], lst[1], lst[2])
  end = dt.datetime(1,1,1, lst[3], lst[4], lst[5])
  count = 0
  t = start
  while t <= end:
    if str(t.time()) == str(t.time())[::-1]:
      count += 1
    t += dt.timedelta(seconds=1)
  return count

