
def is_consecutive(s):
    for i in range(1,len(s)//2 + 1):
        prev = int(s[0:i])
        order = 1 if int(s[0:i]) < int(s[-i:]) else -1
        for j in range(i,len(s),i):
            if int(s[j:j+i]) != prev + order:
                break    
            else:
                prev = int(s[j:j+i])
                if len(s) - i == j:
                    return True
    return False

