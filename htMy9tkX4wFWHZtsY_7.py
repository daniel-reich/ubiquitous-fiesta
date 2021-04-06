
import datetime
def palindrome_time(lst):
  ts = datetime.datetime(100, 1, 1, lst[0], lst[1], lst[2])
  end = datetime.datetime(100, 1, 1, lst[3], lst[4], lst[5])
  cnt = 0
  
  while ts <= end:
    tstr = ts.strftime("%H:%M:%S")
    cnt += tstr == tstr[::-1]
    ts += datetime.timedelta(0, 1)
  return cnt

