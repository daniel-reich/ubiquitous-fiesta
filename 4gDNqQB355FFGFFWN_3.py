
def available_spots(lst, num):
    count = 0
    num = num % 2
    for x in range(len(lst) - 1):
        if lst[x] % 2 == num or lst[x + 1] % 2 == num:
            count += 1
    return count

