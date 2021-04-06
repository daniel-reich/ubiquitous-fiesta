
class Train:
​
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time
​
​
def manage_delays(train, destination, delay):
    if destination in train.destinations:
        h, m = train.expected_time.split(":")
        h, m = int(h) , int(m)
        m = 60 * h + m + delay
        h, m = divmod(m, 60)
        h = h % 24
        if h < 10:
            h = "0" + str(h)
        else:
            h = str(h)
        if m < 10:
            m = "0" + str(m)
        else:
            m = str(m)
​
        train.expected_time = h + ":" + m

