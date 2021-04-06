
def seating_students(lst):
    
    updt_seat = [x if not x in lst[1:] else "#" for x in range(1, lst[0]+1)]
    count = 0
    for each in updt_seat:
        if each != "#":
            if each % 2 and each != updt_seat[-1]:
                if updt_seat[each] != "#":
                    count+=1
            if each < len(updt_seat) - 1 and updt_seat[each+1] != "#":
                count += 1
    return count

