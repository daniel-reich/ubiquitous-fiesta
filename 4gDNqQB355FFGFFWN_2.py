
def available_spots(lst, num):
    count = 0
    for i in range(len(lst) - 1):
        n1, n2 = lst[i] % 2, lst[i + 1] % 2
        if num % 2 and (n1 or n2):
            count += 1
        elif not num % 2 and (not n1 or not n2):
            count += 1
    return count

