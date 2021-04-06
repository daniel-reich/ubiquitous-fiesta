
def lychrel(n) :
    num = n
    if str(n) != str(n)[: :-1] :
        for x in range(500):
            sum = num+(int(str(num)[::-1]))
            if str(sum) != str(sum)[::-1]:
                num = sum
            else:
                return x+1
    else:return 0
    return True

