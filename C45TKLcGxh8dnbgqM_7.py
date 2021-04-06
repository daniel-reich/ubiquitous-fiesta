
def caesar_cipher(s, k):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
​
    num ={}
    let ={}
​
    for i in range(26):
        chr = alpha[i]
        num [chr]=i
        let[i] = chr
​
    out =''
​
    for i in range(len(s)):
        flag = False
        if s[i].isupper() : flag = True
        try:
            n = num[s[i].lower()]
            l = let [(n+k)%26]
            if flag : l=l.upper()
        except:
            l=s[i]
        out += l
​
    return out

