
class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time
def manage_delays(train,town,delay):
    print("check1")
    hour = int(train.expected_time.split(":")[0])
    minute = int(train.expected_time.split(":")[1])
    print("check2")
    if town in train.destinations:
        print("check3")
        for i in range(1,delay+1):
            minute += +1
            if minute == 60:
                minute = 0
                hour += 1
                if hour == 24:
                    hour = 0
            else:
                print("check4")
                pass
    print("check5")
    if len(str(hour)) == 1:
        print("check6")
        hour = "0" + str(hour)
    if len(str(minute)) == 1:
        print("check7")
        minute = "0" + str(minute)
    print("check8")
    train.expected_time = str(hour)+":"+ str(minute)

