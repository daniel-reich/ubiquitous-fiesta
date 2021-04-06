
def cal(depth):
  minutes,count,climb = 0,0,0
  while climb < depth:
    climb += 5
    count += 1
    minutes += 1
    if count > 30:
      count = 0
      climb -= 30
      minutes += 10
  return minutes

