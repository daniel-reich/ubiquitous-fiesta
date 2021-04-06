
def switch_gravity_on(lst):
    for x in range(len(lst[0])):
        count = 0
        for y in range(len(lst)):
            if lst[y][x]== '#':
                count += 1
        for i in range(len(lst)):
            if count>=1:
                lst[-1-i][x] = '#'
                count -=1
            else:
                lst[-1-i][x] = '-'
    return lst

