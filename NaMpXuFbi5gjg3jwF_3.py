
def sock_pairs(socks):
    count=0
    for i in set(socks):
        count=count+int(socks.count(i)//2)
    return count

