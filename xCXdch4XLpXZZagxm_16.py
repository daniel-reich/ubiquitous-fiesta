
import calendar as cl
def num_of_leapyears(y):
  y1,y2=map(int,y.split('-'))
  return cl.leapdays(y1,y2+1)

