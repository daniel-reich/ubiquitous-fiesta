
def make_change(c):
    money = c
​
    qd = money // 25
    money -= qd * 25
​
    dd = money // 10
    money -= dd * 10
​
    nd = money // 5
    money -= nd * 5
​
    pd = money // 1
    money -= pd * 1
​
    return {'q': qd, 'd': dd, 'n': nd, 'p': pd}

