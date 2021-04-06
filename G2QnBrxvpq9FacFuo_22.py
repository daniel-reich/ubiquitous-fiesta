
def possible_path(lst):
    rooms = [1, 2, 3, 4]
    for i in range(1, len(lst)):
        if lst[i] in rooms and lst[i-1] in rooms:
            return False
    return True

