
def seating_students(lst):
    total = 0
    y, z = lst[0], list(lst[1:])
    for x in range(1, y + 1):
        for i in (1, 2)[x%2 == 0:]:
            if x not in z and x + i not in z and x + i <= y:
                total += 1
    return total

