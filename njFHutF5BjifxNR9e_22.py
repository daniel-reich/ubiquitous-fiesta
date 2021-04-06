
def change(y, times):
    x = y.copy()
    for i in range(len(x)):
        j = 1
        while j <= times:
            if i >= j and i < len(x)-j:
                x[i] -= 1
            j += 1
    return x
​
x = [3, 3, 3, 3, 3, 3, 3]

