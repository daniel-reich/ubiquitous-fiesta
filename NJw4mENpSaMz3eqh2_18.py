
def is_undulating(n):
    a = [int(i) for i in str(n)]
    if len(a) <= 2:
        return False
​
    for i in range(2, len(a)):
        if a[i - 2] != a[i]:
            return False
​
    return True

