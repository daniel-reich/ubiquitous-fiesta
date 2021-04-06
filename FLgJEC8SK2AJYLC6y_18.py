
def possible_path(rooms):
    '''
    Returns whether the path through the rooms in rooms is possible
    '''
    ROOMS = {'1': ('2'), '2': ('1','H'), 'H':('2','4'),
             '4': ('H','3'), '3': ('4')}
​
    current = str(rooms[0])
    for i in range(1, len(rooms)):
        possibles = ROOMS[current]
        next_room = str(rooms[i])
        if next_room not in possibles:
            return False
        current = next_room
​
    return True

