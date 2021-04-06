
def is_zygodrome(num):
    count = []
    num = str(num)
    if len(num)<2:
        return False
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            count.append(i)
    count.append(len(num)-1)
​
    for x in range(len(count)-1):
        if (count[x+1] - count[x]) <2:
            return False
    return True

