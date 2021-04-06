
def seating_students(lst):
    k = lst[0]
    occupied = set(lst[1:])
    empty = set([seat for seat in range(1,k+1) if not seat in occupied])
    total = 0
    for seat in range(1,k+1):
        if not seat in occupied:
            if seat + 2 in empty:
                total += 1
            if seat - 2 in empty:
                total += 1
            if seat %  2 == 0 and seat - 1 in empty:
                total += 1
            if seat %  2 == 1 and seat + 1 in empty:
                total += 1
    return total / 2

