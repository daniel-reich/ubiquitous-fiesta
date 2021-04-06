
def binary_clock(time):
    time=time.replace(':','')
    clock=[' b d f',' bcdef','abcdef','abcdef']
    for i in range(6):
        fill=4*(i%2==1)+3*(i%2==0)-(i==0)        
        digit=(str(bin(int(time[i])))[2:].zfill(fill))
        char=chr(i+97)
        for j in range(fill):
            for k in range(4):
                if char in clock[k]:
                    n=clock[k].replace(char,digit[j])
                    clock.pop(k)
                    clock.insert(k,n)
                    break
    return clock

