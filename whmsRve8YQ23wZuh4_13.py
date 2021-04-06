
def calculate(d):
    D, M, Y, h, m = int(d[:2]), int(d[3:5]), int(d[6:10]), int(d[11:13]), int(d[14:])
    return Y*100000 + M*10000 + D*1000 + h*100 + m
​
def sort_dates(lst, mode):
    return sorted(lst, key=calculate, reverse=mode == 'DSC')

