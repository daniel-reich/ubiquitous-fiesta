
def numbers_need_friends_too(n):
    n = str(n)
    temp = ''
    for i in range(len(n)-1):
        if n[i] != n[i+1]:
            temp += n[i]+','
        else:
            temp += n[i]
    temp += n[i+1]
    temp = temp.split(',')
​
    for i in range(len(temp)):
        if len(temp[i]) == 1:
            temp[i] = temp[i]*3
​
​
    return int(''.join(temp))

