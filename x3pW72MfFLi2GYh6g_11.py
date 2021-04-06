
def is_scalable(lst):
    for i in range(1, len(lst)-1):
        if lst[i] - lst[i-1] > 5 or lst[i+1] - lst[i] > 5:
            return False
    return True

