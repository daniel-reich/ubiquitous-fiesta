
def palindrome_time(lst):
  count = 0
  for t in range(lst[0]*3600 + lst[1]*60 + lst[2], lst[3]*3600 + lst[4]*60 + lst[5] + 1):
    txt = ("{:02d}" * 3).format(t // 3600, t // 60 % 60, t % 60)
    if txt == txt[::-1]:
      count += 1
  return count

