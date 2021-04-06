
def list_less_than_100(lst):
    total = 0
    for num in lst:
        total += num
    if total < 100:
        return True
    else:
        return False

