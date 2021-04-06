
def numbers_need_friends_too(n):
    n,l,i = str(n),[], 0
    while i < len(n):
        count = 0
        while 1:
            try:
                if n[i + count] == n[i + count + 1]:
                    count += 1
                else: break
            except IndexError:
                break
        l.append(n[i] * (count + 1))
        if count > 0: i+=count
        i+=1
    return int(''.join([i,i*3][len(i)==1] for i in l))

