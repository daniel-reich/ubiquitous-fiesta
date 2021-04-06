
from itertools import dropwhile,takewhile
def palindrome_time(lst):
  def string(h,m,s):
    s1 = str(m).rjust(2, '0')
    s2 = str(s).ljust(2,'0')
    return int(str(h) + s1 + s2)
  hours = list(filter(lambda x: x % 10 < 6, range(24)))
  minutes = list(range(0,56,11))
  seconds = list(map(lambda x: int(str(x)[::-1]),hours))
  count = 0
  for hour,second in zip(hours,seconds):
    if hour >= lst[0] and hour <= lst[3]:
      for minute in minutes:
        if string(hour,minute,second) >= string(lst[0],lst[1],lst[2]):
          if string(hour,minute,second) <= string(lst[3],lst[4],lst[5]):
            count += 1
​
  return count

