
def available_spots(lst, num):
    count = 0
​
    if num % 2 == 1:
        for i in range(len(lst) - 1):
            if lst[i] % 2 == 0 and lst[i + 1] % 2 == 0:
                continue
            else:
                count += 1
    else:
        for i in range(len(lst) - 1):
            if lst[i] % 2 == 1 and lst[i + 1] % 2 == 1:
                continue
            else:
                count += 1
    return count

