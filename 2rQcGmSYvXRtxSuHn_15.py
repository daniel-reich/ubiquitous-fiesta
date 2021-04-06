
def rotate_matrix(lst, num = 1):
    result_1 = []
    result_2 = []
    for _ in range(len(lst)):
        result_1.append(["0" for _ in range(len(lst[0]))])  # result_1 is same as lst
    for _ in range(len(lst[0])):
        result_2.append(["0" for _ in range(len(lst))])  # result_2 is a first rotation shape of lst
    if num == 0:
        return lst
    elif num == 1:  # clockwise rotation
        for i in range(len(lst[0])):
            for j in range(len(lst)):
                result_2[i][j] = lst[len(lst) - 1 - j][i]
        return result_2
    elif num == 2:
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                result_1[i][j] = lst[len(lst) - 1 - i][len(lst[0]) - 1 - j]
        return result_1
    elif 2 < num < 4:
        return rotate_matrix(rotate_matrix(lst, 1), num - 1)
    elif num >= 4:
        return rotate_matrix(lst, num % 4)
    elif num == -1:  # counter_clockwise rotation
        for i in range(len(lst[0])):
            for j in range(len(lst)):
                result_2[i][j] = lst[j][len(lst[0]) - 1 - i]
        return result_2
    elif num == -2:
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                result_1[i][j] = lst[len(lst) - 1 - i][len(lst[0]) - 1 - j]
        return result_1
    elif -4 < num < -2:
        return rotate_matrix(rotate_matrix(lst, 1), num + 1)
    elif num <= -4:
        return rotate_matrix(lst, ((num * -1) % 4) * -1)

