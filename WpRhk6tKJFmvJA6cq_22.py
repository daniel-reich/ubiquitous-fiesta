
import datetime
def manage_delays(t,dest,delay):
    if dest in t.destinations:
        prevu = datetime.datetime.strptime(t.expected_time, '%H:%M')
        real = (prevu + datetime.timedelta(minutes=delay)).strftime("%H:%M")
        t.expected_time= real

