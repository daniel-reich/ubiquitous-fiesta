
import datetime
​
def time_difference(city_a, timestamp, city_b):
    z = {'Los Angeles':-8,'New York':-5,'Caracas':-4.5,'Buenos Aires':-3,'London':0,'Rome':1,'Moscow':3,'Tehran':3.5,'New Delhi':5.5,'Beijing':8,'Canberra':10}
    x = z[city_b]-z[city_a]
​
    a = datetime.datetime.strptime(timestamp, '%B %d, %Y %H:%M')
    b = a+datetime.timedelta(hours=x)
​
    c = datetime.datetime.strftime(b, '%Y-%m-%d %H:%M')
    c = c.replace('-0','-')
​
    return c

