
def caesar_cipher(s, k):
    s1=""
    for i in s:
        if i.isalpha():
            if i.isupper():
                s1+=chr((ord(i)-ord("A")+k)%26+ord("A"))
            else :
                s1+=chr((ord(i)-ord("a")+k)%26+ord("a"))
        else :
            s1+=i
    return s1

