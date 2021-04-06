
def swap_cards(n1, n2):
    a = [int(i) for i in list(str(n1))]
    b = [int(i) for i in list(str(n2))]
    b2 = int(str(min(a)) + str(b[1]))
    for i in range(len(a)):
        if a[i] == min(a) and a[0] != a[1]:
            a[i] = b[0]
        elif a[0] ==a[1]:
            a[0]=b[0]
​
    if int(str(a[0])+str(a[1])) > b2:
        return True
    return False

