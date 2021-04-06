
def keyword_cipher(key, message):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    k = list(key)
    for i in range(1,len(k)):
        if k[i] in k[:i]:
            k[i] = '.'
    i = 0
    while i < len(k):
        if k[i] == '.':
            del k[i]
        else:
            i += 1
        
    for i in a:
        if i not in k:
            k.append(i)
    myans = ''
    for i in message:
        if i not in a:
            myans += i
        else:
            myans += k[a.index(i)]
  
    return myans

