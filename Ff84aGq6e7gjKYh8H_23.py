
def minutes_to_seconds(time):
  lst = time.split(":")
  if(int(lst[1])>= 60):
    return False
  sum = int(lst[0])*60
  sum += int(lst[1])
  return sum

