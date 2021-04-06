
import datetime
​
def less_than_10(num):
  if num < 10:
    return '0' + str(num)
  else:
    return str(num)
​
def is_palindrome(time):
  str_time_1 = time.strftime('%H:%M:%S')
  return str_time_1 == str_time_1[::-1]
​
def palindrome_time(lst):
  count = 0
  time_1_str = less_than_10(lst[0]) + ':' + less_than_10(lst[1]) + ':' + less_than_10(lst[2])
  time_2_str = less_than_10(lst[3]) + ':' + less_than_10(lst[4]) + ':' + less_than_10(lst[5])
  time1 = datetime.datetime.strptime(time_1_str, '%H:%M:%S')
  time2 = datetime.datetime.strptime(time_2_str, '%H:%M:%S')
  if is_palindrome(time1) or (time1 == time2): count += 1
  while time1 != time2:
    time1 = time1 + datetime.timedelta(0, 1)
    if is_palindrome(time1):
      count += 1
  return count

