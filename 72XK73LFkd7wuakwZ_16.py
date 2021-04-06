
def find_sum(num):
    x = 0
    for i in str(num):
        x = x + int(i)
    return x
​
​
def junction_or_self(n):
    lst = []
    for num in list(range(1, n)):
        total = find_sum(num) + num
        if total == n:
            lst.append(num)
    if not lst:
        return "Self"
    else:
        lst.sort(reverse=True)
        return lst

