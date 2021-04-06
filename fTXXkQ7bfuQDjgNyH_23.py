
import datetime
def day_of_year(date):
    a = datetime.datetime.strptime(date,'%m/%d/%Y')    
    return int(a.strftime('%j'))

