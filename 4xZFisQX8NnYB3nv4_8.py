
def maximum_seating(lst):
    seat_count = 0
    buff = [0,0]
    valid_seat = buff + [0] + buff
    
    #isles cout as buffer
    lst = buff + lst + buff
​
    for i in range(len(lst)):
        if lst[i:i+len(valid_seat)] == valid_seat:
            lst[i+len(buff)] = 1
            seat_count += 1
​
    return seat_count

