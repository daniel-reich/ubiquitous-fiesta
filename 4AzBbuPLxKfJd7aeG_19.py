
def encrypt(key, message):
    a, d = [], {}
    for i in range(len(key)//2):
        if not key[2*i] in d: d.update({key[2*i]:key[2*i+1]})
        if not key[2*i+1] in d:d.update({key[2*i+1]:key[2*i]})
    for i in message:
        if i in key: a.append(d[i])
        else: a.append(i)
    return "".join(a)

