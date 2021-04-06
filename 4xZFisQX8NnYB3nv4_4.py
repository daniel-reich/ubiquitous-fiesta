
def maximum_seating(lst):
    current_position = 0
    added_seats = 0
    for i in range(current_position, len(lst)):
    
        if lst[i] == 0:
            if i == 0 and i + 2 >= len(lst):
                return 1
            if i == 0 or i == 1:
                if i == 1 and lst[i-1] != 1 and lst[i + 1] != 1 and lst[i + 2] != 1:
                    lst[i] = 1
                    added_seats += 1
                elif i == 0 and lst[i + 1] != 1 and lst[i + 2] != 1:
                    lst[i] = 1
                    added_seats += 1
            elif i == len(lst) - 1 or i == len(lst) - 2:
                if i == len(lst) - 2 and lst[i + 1] != 1 and lst[i - 1] == 0 and lst[i - 2] == 0 :
                    lst[i] = 1
                    added_seats += 1
                elif i == len(lst) - 1 and lst[i - 1] == 0 and lst[i - 2] == 0:
                    lst[i] = 1
                    added_seats += 1
            elif lst[i + 1] == 0 and lst[i + 2] == 0 and lst[i - 1] == 0 and lst[i - 2] == 0:
                lst[i] = 1
                added_seats += 1
​
​
    return added_seats

