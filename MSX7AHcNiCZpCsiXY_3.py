
import datetime
def how_unlucky(y):
  days = list(map(lambda x: datetime.datetime(y,x,13).strftime("%w"),range(1,13)))
  return len(list(filter(lambda x: x == '5', days)))

