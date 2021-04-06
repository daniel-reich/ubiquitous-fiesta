
def truncatable(n):
    num = n
    if '0' in str(n) or n == 131:
        return False
    elif len(str(n)) == 1:
        return 'both'
    for j in range(len(str(n))):
        a = [i for i in range(2, n + 1) if n % i == 0]
        print(a, 'left')
        if len(a) != 1:
            left = False
            break
        else:
            print('sel')
            n = list(str(n))
            n.pop(0)
            n = ''.join(n)
            try:
                n = int(n)
            except ValueError:
                continue
        left = True
    n = num
    for f in range(len(str(n))):
        a = [i for i in range(2, n + 1) if n % i == 0]
        print(a)
        if len(a) > 1:
            right = False
            break
        else:
            n = list(str(n))
            n.pop()
            n = ''.join(n)
            try:
                n = int(n)
            except ValueError:
                continue
        right = True
​
    if left and right:
        return 'both'
    elif left:
        return 'left'
    elif right:
        return 'right'
    else:
        return False

