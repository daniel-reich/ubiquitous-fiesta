
def manage_delays(train, dest, delay):
    time = train.expected_time
    
    time_front = int(time[:2])
    time_tail = int(time[-2:])
    
    if dest in train.destinations:
        time_tail += delay
        n = time_tail//60
        time_front += n
        if time_front>24:
            time_front -= 24 
        time_tail -= 60*n
        
        if time_tail < 10:
            train.expected_time = '{}:0{}'.format(time_front,time_tail)
        else:
            train.expected_time = '{}:{}'.format(time_front,time_tail)
    else:
        pass

