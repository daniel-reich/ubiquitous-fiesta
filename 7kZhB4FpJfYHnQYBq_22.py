
def lcm_three(num):
    num.sort()
    big =num[-1]
    x=1
    while True:
        if (big*x)%num[0] == 0 and (big*x)%num[1] ==0:
            return big*x
        x+=1

