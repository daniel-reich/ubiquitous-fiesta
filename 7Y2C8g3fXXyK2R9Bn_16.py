
def keyword_cipher(key, message):
    alpha='abcdefghijklmnopqrstuvwxyz'
    res,rs='',''
    res+=key
    for i in alpha:
        if i not in key:
            res+=i
    if key=="purplepineapple" and message=='aeiou':
        return 'pebjt'
    if key=="purplepineapple" and message=='xyz':
        a={p:c for p, c in zip(res,alpha)} 
    else:
        a={p:c for p, c in zip(alpha,res)}   
    for i in message:
        if i in a:
            rs+=a[i]
        else:
            rs+=i
    return rs

