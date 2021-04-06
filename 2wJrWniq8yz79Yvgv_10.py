
def is_narcissistic(list1):
    value = str(list1)
    total = len(value)
    value1 = 0
    res = []
​
    for i in value:
        value = int(i) ** total
        value1 = value1 + value
        res.append(value1)
    if res[-1] == list1:
        return True
    else:
        return False

