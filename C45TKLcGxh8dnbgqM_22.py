
def caesar_cipher(s, k):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            val = (ord(s[i]) - 97 + k) % 26 + 97
            s[i] = chr(((ord(s[i]) - 97 + k) % 26 + 97))
        if s[i].isupper():
            s[i] = chr(((ord(s[i]) - 65 + k) % 26 + 65))
​
    return ''.join(s)

