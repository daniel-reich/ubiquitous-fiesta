
def seating_students(lst):
    left_column = []
    right_column = []
    for i in range(1, lst[0] + 1):
        if i not in lst[1:] and i % 2 != 0:
            left_column.append(i)
        elif i in lst[1:] and i % 2 != 0:
            left_column.append(-1)
        elif i not in lst[1:] and i % 2 == 0:
            right_column.append(i)
        elif i in lst[1:] and i % 2 == 0:
            right_column.append(-1)
    cnt = 0
    for i in range(0, len(left_column) - 1):
        if left_column[i + 1] - left_column[i] == 2:
            cnt += 1
        if right_column[i + 1] - right_column[i] == 2:
            cnt += 1
        if right_column[i] - left_column[i] == 1:
            cnt += 1
    if right_column[len(left_column) -1] - left_column[len(left_column) -1] == 1:
        cnt += 1
    return cnt

