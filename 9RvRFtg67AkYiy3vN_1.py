
def shift_array(arr, direction):
    """Shifts the given array left if direction is -1 and right if it's 1"""
    if direction == -1:
        first_num = arr[0]
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = first_num
            else:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    elif direction == 1:
        last_num = arr[len(arr) - 1]
        for i in range(len(arr) - 1, -1, -1):
            if i == 0:
                arr[i] = last_num
            else:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
    return arr
​
​
​
def left_rotations(txt):
    rotations = [txt]
    for i in range(len(txt) - 1):
        rotation = ''.join(shift_array([i for i in txt], -1))
        rotations.append(rotation)
        txt = rotation
    return rotations
​
​
​
def right_rotations(txt):
    rotations = [txt]
    for i in range(len(txt) - 1):
        rotation = ''.join(shift_array([i for i in txt], 1))
        rotations.append(rotation)
        txt = rotation
    return rotations

