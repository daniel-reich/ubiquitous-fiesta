
def how_many_times(msg):
  sum=0
  for m in msg:
    if m.islower():
      sum+=ord(m)-96
    elif m.isupper():
      sum+=ord(m)-64
  return sum

