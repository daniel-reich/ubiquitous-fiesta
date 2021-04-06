
def mark_maths(lst):
    count = 0
    for i in range(len(lst)):
        new_lst = lst[i].split('=')
        if new_lst[0][1] == '+':
            sum = int(new_lst[0][0]) + int(new_lst[0][-1])
            if sum == int(new_lst[-1]):
                count += 1
        elif new_lst[0][1] == '-':
            sum = int(new_lst[0][0]) - int(new_lst[0][-1])
            if sum == int(new_lst[-1]):
                count += 1
    return str((round((100/len(lst))*count)))+'%'

