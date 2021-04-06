
import datetime  
from datetime import date 
  
def first_tuesday_of_the_month(year, month): 
    day = 1
    born = datetime.date(year, month, day) 
    while born.strftime("%A") != "Tuesday":
      born = datetime.date(year, month, day) 
      day += 1
    return "{}-{}-{}".format(year, str(month).zfill(2), str(day - 1).zfill(2) if day > 1 else \
       str(day).zfill(2))

