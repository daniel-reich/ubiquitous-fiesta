
import datetime
​
def manage_delays(train,dest,delay):
    if dest in train.destinations:
        currtime = datetime.datetime.strptime(train.expected_time,'%H:%M')
        newtime = currtime + datetime.timedelta(minutes=delay)
        train.expected_time = "{}:{:0>2}".format(newtime.hour,newtime.minute)

