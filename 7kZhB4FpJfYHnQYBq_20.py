
def lcm_three(num):
    a = num[0]*num[1]*num[2]
    for i in range(1,a+1):
        if i%num[0]==0 and i%num[1]==0 and i%num[2]==0:
            return i

