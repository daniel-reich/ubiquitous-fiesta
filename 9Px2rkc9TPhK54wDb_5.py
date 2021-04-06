
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
​
def ecg_seq_index(n):
    temp = [1,2]
    while n not in temp:
        for i in range(3,9999):
            if i not in temp:
                if gcd(temp[-1],i) > 1:
                    temp.append(i)
                    break
​
    return temp.index(n)

