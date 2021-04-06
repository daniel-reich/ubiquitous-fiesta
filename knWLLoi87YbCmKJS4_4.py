
def happy(n):
    temp = n
    map = {}
​
    output = 0
​
    while temp !=1:
        output =0
        while temp>0:
            rem = temp%10
            output = output+ rem*rem
​
            temp = int(temp/10)
        temp = output
        if output not in map:
            map[output]=1
        else:
            break
​
    if temp ==1:
        return True
    else:
        return False

