
def change(x, times):
    new_x=x.copy()
    for i in range(len(new_x)):
        j = 1
        while j <= times:
              if i >= j and i < len(new_x)-j:
                new_x[i] -= 1
              j += 1
    return new_x
​
x = [3, 3, 3, 3, 3, 3, 3]

