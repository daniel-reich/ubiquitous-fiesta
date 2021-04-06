
def stock_picker(lst):
    buy, sell = 0, 0
    for n, i in enumerate(lst):
        for j in lst[n+1:]:
            if j-i > sell - buy:
                buy, sell = i, j
    return sell - buy or -1

