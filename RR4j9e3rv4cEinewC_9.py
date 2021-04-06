
def hats(lst):
    hat,lines = lst[0],lst[1]
    cycle = sum([1 / i for i in lines])
    minutes = int(hat // cycle)
    t_hats = sum([minutes // i for i in lines])
    while True: 
        if t_hats == hat:    
            if minutes == 1:
                return '{} minute'.format(minutes)    
            return '{} minutes'.format(minutes)
        if t_hats > hat:
            return None
        minutes += 1
        for i in lines:
            if minutes % i == 0:
                t_hats += 1

