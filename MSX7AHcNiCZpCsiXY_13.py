
import datetime
def how_unlucky(y):
  count = 0
  for i in range(1,13):
    day = datetime.datetime.strftime(datetime.datetime.strptime(("13"+" "+str(i)+" "+str(y)),"%d %m %Y"),"%A")
    if day == "Friday": 
      count +=1
  return count

