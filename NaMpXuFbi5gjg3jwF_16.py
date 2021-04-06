
def sock_pairs(s):
    return sum({i:(s.count(i)-1)//2 if s.count(i)%2!=0 else s.count(i)//2 for i in s}.values())

