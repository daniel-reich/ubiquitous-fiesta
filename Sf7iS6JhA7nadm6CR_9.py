
def divisibility_rule(n):
    seq = [1, 10, 9, 12, 3, 4]
    num = str(n)
    seq += seq * (len(num) // 6)
    temp = 0
    while True:
        for i,j in zip(num[::-1],seq):
            temp += int(i) * j
        if int(num) == temp:
            return int(num)
        num = str(temp)
        temp = 0

