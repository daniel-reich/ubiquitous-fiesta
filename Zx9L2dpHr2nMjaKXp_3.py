
def int_to_vlq(n):
    num = bin(n)[2:]
    size = len(num)
    lst = [num[i-7 if i -7 >0 else 0:i] for i in range(size,0,-7)]
    ans = []
    for i,j in enumerate(lst):
        if i == 0:
            ans.append(int('0' * (8 - len(j)) + j,2)) 
        else:
            ans.append(int('1' + '0' * (7 - len(j)) + j,2))
    return ans[::-1]
​
def vlq_to_int(lst):
    size = len(lst)
    ans = [(j - 128) * 128 ** (size - 1 - i) if i != size - 1 else j for i,j in enumerate(lst)]
    return sum(ans)

