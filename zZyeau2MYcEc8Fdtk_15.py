
def round_number(num, n):
    m=num
    while True:
        m+=1
        num-=1
        if m%n==0:
            return m
        if num%n==0:
            return num

