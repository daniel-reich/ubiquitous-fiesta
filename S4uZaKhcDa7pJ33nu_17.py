
from datetime import datetime, timedelta
​
​
def week_after(d):
    d = datetime.strptime(d, "%d/%m/%Y")
    week = timedelta(weeks=1)
    new_date = d + week
    return new_date.strftime("%d/%m/%Y")

