
class Train:
    def __init__(self,destinations,expected_time):
        self.destinations = destinations
        self.expected_time = expected_time
​
def manage_delays(obj, dest, delay):
​
    m = 0
    h = 0
    if dest in obj.destinations:
        t = obj.expected_time.split(':')
        m = int(t[1]) + delay
        h = int(t[0])
        if m > 59:
            h = h + m//60
            m = m%60
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        t = '{}:{}'.format(h,m)
        obj.expected_time = t
    return()

