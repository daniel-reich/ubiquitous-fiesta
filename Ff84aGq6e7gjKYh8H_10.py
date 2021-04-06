
def minutes_to_seconds(time):
    number = "0123456789"
    arr = []
    for i in time:
        if i in number:
            arr.append(i)
​
    arr1 = int("".join(arr[:-2]))
    arr2 = int("".join(arr[-2:]))
​
    if arr2 >= 60:
        return False
    return arr1 * 60 + arr2

