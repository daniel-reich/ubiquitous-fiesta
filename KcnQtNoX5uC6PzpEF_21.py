
def check_sum(lst, n):
    for x in range(0, len(lst)):
        for y in range(0, len(lst)):
            if lst[x]+lst[y]==n:
                return True
            else:
                y+=1
    return False

