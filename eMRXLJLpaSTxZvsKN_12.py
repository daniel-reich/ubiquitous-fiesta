
def is_ladder_safe(ldr):
    count = 0
    if len(ldr[0]) >= 5:
        count += 1
    else:
        return False
​
    arr = []
    for i in range(len(ldr)):
        arr.append(ldr[i].count("#"))
​
    if len(set(arr)) != 2:
        return False
    else:
        count += 1
​
    arr3 = []
    for i in range(len(arr))[1:-1:3]:
        arr3.append(arr[i:i + 3])
​
    if arr3[0] == arr3[1]:
        count += 1
    else:
        return False
​
    return count == 3

