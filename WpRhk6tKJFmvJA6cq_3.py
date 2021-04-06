
"""
class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time
​
    def get_expected_time(self):
        return self.expected_time
​
    def set_expected_time(self, expected_time):
        self.expected_time = expected_time
​
    def manage_delays(self, dest, delay):
        if dest in self.destinations:
            h, m = [int(_) for _ in self.expected_time.split(':')]
            m += delay
            h += m // 60
            m %= 60
            h %= 24
            new_time = str(h).zfill(2) + ':' + str(m).zfill(2)
            self.expected_time = new_time
        return self.expected_time
"""
​
def manage_delays(train, dest, delay):
    #train.manage_delays(dest, delay)
    #return train.get_expected_time()
    if dest in train.destinations:
        h, m = [int(_) for _ in train.expected_time.split(':')]
        m += delay
        h += m // 60
        m %= 60
        h %= 24
        new_time = str(h).zfill(2) + ':' + str(m).zfill(2)
        train.expected_time = new_time
    return train.expected_time

