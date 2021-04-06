
def maya_number(n):
    lst = []
    while n > 20:
        for i in range(20):
            if (n-i) % 20 == 0:
                lst.append(i)
                n = (n - i) // 20
                break
    lst.append(n)
    return ['@' if i == 0 else 'o'*(i%5) + '-'*(i//5) for i in lst[::-1]]

