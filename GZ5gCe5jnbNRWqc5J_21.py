
from datetime import datetime;
def first_tuesday_of_the_month(year, month): 
    for i in range(1,10):
        if datetime(year, month,i).strftime("%A") == "Tuesday":
            return datetime(year, month,i).strftime("%Y-%m-%d")
    return False,"No good!";

