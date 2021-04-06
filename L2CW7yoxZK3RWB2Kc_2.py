
def nico_cipher(message, key):
    a = sorted(key)
    k = sorted([(a.index(key[i]),i) for i in range(len(key))])
    j = 0
    l = 0
    message += ' ' * (len(key) - len(message) % len(key)) 
    ans = ''
    for i in message:
        ans += message[k[j][1]+l]
        if j + 1 < len(key):
            j += 1
        else:
            j = 0
            l += len(key)
    return ans

