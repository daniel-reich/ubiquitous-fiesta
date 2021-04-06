
def fibonacci(num):
    fbnc_dct = {}
​
    i = 0
    num = num + 2
​
    while i < num:
        if i == 0:
            fbnc_dct[i] = 0
        elif i == 1:
            fbnc_dct[i] = 1
        else:
            fbnc_dct[i] = fbnc_dct[i-1] + fbnc_dct[i-2]
​
        i += 1
​
    return fbnc_dct[num - 1]

