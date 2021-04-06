
def sock_pairs(socks):
    countA = 0
    countB = 0
    countC = 0
    
    countA = socks.count("A") // 2
    countB = socks.count("B") // 2
    countC = socks.count("C") // 2
    
    return countA + countB + countC

