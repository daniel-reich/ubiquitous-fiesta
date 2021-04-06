
def how_many_times(msg):
  sum=0
  for i in range(0,len(msg)):
    sum= sum + ord(msg[i])-96
  return sum

