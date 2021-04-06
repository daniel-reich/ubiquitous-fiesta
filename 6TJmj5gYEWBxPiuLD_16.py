
def seating_students(lst):
    save_1 = 0
    save_2 = 0
    save_1i = []
    save_2i = []
    count_1 = 0
    count_2 = 0
    com_12 = 0
    dek_num = lst[0]
    dek_col1 = [x for x in range(dek_num) if x % 2 != 0]
    dek_col2 = [x+2 for x in range(dek_num) if x % 2 == 0]
    totl_num = (lst[0]/2) * 3 - 2
    for i in lst[1:]:
           dek_col1 = ['#' if val == i else val for val in dek_col1]
           dek_col2 = ['#' if val == i else val for val in dek_col2]
​
    for i in range(len(dek_col1)-1):
        if dek_col1[i] == dek_col1[i+1]:
            save_1 += 1
            save_1i.append(i)
​
    for i in range(len(dek_col2)-1):
        if dek_col2[i] == dek_col2[i+1]:
            save_2 += 1
            save_2i.append(i)
​
    for i in range(len(dek_col1)-1):
        if dek_col1[i] == dek_col2 [i]:
            com_12 +=1
​
​
    for i, j in enumerate(dek_col1):
        if j == '#' and i != 0 and i != len(dek_col1)-1:
            count_1 += 3
        elif j == '#':
            count_1 += 2
​
    for i, j in enumerate(dek_col2):
        if j == '#' and i != 0  and i != len(dek_col2)-1:
            count_2 += 3
        elif j == '#':
            count_2 += 2
​
    return totl_num + save_1 + save_2 + com_12 - count_1 - count_2

