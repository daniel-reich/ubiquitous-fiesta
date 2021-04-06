
import datetime
def day_of_year(date):
    x=date.split("/")
    day = datetime.datetime(int(x[2]),int(x[0]),int(x[1]))
    return int(day.strftime("%j"))

