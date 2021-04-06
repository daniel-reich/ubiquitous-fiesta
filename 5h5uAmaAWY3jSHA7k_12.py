
def landscape_type(lst):
    direction = []
    change = False
    for index, num in enumerate(lst[:-1]):
        if lst[index] < lst[index+1]:
            direction.append('inc')
        elif lst[index] > lst[index+1]:
            direction.append('dec')
    print(direction)
    for index, value in enumerate(direction[:-1]):
        if direction[index] != direction[index+1] and not change:
            change = True
        elif direction[index] != direction[index+1] and change:
            return 'neither'
        elif len(set(direction)) == 1:
            return 'neither'
​
    if direction[0] == 'inc':
        return 'mountain'
    else:
        return 'valley'

