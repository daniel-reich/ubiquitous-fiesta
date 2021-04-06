
def car_timer(n):
    hr = sum([int(i) for i in str(list(divmod(n, 60))[0])])
    min = sum([int(i) for i in str(list(divmod(n, 60))[1])])
    return hr+min

