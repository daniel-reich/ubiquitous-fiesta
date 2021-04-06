
def strong_password(password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    s=[0,0,0,0]
    count=0
    for i in password:
        if i in numbers:
            s[0]+=1
        if i in lower_case:
            s[1]+=1
        if i in upper_case:
            s[2]+=1
        if i in special_characters:
            s[3]+=1
    for i in s:
        if i==0:
            count+=1
    if count+len(password)<6:
        return 6-len(password)
    else :
        return count

