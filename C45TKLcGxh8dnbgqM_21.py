
def caesar_cipher(s, k):
    s = list(s)
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*10
    for i in range(0,len(s)):
        if s[i].isalpha() == True:
            if s[i].islower() == True:
                  s[i] = abc[abc.index(s[i])+k]
            else:
                s[i] = s[i].lower()
                s[i] = abc[abc.index(s[i])+k].upper()
​
    return "".join(s)

